import cv2

cap = cv2.VideoCapture(0)

is_recording = False

video_name = "my_video.mp4"

while True:

    ret, frame = cap.read()

    cv2.imshow("Video", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s") and not is_recording:
        is_recording = True

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(video_name, fourcc, 20.0, (frame.shape[1], frame.shape[0]))

    elif key == ord("s") and is_recording:
        is_recording = False
        writer.release()

    if is_recording:
        writer.write(frame)

    if key == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()
