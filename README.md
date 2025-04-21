
## System Requirements
- Python 3.7+
- `friends1.txt` in project root

## Installation Options

### Option 1: Automated Setup (Recommended for First-Time Users)
For users who need a complete environment setup:

#### Linux/Mac:
```bash
# Make script executable (first time only)
#run in project root directory
chmod +x run.sh

# Execute the script
./run.sh
```

### Option 2: Manual Setup (For Existing Virtual Environments)
For users who already manage their own Python environments:

## Required Packages
The system requires these Python packages:
- Flask>=2.0.1
- numpy>=1.21.2
- tensorflow>=2.6.0

1. Activate your virtual environment with required packages installed:
   ```bash
   # Linux/Mac
   source your_env/bin/activate


2. Run the appropriate script:
  
   - **Linux/Mac**:
     ```bash
     chmod +x run_manual.sh
     ./run_manual.sh
     ```

    - **Alternative to using bash**
    - just run the app.py script using python  

## Usage Instructions
1. The web interface will automatically open at `http://localhost:5000`
2. If browser doesn't open automatically:
   - Manually visit the above URL
   - Ensure no other services are using port 5000
   - check using : lsof -i :5000
   - and kill process using : sudo kill -9 <PID>

## Troubleshooting

### Linux/Mac Issues:
- Permission denied:
  ```bash
  sudo chmod +x *.sh
  ```
- Python not found:
  ```bash
  sudo apt install python3 python3-pip  # Debian/Ubuntu
  brew install python                   # MacOS
  ```

## Project Structure
```
root/
├── app.py                 # Main application
├── main.py                # Prediction model
├── friends1.txt           # Dataset
├── run.sh                 # Linux/Mac setup script
├── run_manual.sh          # Linux/Mac manual script
└── templates/
    └── index.html         # Web interface
```

Note: First execution may take several minutes while TensorFlow downloads required models.
```
