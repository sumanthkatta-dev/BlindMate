# BlindMate - Path Buddy

A real-time object detection and navigation assistance application designed to help visually impaired users navigate safely. The system uses YOLOv8 for object detection and provides voice feedback, visual warnings, and turn-by-turn navigation.

## Features

### 🎯 Object Detection
- **Real-time YOLO Detection**: Uses YOLOv8 for fast and accurate object detection
- **Risk Classification**: Categorizes objects into high, medium, and low risk levels
  - **High Risk**: Cars, buses, trucks, motorbikes, bicycles
  - **Medium Risk**: People, animals (dogs, cats, horses, etc.)
  - **Low Risk**: Other objects
- **Distance Estimation**: Calculates approximate distance to detected objects (1m, 2m, 3m+)
- **Direction Indicators**: Shows whether objects are on the left, center, or right

### 🗺️ Navigation System
- **Google Maps Integration**: Real-time navigation with turn-by-turn directions
- **Voice Input**: Speak your destination or choose between casual walk/roaming mode
- **Live Location Tracking**: Continuously updates your position on the map
- **Weather Information**: Displays current weather conditions at your location
- **Distance Tracking**: Shows remaining distance to destination

### 🔊 Accessibility Features
- **Text-to-Speech (TTS)**: Audio announcements for object detection and navigation
- **Beep Alerts**: Sound warnings for high-risk objects
- **Voice Commands**: Hands-free destination input
- **High-Contrast Warnings**: Visual alerts for nearby dangers

### 💡 User Interface
- **Professional Design**: Modern glassmorphism UI with clean blue color scheme
- **Responsive Layout**: Works on desktop and mobile devices
- **Real-time FPS Display**: Shows detection performance
- **Color-Coded Detections**: Easy-to-understand visual feedback
- **Smooth Animations**: Enhanced user experience with transitions

## Technology Stack

### Frontend
- **HTML5/CSS3**: Modern responsive design
- **JavaScript**: Real-time processing and API integration
- **Google Maps API**: Navigation and location services
- **Web Speech API**: Voice recognition and text-to-speech
- **Font Awesome**: Icon library

### Backend
- **FastAPI**: High-performance Python web framework
- **YOLOv8 (Ultralytics)**: State-of-the-art object detection
- **OpenCV**: Image processing
- **NumPy**: Numerical computations

## Installation

### Prerequisites
- Python 3.8 or higher
- Modern web browser with geolocation support
- Webcam/camera access

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/BlindMate.git
   cd BlindMate
   ```

2. **Install Python dependencies**
   ```bash
   pip install fastapi uvicorn ultralytics opencv-python numpy python-multipart
   ```

3. **Download YOLO model**
   - The `yolov8n.pt` model file should be in the project directory
   - If not present, it will be downloaded automatically on first run

4. **Start the backend server**
   ```bash
   uvicorn backend:app --reload --host 127.0.0.1 --port 8000
   ```

### Frontend Setup

1. **Open `index.html`**
   - Simply open the `index.html` file in a modern web browser
   - Or use a local server:
     ```bash
     python -m http.server 8080
     ```
   - Navigate to `http://localhost:8080`

2. **Enable Permissions**
   - Allow camera access when prompted
   - Allow location access for navigation features
   - Allow microphone access for voice commands

## Configuration

### API Keys
Update the following in `index.html`:
- **Google Maps API Key** (line 508): Replace with your API key
- **OpenWeather API Key** (line 507): Replace with your API key

```javascript
const OPENWEATHER_API_KEY = 'your_openweather_api_key';
const GOOGLE_API_KEY = 'your_google_maps_api_key';
```

### Model Customization
- Replace `yolov8n.pt` with a custom-trained model for specific use cases
- Modify risk categories in `backend.py`:
  ```python
  high_risk_labels = {"car", "bus", "truck", "motorbike", "bicycle"}
  medium_risk_labels = {"person", "dog", "cat", "horse", "cow", "sheep"}
  ```

## Usage

### Casual Walk Mode
1. Click "Voice Destination"
2. Say "casual walk" or "roaming"
3. Camera will activate with real-time object detection
4. Navigate safely with visual and audio feedback

### Navigation Mode
1. Click "Voice Destination"
2. Say "destination"
3. Speak your destination when prompted
4. Follow turn-by-turn directions
5. Receive real-time obstacle alerts

### Manual Navigation
1. Type destination in the input field
2. Click "Get Directions"
3. Click "Start Navigation"
4. Follow the route with real-time detection

## Controls

- **Toggle TTS**: Enable/disable voice announcements
- **Toggle Beep**: Enable/disable warning sounds
- **Stop Navigation**: End current navigation session

## Project Structure

```
BlindMate/
├── index.html          # Frontend application
├── backend.py          # FastAPI backend server
├── yolov8n.pt         # YOLO model weights
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Performance

- **Detection Speed**: ~30 FPS on modern hardware
- **Response Time**: Real-time object detection and tracking
- **Accuracy**: Depends on YOLO model (YOLOv8n provides good balance)

## Browser Support

- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ⚠️ Requires HTTPS or localhost for camera/microphone access

## Known Limitations

- Requires good lighting conditions for optimal detection
- GPS accuracy depends on device and environment
- Voice recognition requires clear speech and quiet environment
- Large YOLO model file (~6MB)

## Future Enhancements

- [ ] Offline mode with cached maps
- [ ] Custom voice profiles
- [ ] Multi-language support
- [ ] Depth sensor integration
- [ ] Mobile app version
- [ ] Obstacle avoidance suggestions
- [ ] Community-reported hazards

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- **YOLOv8** by Ultralytics for object detection
- **FastAPI** for the backend framework
- **Google Maps API** for navigation services
- **OpenWeather API** for weather data

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## Author

**Sathwik Chappala**

---

**⚠️ Safety Notice**: This application is designed to assist visually impaired users but should not be used as the sole means of navigation. Always use caution and consider using additional mobility aids.
