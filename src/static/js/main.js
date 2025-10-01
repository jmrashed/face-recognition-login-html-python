// Face Recognition Login JavaScript

let video, canvas, ctx;

// Initialize camera and canvas
async function init() {
    video = document.getElementById('video');
    canvas = document.getElementById('canvas');
    ctx = canvas.getContext('2d');
    
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ 
            video: { width: 640, height: 480 }, 
            audio: false 
        });
        video.srcObject = stream;
    } catch (err) {
        showMessage('Camera access denied or not available', 'danger');
        console.error('Error accessing camera:', err);
    }
}

// Capture image and perform login
async function captureAndLogin() {
    const email = document.getElementById('email').value.trim();
    
    if (!email) {
        showMessage('Please enter your email', 'warning');
        return;
    }
    
    // Set canvas dimensions to match video
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    
    // Draw current video frame to canvas
    ctx.drawImage(video, 0, 0);
    
    // Convert to base64
    const imageData = canvas.toDataURL('image/jpeg', 0.8);
    
    // Show loading message
    showMessage('Processing...', 'info');
    document.getElementById('loginBtn').disabled = true;
    
    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: email,
                image: imageData
            })
        });
        
        const result = await response.json();
        
        if (result.success) {
            showMessage(result.message, 'success');
        } else {
            showMessage(result.message, 'danger');
        }
    } catch (error) {
        showMessage('Network error. Please try again.', 'danger');
        console.error('Login error:', error);
    } finally {
        document.getElementById('loginBtn').disabled = false;
    }
}

// Show message to user
function showMessage(message, type) {
    const messageDiv = document.getElementById('message');
    messageDiv.innerHTML = `<div class="alert alert-${type}" role="alert">${message}</div>`;
    
    // Auto-hide success messages after 3 seconds
    if (type === 'success') {
        setTimeout(() => {
            messageDiv.innerHTML = '';
        }, 3000);
    }
}

// Event listeners
document.addEventListener('DOMContentLoaded', init);
document.getElementById('loginBtn').addEventListener('click', captureAndLogin);

// Allow Enter key to trigger login
document.getElementById('email').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        captureAndLogin();
    }
});