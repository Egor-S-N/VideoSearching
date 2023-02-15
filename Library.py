import os
import cv2
import numpy as np
from datetime import date, time, datetime


class Library:
    def __init__(self):
        self._video_source = ""
        self._image_source = ""
        self._index = 0

    @property
    def video_source(self):
        return self._video_source

    @video_source.setter
    def video_source(self, value):
        self._video_source = value

    @property
    def image_source(self) -> str:
        return self._image_source

    @image_source.setter
    def image_source(self, value):
        self._image_source = value

    def show_video(self):
        
        dir_name = str(date.today()) + " " + str(datetime.now().strftime("%H-%M-%S"))
        os.chdir("Results/")
        os.mkdir(dir_name)
        reference_image = cv2.imread(self._image_source, cv2.IMREAD_GRAYSCALE)
        reference_image_resized = cv2.resize(reference_image, (int(reference_image.shape[1]//1.7),int(reference_image.shape[0]//1.7)))

        detector = cv2.SIFT_create()
        keypoints, descriptors = detector.detectAndCompute(reference_image_resized, None)
        video_capture = cv2.VideoCapture(self._video_source)
        while video_capture.isOpened():
            ret, frame = video_capture.read()
            frame_resized = cv2.resize(frame, (int(frame.shape[1]//1.7), int(frame.shape[0]//1.7)))
            gray_frame = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
            current_keypoints, current_descriptors = detector.detectAndCompute(gray_frame, None)

            matcher = cv2.FlannBasedMatcher({'algorithm': 0, 'trees': 5}, {'checks': 50})
            matches = matcher.knnMatch(descriptors, current_descriptors, k=2)

            good_matches = []
            for m, n in matches:
                if m.distance < 0.7 * n.distance:
                    good_matches.append(m)

            if len(good_matches) > 10:
                reference_points = [keypoints[m.queryIdx].pt for m in good_matches]
                current_points = [current_keypoints[m.trainIdx].pt for m in good_matches]
                H, mask = cv2.findHomography(np.float32(reference_points), np.float32(current_points), cv2.RANSAC, 5.0)
                h, w = reference_image_resized.shape
                corners = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
                current_corners = cv2.perspectiveTransform(corners, H)
                frame_resized = cv2.polylines(frame_resized, [np.int32(current_corners)], True, (0, 0, 255), 2)
                [np.int32(current_corners)[0]][0][0]
                try:
                    x,y = [np.int32(current_corners)[0]][0][0]
                    cv2.putText(frame_resized, "Object found", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1 )
                except:
                    pass

                cv2.imwrite(f"{dir_name}/test_{self._index}.png", frame_resized)

            frame = cv2.resize(frame_resized, (frame.shape[1], frame.shape[0]))

            cv2.imshow('Video', frame_resized)
            self._index += 1 
            # cv2.imwrite('temp.png', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()
