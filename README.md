# Face Recognition Login System

A modern web-based authentication system using facial recognition technology. Built with Flask, OpenCV, and the face_recognition library.

## Features

- Real-time face detection and recognition
- Web-based interface with camera integration
- Secure user authentication
- Modern responsive design
- RESTful API architecture

## Project Structure

```
face-recognition-login-html-python/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE.md            # License information
├── .gitignore           # Git ignore rules
├── config/              # Configuration files
│   └── config.py        # Application configuration
├── src/                 # Source code
│   ├── static/          # Static assets
│   │   ├── css/         # Stylesheets
│   │   ├── js/          # JavaScript files
│   │   └── images/      # Image assets
│   └── templates/       # HTML templates
│       └── login.html   # Login page template
├── data/                # Data storage
│   └── users/           # User face images
├── models/              # ML models (if needed)
└── temp/                # Temporary files
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Webcam or camera device

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/jmrashed/face-recognition-login.git
   cd face-recognition-login-html-python
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add user images**
   - Place user photos in the `data/users/` directory
   - Name format: `email@domain.com.jpg`
   - Example: `john.doe@example.com.jpg`

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser and go to `http://localhost:5000`

## Usage

1. **Setup User Images**
   - Add clear, front-facing photos of users to `data/users/`
   - Use the email address as the filename (e.g., `user@example.com.jpg`)

2. **Login Process**
   - Enter your email address
   - Allow camera access when prompted
   - Click "Capture & Login" to authenticate
   - The system will compare your face with the stored image

3. **Authentication Results**
   - ✅ Success: Welcome message displayed
   - ❌ Failure: Error message with reason

## API Endpoints

### POST /login
Authenticate user with face recognition

**Request Body:**
```json
{
  "email": "user@example.com",
  "image": "data:image/jpeg;base64,..."
}
```

**Response:**
```json
{
  "success": true,
  "message": "Welcome user@example.com!"
}
```

## Configuration

Edit `config/config.py` to customize:
- File upload limits
- Security settings
- Debug mode
- Data paths

## Security Considerations

- Store user images securely
- Use HTTPS in production
- Implement rate limiting
- Add proper authentication tokens
- Validate file uploads

## Troubleshooting

### Common Issues

1. **Camera not working**
   - Ensure browser has camera permissions
   - Check if camera is being used by another application

2. **Face not detected**
   - Ensure good lighting
   - Face should be clearly visible and front-facing
   - Remove glasses or masks if possible

3. **Installation errors on Windows**
   - Install Visual Studio Build Tools
   - Install CMake
   - Use Python 3.7-3.9 for better compatibility

### Windows Installation

If you encounter issues installing dlib or face_recognition:

```bash
# Install build tools
pip install cmake
pip install dlib
pip install face_recognition
```

For persistent issues, install:
- Visual Studio Build Tools
- CMake (standalone)

## Development

### Running in Development Mode

```bash
export FLASK_ENV=development  # Linux/macOS
set FLASK_ENV=development     # Windows
python app.py
```

### Adding New Features

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Face Recognition**: face_recognition library
- **Computer Vision**: OpenCV, dlib
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5
- **Image Processing**: Pillow (PIL)

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 11+
- Edge 79+

*Note: Requires browsers with WebRTC support for camera access*

## License

This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- [face_recognition](https://github.com/ageitgey/face_recognition) library by Adam Geitgey
- [dlib](http://dlib.net/) library for machine learning
- Bootstrap for responsive design

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Note**: This system is for educational and demonstration purposes. For production use, implement additional security measures and user management features.