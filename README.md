# internship-project
This project basically detects human or living beign on site and is implemented using Artificial intelligence concepts

Import the necessary library, OpenCV (cv2).

Define a function named detect_human_in_video that takes a video file path as input.

Inside the function:

Load a pretrained SVM classifier designed for human detection using HOG features.
Open the video file using cv2.VideoCapture.
Start a loop to process each frame in the video.
Read a frame from the video using cap.read().
Convert the frame to grayscale, as HOG works on grayscale images.
Detect human figures in the frame using the HOG descriptor.
For each detected human, draw a green bounding box around them in the frame.
Display the frame with bounding boxes using cv2.imshow.
Check for the 'Esc' key press to exit the loop.
In the __main__ block:

Specify the path to the video file you want to analyze.
Call the detect_human_in_video function with the video path
