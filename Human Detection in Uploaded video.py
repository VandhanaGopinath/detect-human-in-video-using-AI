import cv2

def detect_human_in_video(video_path):
    # Load the pre-trained SVM classifier for human detection using HOG features
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        # Read a frame from the video
        ret, frame = cap.read()

        if not ret:
            break

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect humans using HOG descriptor
        human_detections, _ = hog.detectMultiScale(gray_frame)

        for (x, y, w, h) in human_detections:
            # Draw bounding boxes around humans
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame with detected humans
        cv2.imshow("Human Detection", frame)

        # Press 'Esc' to exit
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Release the video capture and close the display window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = r"path_to_your_video.mp4"  # Replace with the actual path to your video file
    detect_human_in_video(video_path)
