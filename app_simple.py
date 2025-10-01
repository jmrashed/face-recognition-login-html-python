#!/usr/bin/env python3
"""
Face Recognition Login System - Simplified Version
A Flask web application for face-based authentication
"""

from flask import Flask, render_template, request, jsonify
import os
import io
from base64 import b64decode
from PIL import Image
import numpy as np

app = Flask(__name__, template_folder='src/templates', static_folder='src/static')

# Configuration
USERS_DATA_PATH = 'data/users'
UPLOAD_FOLDER = 'temp'

# Ensure directories exist
os.makedirs(USERS_DATA_PATH, exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    """Main login page"""
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """Process face recognition login - Simplified version"""
    try:
        data = request.get_json()
        email = data.get('email')
        image_data = data.get('image')
        
        if not email or not image_data:
            return jsonify({'success': False, 'message': 'Email and image required'})
        
        # Check if user exists
        user_image_path = os.path.join(USERS_DATA_PATH, f"{email}.jpg")
        if not os.path.exists(user_image_path):
            return jsonify({'success': False, 'message': 'User not found'})
        
        # Decode and save captured image
        header, encoded = image_data.split(',', 1)
        image_bytes = b64decode(encoded)
        
        # Save captured image for verification
        captured_path = os.path.join(UPLOAD_FOLDER, 'captured.jpg')
        with open(captured_path, 'wb') as f:
            f.write(image_bytes)
        
        # For now, simulate face recognition (replace with actual face_recognition when installed)
        # This is a placeholder - install face_recognition for real functionality
        try:
            import face_recognition
            
            # Load images
            pil_image = Image.open(io.BytesIO(image_bytes))
            current_image = np.array(pil_image)
            stored_image = face_recognition.load_image_file(user_image_path)
            
            # Get face encodings
            current_encodings = face_recognition.face_encodings(current_image)
            stored_encodings = face_recognition.face_encodings(stored_image)
            
            if not current_encodings or not stored_encodings:
                return jsonify({'success': False, 'message': 'No face detected'})
            
            # Compare faces
            results = face_recognition.compare_faces([stored_encodings[0]], current_encodings[0])
            
            if results[0]:
                return jsonify({'success': True, 'message': f'Welcome {email}!'})
            else:
                return jsonify({'success': False, 'message': 'Face not recognized'})
                
        except ImportError:
            # Fallback when face_recognition is not installed
            return jsonify({
                'success': True, 
                'message': f'Demo mode: Welcome {email}! (Install face_recognition for real authentication)'
            })
            
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'})

if __name__ == '__main__':
    print("Face Recognition Login System")
    print("=" * 40)
    print("Note: Install face_recognition library for full functionality")
    print("Currently running in demo mode")
    print("Server starting at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)