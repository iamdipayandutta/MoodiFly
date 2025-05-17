const socket = io({
    reconnection: true,
    reconnectionDelay: 1000,
    reconnectionDelayMax: 5000,
    reconnectionAttempts: 5
});

const messageForm = document.getElementById('message-form');
const messageInput = document.getElementById('message-input');
const messagesDiv = document.getElementById('messages');
const currentMoodSpan = document.getElementById('current-mood');
const moodMusic = document.getElementById('mood-music');
const musicName = document.getElementById('music-name');

// Connection status handling
socket.on('connect', () => {
    console.log('Connected to server');
    addSystemMessage('Connected to server');
});

socket.on('disconnect', () => {
    console.log('Disconnected from server');
    addSystemMessage('Disconnected from server');
});

socket.on('connect_error', (error) => {
    console.error('Connection error:', error);
    addSystemMessage('Connection error. Please try again later.');
});

// Message handling
messageForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const message = messageInput.value.trim();
    if (message) {
        try {
            socket.emit('message', { message: message });
            messageInput.value = '';
        } catch (error) {
            console.error('Error sending message:', error);
            addSystemMessage('Error sending message. Please try again.');
        }
    }
});

// Handle received messages (from other users)
socket.on('message', (data) => {
    addMessage(data.message, 'received');
    updateMoodAndMusic(data.mood, data.music);
});

// Handle sent message confirmation
socket.on('message_sent', (data) => {
    addMessage(data.message, 'sent');
    updateMoodAndMusic(data.mood, data.music);
});

socket.on('error', (error) => {
    console.error('Server error:', error);
    addSystemMessage('An error occurred. Please try again.');
});

// Helper functions
function addMessage(message, type) {
    const messageElement = document.createElement('div');
    messageElement.className = `message ${type}`;
    messageElement.textContent = message;
    messagesDiv.appendChild(messageElement);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function addSystemMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.className = 'message system';
    messageElement.textContent = message;
    messagesDiv.appendChild(messageElement);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function updateMoodAndMusic(mood, musicInfo) {
    // Update mood display
    currentMoodSpan.textContent = mood.charAt(0).toUpperCase() + mood.slice(1);
    
    // Update music player
    if (musicInfo && musicInfo.url) {
        moodMusic.src = musicInfo.url;
        musicName.textContent = musicInfo.name;
        moodMusic.play().catch(error => {
            console.error('Error playing music:', error);
        });
    }
} 