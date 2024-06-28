import cv2
import numpy as np

# Initialize game variables
ball_pos = [320, 240]
ball_radius = 10
ball_speed = [4, 4]  # Initial ball speed
initial_ball_speed = [4, 4]

paddle_width = 100
paddle_height = 20
paddle_pos = 320

score = 0
high_score = 0

cap = cv2.VideoCapture(0)

def detect_hand(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_color = np.array([0, 48, 80], dtype="uint8")
    upper_color = np.array([20, 255, 255], dtype="uint8")
    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)
        if radius > 10:
            return int(x)
    return None

def update_game(frame, hand_pos):
    global ball_pos, ball_speed, paddle_pos, score, high_score

    # Update paddle position
    if hand_pos:
        paddle_pos = hand_pos

    # Update ball position
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Ball collision with walls
    if ball_pos[0] <= ball_radius or ball_pos[0] >= frame.shape[1] - ball_radius:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= ball_radius:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with paddle
    if (frame.shape[0] - paddle_height <= ball_pos[1] <= frame.shape[0] and
            paddle_pos - paddle_width // 2 <= ball_pos[0] <= paddle_pos + paddle_width // 2):
        ball_speed[1] = -ball_speed[1]
        score += 1  # Increase score when ball hits paddle
        ball_speed[0] += np.sign(ball_speed[0])  # Increase ball speed
        ball_speed[1] += np.sign(ball_speed[1])

    # Ball out of bounds
    if ball_pos[1] > frame.shape[0]:
        ball_pos = [320, 240]
        ball_speed = initial_ball_speed.copy()  # Reset ball speed
        if score > high_score:
            high_score = score
        score = 0  # Reset score when ball is out of bounds

    return frame

def draw_elements(frame):
    global ball_pos, ball_radius, paddle_pos, paddle_width, paddle_height, score, high_score

    # Draw ball
    cv2.circle(frame, tuple(ball_pos), ball_radius, (0, 255, 0), -1)

    # Draw paddle
    cv2.rectangle(frame, (paddle_pos - paddle_width // 2, frame.shape[0] - paddle_height),
                  (paddle_pos + paddle_width // 2, frame.shape[0]), (255, 0, 0), -1)

    # Draw text
    cv2.putText(frame, 'Use your hand', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, f'Score: {score}', (frame.shape[1] - 150, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, f'High Score: {high_score}', (frame.shape[1] - 250, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    return frame

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hand_pos = detect_hand(frame)
    frame = update_game(frame, hand_pos)
    frame = draw_elements(frame)

    cv2.imshow("Pong", frame)
    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
