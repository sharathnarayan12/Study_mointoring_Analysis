'''
    author @sharath VN
    - collecting bunch of data from keypoints from mediapipe holistic
    - The MediaPipe Holistic Landmarker task lets you combine components of the pose, face, and hand landmarkers to create a complete landmarker for the human body.
    - You can use this task to analyze full-body gestures, poses, and actions.
'''

import cv2
import mediapipe as mp


class HolisticDetection:
    def __init__(self):
        self.mp_holistic = mp.solutions.holistic
        self.mp_drawing = mp.solutions.drawing_utils
        self.model = self.mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.cap = cv2.VideoCapture(2)

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def mediapipe_detection(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = self.model.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        return image, results

    def draw_styled_landmarks(self, image, results):
        self.mp_drawing.draw_landmarks(image, results.face_landmarks, self.mp_holistic.FACEMESH_CONTOURS,
                                        self.mp_drawing.DrawingSpec(color=(80, 110, 10), thickness=1, circle_radius=1),
                                        self.mp_drawing.DrawingSpec(color=(80, 256, 121), thickness=1,
                                                                    circle_radius=1))
        self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS,
                                        self.mp_drawing.DrawingSpec(color=(80, 22, 10), thickness=2, circle_radius=4),
                                        self.mp_drawing.DrawingSpec(color=(80, 44, 121), thickness=2,
                                                                    circle_radius=2))
        self.mp_drawing.draw_landmarks(image, results.left_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS,
                                        self.mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        self.mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=2,
                                                                    circle_radius=2))
        self.mp_drawing.draw_landmarks(image, results.right_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS,
                                        self.mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2,
                                                                    circle_radius=4),
                                        self.mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2,
                                                                    circle_radius=2))
    def Not_Reading_print(self):
        print("NOT READING !!!!!!!!!!!!!!!!")

    def Reading_print(self):
        print("READING !!!!!!!!!!!!!!!!")

    def run_detection(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            
            image, results = self.mediapipe_detection(frame)
            self.draw_styled_landmarks(image, results)

            # Check if the face landmarks are below a horizontal line
            if results.face_landmarks:
                face_landmarks = results.face_landmarks.landmark
                # Get the Y-coordinate of the first face landmark (assuming it's the nose)
                nose_y = int(face_landmarks[2].y * frame.shape[0])
                # Y-coordinate for the horizontal line
                y_coord = 200
                if nose_y > y_coord:
                    # print("Reading")
                    self.Reading_print()
                else:
                    # print("NOT Reading")
                    self.Not_Reading_print()
            else:
                print("NO student detected !!!!!")

            # Show to screen
            cv2.imshow('OpenCV Feed', image)

            # Break gracefully
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()
