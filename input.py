import cv2

def capture_snapshot():
    cap = cv2.VideoCapture(0)
    print("press s = snapshot or q = quit")
    while True:
        ret , frame = cap.read()
        cv2.imshow("webcam",frame)
        key = cv2.waitKey(1)

        if key == ord("s"):   # press S to capture image
            cv2.imwrite("snapshot.jpg", frame)
            print("Snapshot captured!")

            cap.release()
            cv2.destroyAllWindows()
            return "snapshot.jpg"

        elif key == ord("q"): # press Q to quit
            cap.release()
            cv2.destroyAllWindows()

            return None
