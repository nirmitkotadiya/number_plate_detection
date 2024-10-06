# Number Plate Detection using OpenCV

This project demonstrates a number plate detection system using **OpenCV** for image processing. The system identifies license plates from images and highlights them by drawing rectangles around the detected plates.

## Table of Contents

- [Introduction](#introduction)
- [Number Plate Detection System Presentation](#project-presentation)
- [AI In Defence Presentation](#seminar-presentation)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Author](#author)

## Introduction

This project utilizes OpenCV to detect vehicle license plates from images. By using a pre-trained **Haar Cascade** classifier, the system can process images and detect license plates by drawing rectangles around them.

## Project Presentation

For a detailed overview of this project, check out the PowerPoint presentation:

*Warning: Sorry, we can't display files of this size directly here. Please download the presentation to view it on your local system.*

[Number Plate Detection System Presentation](https://github.com/nirmitkotadiya/number_plate_detection/blob/main/Number%20Plate%20Detection.pptx)

## Seminar Presentation

For a detailed overview of the **AI in Defence** seminar, check out the PowerPoint presentation:

*Warning: Sorry, we can't display files of this size directly here. Please download the presentation to view it on your local system.*

[AI in Defence Seminar Presentation](https://github.com/nirmitkotadiya/number_plate_detection/blob/main/AI.pptx)

## Key Features

- **Preprocessing**: Converts the input image to grayscale for efficient plate detection.
- **License Plate Detection**: Uses a pre-trained Haar Cascade classifier to detect license plates from images.
- **Logging**: Logs detection details, such as timestamps and file paths.
- **Image Display and Save**: Saves and displays the image with the detected plates.

## Installation

### Requirements

- Python 3.x
- OpenCV (`cv2`)

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/nirmitkotadiya/number_plate_detection.git
   ```

2. Navigate to the project directory:

   ```bash
   cd number_plate_detection
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```


### Usage

1. Place an image containing a car or vehicle with a license plate in the images folder.
   
2. Run the main.py script:
   ```bash
   python main.py
   ```

3. If a plate is detected, it will be highlighted in the image, saved to the detected_image folder, and a log entry will be recorded.


### Output

- Detected plates are highlighted with rectangles in the image.
- The detection log is saved in number_plate_log.txt.


### Project Structure

- **`detector.py`**: Core detection logic.
  - Detects number plates in images and applies OpenCV’s Haar Cascade model.

- **`main.py`**: Main execution script.
  - Loads images, calls the detection logic, saves the results, and logs the detection.

- **`utils.py`**: Image preprocessing helper functions.
  - Contains functions to convert images to grayscale for better plate detection.

- **`images/`**: Input image folder.
  - Store input images here, such as vehicle images for plate detection.

- **`detected_image/`**: Output folder for detected plates.
  - Stores images with detected license plates highlighted.

- **`model/`**: Haar Cascade model for plate detection.
  - Contains the pre-trained model used to detect vehicle license plates.

- **`number_plate_log.txt`**: Log file for detected plates.
  - Stores logs with timestamps and information about successful detections.

- **`README.md`**: Project documentation.
  - Provides an overview and details about the project structure, usage, and setup.


## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the project.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure that the code is properly documented.
4. Test your changes thoroughly.
5. Submit a pull request with a clear description of your changes.

## Author

This Number Plate Detection System was created by Nirmit Kotadiya & his Team.

Feel free to use and modify this Number Plate Detection System for your own educational purposes or as part of a Python project. If you have any questions or need assistance, please contact the author.

Enjoy the Number Plate Detection System!
