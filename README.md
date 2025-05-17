# MoodiFly - Real-time Chat with Mood-based Music

MoodiFly is a real-time chat application that analyzes the mood of messages and plays corresponding music. When users chat, the application detects their emotional state and changes the background music accordingly.

## Features

- 💬 Real-time chat functionality
- 🎵 Mood-based music playback
- 😊 Sentiment analysis of messages
- 🎨 Modern and responsive UI
- 🔄 Automatic mood detection
- 🎧 Integrated music player

## Mood Categories

The application detects five different moods:
- 😊 Happy - Positive and cheerful messages
- 😢 Sad - Negative or melancholic messages
- ❤️ Love - Messages containing love-related words
- 😠 Angry - Messages with angry or hate-related words
- 😐 Neutral - Messages with neutral sentiment

## Prerequisites

Before you begin, ensure you have:
- Python 3.8 or higher installed
- pip (Python package installer)
- A modern web browser

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/MoodiFly.git
cd MoodiFly
```

2. Create a virtual environment (recommended):
```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Open the same URL in another browser window or device to test the chat functionality.

## How to Use

1. **Starting a Chat**:
   - Open the application in your web browser
   - You'll see a chat interface with a message input box at the bottom

2. **Sending Messages**:
   - Type your message in the input box
   - Press Enter or click the Send button
   - Your message will appear in the chat

3. **Mood Detection**:
   - The application automatically analyzes your message
   - The current mood is displayed at the top of the chat
   - Music will change based on the detected mood

4. **Music Control**:
   - Use the audio player controls to:
     - Play/Pause the music
     - Adjust volume
     - Skip to different parts of the track

## Example Messages to Try

- Happy mood: "I'm so happy today!" or "This is amazing!"
- Sad mood: "I'm feeling down" or "This is terrible"
- Love mood: "I love you" or "You're my heart"
- Angry mood: "I'm angry" or "I hate this"
- Neutral mood: "Hello" or "How are you?"

## Project Structure

```
MoodiFly/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css  # Styling for the application
│   └── js/
│       └── script.js  # Frontend JavaScript code
└── templates/
    └── index.html     # Main HTML template
```

## Customization

### Changing Music Tracks

To change the music tracks, edit the `MOOD_MUSIC` dictionary in `app.py`:

```python
MOOD_MUSIC = {
    'happy': {
        'name': 'Your Happy Song',
        'url': 'your-music-url.mp3'
    },
    # Add other moods...
}
```

### Modifying Mood Detection

The mood detection can be customized in the `analyze_mood` function in `app.py`:

```python
def analyze_mood(text):
    # Add your custom mood detection logic here
    pass
```

## Troubleshooting

1. **Music Not Playing**:
   - Check if your browser allows autoplay
   - Ensure the music URLs are accessible
   - Try refreshing the page

2. **Chat Not Working**:
   - Check if the Flask server is running
   - Ensure both users are connected to the same server
   - Check browser console for any errors

3. **Installation Issues**:
   - Make sure Python is installed correctly
   - Try updating pip: `python -m pip install --upgrade pip`
   - Check if all requirements are installed: `pip list`

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch
3. Making your changes
4. Submitting a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask and Flask-SocketIO for the backend
- TextBlob for sentiment analysis
- SoundHelix for sample music tracks 
