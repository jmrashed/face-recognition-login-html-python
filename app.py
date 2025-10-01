#!/usr/bin/env python3
"""
Face Recognition Login System
A Flask web application for face-based authentication
"""

from flask import Flask, render_template, request, jsonify
import face_recognition
import numpy as np
from base64 import b64decode
import os
import io
from PIL import Image

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
    """Process face recognition login"""
    try:
        data = request.get_json()
        email = data.get('email')
        image_data = data.get('image')
        
        if not email or not image_data:
            return jsonify({'success': False, 'message': 'Email and image required'})
        
        # Decode base64 image
        header, encoded = image_data.split(',', 1)
        image_bytes = b64decode(encoded)
        
        # Convert to PIL Image and then to numpy array
        pil_image = Image.open(io.BytesIO(image_bytes))
        current_image = np.array(pil_image)
        
        # Load stored user image
        user_image_path = os.path.join(USERS_DATA_PATH, f"{email}.jpg")
        if not os.path.exists(user_image_path):
            return jsonify({'success': False, 'message': 'User not found'})
        
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
            
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)