#!/usr/bin/env python3
"""
Setup script for Face Recognition Login System
"""

import os
import sys

def create_directories():
    """Create necessary directories"""
    directories = [
        'data/users',
        'temp',
        'models',
        'logs'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Created directory: {directory}")

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import flask
        import face_recognition
        import PIL
        import numpy
        print("✓ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def main():
    """Main setup function"""
    print("Face Recognition Login System - Setup")
    print("=" * 40)
    
    # Create directories
    create_directories()
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    print("\n✓ Setup completed successfully!")
    print("\nNext steps:")
    print("1. Add user images to data/users/ directory")
    print("2. Run: python app.py")
    print("3. Open http://localhost:5000 in your browser")

if __name__ == "__main__":
    main()