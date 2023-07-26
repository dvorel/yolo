from ultralytics import YOLO
import cv2

if __name__=="__main__":
    model = YOLO("./yolo/yolov8l.pt")
    cap = cv2.VideoCapture(0)

    while True:

        _, frame = cap.read()

        res = model.predict(frame, show=True)
        for r in res:
            print(r.boxes)
        #cv2.imshow("yolo", frame)
        cv2.waitKey(1)