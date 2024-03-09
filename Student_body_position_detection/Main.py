'''
    author @sharath VN
    - collecting bunch of data from keypoints from mediapipe holistic
    - The MediaPipe Holistic Landmarker task lets you combine components of the pose, face, and hand landmarkers to create a complete landmarker for the human body.
    - You can use this task to analyze full-body gestures, poses, and actions.
'''
import cv2
import mediapipe as mp
import sklearn as sk
import matplotlib.pyplot as plt
import os , time , pandas as pd ,numpy as np

print("done___ ready")


mp_holistic = mp.solutions.holistic # Holistic model
mp_drawing = mp.solutions.drawing_utils # Drawing utilities


def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False                  # Image is no longer writeable
    results = model.process(image)                 # Make prediction
    image.flags.writeable = True                   # Image is now writeable 
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
    return image, results

  
def draw_styled_landmarks(image, results):
    # Draw face connections
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS,
                             mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1), 
                             mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
                             ) 
    # Draw pose connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                             ) 
    # Draw left hand connections
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                             ) 
    # Draw right hand connections  
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                             ) 
# Inside the while loop where you are processing the video feed
    
cap = cv2.VideoCapture(2)
# Set mediapipe model 
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        # Y-coordinate for the horizontal line
        y_coord = 200
        # Start and end points for the horizontal line
        start_point = (0, y_coord)
        end_point = (900, y_coord)  # Assuming the width of the video stream is 640 pixels
        # Black color in BGR
        color = (0, 200, 0, 225) 
        # Line thickness
        thickness = 5
       
        alpha = 0.0
        # Read feed
        ret, frame = cap.read()
        overlay = frame.copy()
        # Draw the horizontal line
        overlay = cv2.line(overlay, start_point, end_point, color, thickness)
        frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

        # Make detections
        image, results = mediapipe_detection(frame, holistic)
        
        # Draw landmarks
        draw_styled_landmarks(image, results)

        # Check if the face landmarks are below the line
        if results.face_landmarks:
            face_landmarks = results.face_landmarks.landmark
            # Get the Y-coordinate of the first face landmark (assuming it's the nose)
        
            nose_y = int(face_landmarks[2].y * frame.shape[0])
            print(face_landmarks[2])
            # Check if the nose Y-coordinate is below the line
            if nose_y > y_coord:
                print("Reading")
            else:
                print("NOT Reading")
        else:
            print("NO student detected !!!!!")
        # Show to screen
        cv2.imshow('OpenCV Feed',image)

        # Break gracefully
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
