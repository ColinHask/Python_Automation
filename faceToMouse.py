import cv2
import mediapipe as mp
import pyautogui

# Disable PyAutoGUI fail-safe (not recommended)
pyautogui.FAILSAFE = False

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize Video Capture
cap = cv2.VideoCapture(0)

# Get screen size for cursor movement
screen_width, screen_height = pyautogui.size()

# Variables to control sensitivity
tilt_sensitivity = 2.0  # Adjust this value to control sensitivity of head tilt
movement_sensitivity = 1.5  # Adjust this value to control overall sensitivity

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
            
            # Move cursor based on eye position and head tilt with overall movement sensitivity
            cursor_x = avg_eye_x * screen_width // frame_width * movement_sensitivity
            cursor_y = (avg_eye_y + head_tilt) * screen_height // frame_height * movement_sensitivity
            
            # Prevent the cursor from moving to the corners of the screen
            cursor_x = min(max(cursor_x, 1), screen_width - 1)
            cursor_y = min(max(cursor_y, 1), screen_height - 1)
            
            pyautogui.moveTo(cursor_x, cursor_y)
    
    # Display the frame
    cv2.imshow('Eye Tracking', frame)
    
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
