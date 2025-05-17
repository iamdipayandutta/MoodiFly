from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room, rooms
from flask_cors import CORS
from textblob import TextBlob
import logging
import os
import sys
import json
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)  # Enable CORS for all routes
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log')
    ]
)
logger = logging.getLogger(__name__)

# Mood to music mapping
MOOD_MUSIC = {
    'happy': {
        'name': 'Happy Mood',
        'url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'
    },
    'sad': {
        'name': 'Sad Mood',
        'url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3'
    },
    'love': {
        'name': 'Love Mood',
        'url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3'
    },
    'angry': {
        'name': 'Angry Mood',
        'url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3'
    },
    'neutral': {
        'name': 'Neutral Mood',
        'url': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3'
    }
}

def analyze_mood(text):
    # Check for specific keywords first
    text_lower = text.lower()
    if 'love' in text_lower or 'heart' in text_lower:
        return 'love'
    if 'angry' in text_lower or 'hate' in text_lower:
        return 'angry'
    
    # Use TextBlob for sentiment analysis
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0.3:
        return 'happy'
    elif polarity < -0.3:
        return 'sad'
    else:
        return 'neutral'

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    logger.info('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    logger.info('Client disconnected')

@socketio.on('message')
def handle_message(data):
    try:
        message = data.get('message', '')
        sender_id = request.sid
        
        # Analyze mood from the message
        mood = analyze_mood(message)
        music_info = MOOD_MUSIC.get(mood, MOOD_MUSIC['neutral'])
        
        # Emit to all clients except the sender
        emit('message', {
            'message': message,
            'sender_id': sender_id,
            'mood': mood,
            'music': music_info
        }, broadcast=True, include_self=False)
        
        # Send confirmation to the sender
        emit('message_sent', {
            'message': message,
            'sender_id': sender_id,
            'mood': mood,
            'music': music_info
        })
        
    except Exception as e:
        logger.error(f"Error handling message: {str(e)}")
        emit('error', {'message': 'An error occurred'})

if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT', 5000))
        socketio.run(app, debug=True, host='0.0.0.0', port=port)
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}") 