import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize Video Capture
cap = cv2.VideoCapture(0)

# Get screen size for cursor movement
screen_width, screen_height = pyautogui.size()

# Variable to control sensitivity of cursor movement based on head tilt
tilt_sensitivity = 2.0  # Adjust this value to control sensitivity

def get_eye_position(landmarks):
    left_eye_x = int((landmarks[362].x + landmarks[263].x) * 0.5 * frame_width)
    left_eye_y = int((landmarks[362].y + landmarks[263].y) * 0.5 * frame_height)
    right_eye_x = int((landmarks[33].x + landmarks[133].x) * 0.5 * frame_width)
    right_eye_y = int((landmarks[33].y + landmarks[133].y) * 0.5 * frame_height)
    
    return (left_eye_x, left_eye_y), (right_eye_x, right_eye_y)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    
    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame and find face landmarks
    results = face_mesh.process(rgb_frame)
    
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            left_eye, right_eye = get_eye_position(face_landmarks.landmark)
            
            # Calculate average eye position
            avg_eye_x = (left_eye[0] + right_eye[0]) // 2
            avg_eye_y = (left_eye[1] + right_eye[1]) // 2
            
            # Calculate the head tilt
            head_tilt = (right_eye[1] - left_eye[1]) * tilt_sensitivity
            
            # Move cursor based on eye position and head tilt
            pyautogui.moveTo(avg_eye_x * screen_width // frame_width, (avg_eye_y + head_tilt) * screen_height // frame_height)
    
    # Display the frame
    cv2.imshow('Eye Tracking', frame)
    
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
