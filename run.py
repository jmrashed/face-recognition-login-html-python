#!/usr/bin/env python3
"""
Run script for Face Recognition Login System
"""

import os
import sys
from app import app

def main():
    """Main run function"""
    print("Starting Face Recognition Login System...")
    print("Server will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()