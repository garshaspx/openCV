import torch

model = torch.load()
print(model['train_args']['nbs'])

import cv2


import torch
from ultralytics import YOLO
# Set device to GPU if available, CPU otherwise
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Initialize model and load weights
model = YOLO('yolov8n.pt').to(device) 

# Run inference
img = torch.rand(1, 3, 640, 640).to(device)  
results = model(img)

# Rest of your code...

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    
    # Move frame to GPU memory 
    frame_gpu = torch.from_numpy(frame).to(device) 
    
    results = model(frame_gpu)
    
    # Plot and display detections    
    frame = results.plot(frame)
    cv2.imshow('Detected', frame)
    
    # etc...



# The key points are:

# Use torch.device to select GPU if available
# Move model to GPU using .to(device)
# Move input image to GPU as torch tensor
# Run model inference on GPU
# Move results back to CPU for plotting/display
# This will enable the YOLOv8 model to leverage the GPU for faster inference.
# Make sure to install PyTorch with CUDA support to access the GPU.