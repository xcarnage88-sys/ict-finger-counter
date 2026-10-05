import cv2
from cvzone.HandTrackingModule import HandDetector

# 0 uses your laptop's built-in webcam
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    if not success:
        print("Camera not detected.")
        break

    hands, img = detector.findHands(img)

    if hands:
        hand1 = hands[0]
        fingers = detector.fingersUp(hand1)
        total_fingers = fingers.count(1)

        cv2.putText(img, f'Count: {total_fingers}', (50, 80),
                    cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv2.imshow("Finger Counter", img)

    # Press 'q' on your keyboard to close the camera window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()