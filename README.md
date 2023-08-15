
Image Processing Application
This is a Python application for real-time object detection, tracking and model training using computer vision and deep learning. It provides a GUI to manage the entire workflow.

-Features

---Object Detection
Uses YOLOv8 object detection model to identify common objects like person, car, pet or any pre-trained object.
Loads a pretrained model and runs inference on input video/images
Displays bounding boxes and labels around detected objects
Provides option to set detection confidence threshold
Uses OpenCV for preprocessing and visualization

---Object Tracking
Tracks identified objects across video frames
Maintains consistent object IDs as they move around
Uses object center positions and IDs for smooth tracking
Handles objects leaving frame and re-entering

---GUI Interface
Built using Tkinter for cross-platform compatibility
Intuitive graphical interface to control full workflow
Options to select input, view real-time detections, start/stop tracking
Settings to configure input camera device and parameters
Status messages and prompts to guide the user

---Image Database
Saves cropped object images to disk for model training
Stores images along with auto-generated annotations
Annotations include class name, coordinates etc.
Prepares dataset in standard format for training

---Model Training
Provides option to train a custom YOLO model on collected images
Uses YOLOv8 model architecture and training code
Allows configuring training hyperparameters like batch size, epochs etc.
Resumes training from previous checkpoints
Exports trained model to use for inference

---Library Manager
Organize multiple databases/libraries of images
Add, delete, activate different libraries
Switch between multiple datasets for model training
---Requirements
Python 3.7 or later
OpenCV
Ultralytics YOLOv8
TensorFlow 2.x
Tkinter, SQLite3 and other standard Python packages

---Usage
Clone this repository
Install requirements
Run python main.py to launch the application
Add new libraries using the library manager
Choose input and start object tracking
View real-time detections on screen
Train custom models using collected images(before training the data set make sure to add YAML file in ML_train folder)
