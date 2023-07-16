import cv2
import numpy as np

# Function to extract features from an image using SIFT
def extract_features(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(gray, None)
    return keypoints, descriptors

# Function to filter unnecessary features using RANSAC
def filter_features(keypoints1, keypoints2, matches, threshold):
    filtered_matches = []
    for match in matches:
        pt1 = keypoints1[match.queryIdx].pt
        pt2 = keypoints2[match.trainIdx].pt
        if np.linalg.norm(np.array(pt1) - np.array(pt2)) < threshold:
            filtered_matches.append(match)
    return filtered_matches

# Load and extract features from the two images
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')
keypoints1, descriptors1 = extract_features(image1)
keypoints2, descriptors2 = extract_features(image2)

# Match the features
matcher = cv2.BFMatcher()
matches = matcher.match(descriptors1, descriptors2)

# Filter the matches
filtered_matches = filter_features(keypoints1, keypoints2, matches, threshold=10)

# Draw the filtered matches
result = cv2.drawMatches(image1, keypoints1, image2, keypoints2, filtered_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Display the result
cv2.imshow('Filtered Matches', result)
cv2.waitKey(0)
cv2.destroyAllWindows()