import cv2
import time

class FallDetection:
    def is_fall(self, video_path):
        cap = cv2.VideoCapture(video_path)
        time.sleep(2)
        fgbg = cv2.createBackgroundSubtractorMOG2()
        j = 0
        is_fall = False
        try:
            while (1):
                ret, frame = cap.read()
                # Conver each frame to gray scale and subtract the background
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                fgmask = fgbg.apply(gray)

                # Find contours
                contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                if contours:
                    areas = []
                    for contour in contours:
                        ar = cv2.contourArea(contour)
                        areas.append(ar)

                    max_area = max(areas or [0])
                    max_area_index = areas.index(max_area)
                    cnt = contours[max_area_index]
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.drawContours(fgmask, [cnt], 0, (255, 255, 255), 3, maxLevel=0)
                    if h < w:
                        j += 1
                    if j > 10:
                        print("FALL")
                        cv2.destroyAllWindows()
                        is_fall = True
                        # print "FALL"
                        # cv2.putText(fgmask, 'FALL', (x, y), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 2)
                        cv2.putText(frame, "FALL", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 140, 255), 1)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        break

                    if h > w:
                        j = 0
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    cv2.imshow('video', frame)

                    if cv2.waitKey(33) == 27:
                        break
            cv2.destroyAllWindows()
            return is_fall
        except:
            # print(is_fall)
            return is_fall

# detector = FallDetection()
# result = detector.is_fall("/Users/haminhle/Downloads/fall.mp4")
# print(result)