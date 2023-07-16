import cv2
import numpy as np

# Function to extract features from an image using SIFT
def extract_features(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(gray, None)
    return keypoints, descriptors

# Function to compare and merge features
def merge_features(features_list):
    merged_features = []
    for features in features_list:
        for feature in features:
            if not any(np.array_equal(feature[1], existing_feature[1]) for existing_feature in merged_features):
                merged_features.append(feature)
    return merged_features

# List to store features from multiple images
features_list = []

# Load and extract features from each image
image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']
for image_path in image_paths:
    image = cv2.imread(image_path)
    keypoints, descriptors = extract_features(image)
    features_list.append(descriptors)

# Merge the features
merged_features = merge_features(features_list)

# Save the merged features to a file
np.save('merged_features.npy', merged_features)