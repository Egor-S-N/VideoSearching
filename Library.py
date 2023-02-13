import cv2
import numpy as np

class Library:
    def __init__(self):
        self._video_source = ""
        self._image_source = ""

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
        video = cv2.VideoCapture(self._video_source)
        template= cv2.imread(self._image_source,0)
        while video.isOpened():
            ret, frame = video.read()
            gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            result= cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(result >= 0.8)
            height, width= template.shape[:2]
            for pt in zip(*loc[::-1]):
                cv2.rectangle(frame, pt, (pt[0] + width, pt[1] + height), (0, 0, 255), 1)
            # min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result)
            # height, width= template.shape[:2]
            # top_left= max_loc
            # bottom_right= (top_left[0] + width, top_left[1] + height)
            # cv2.rectangle(frame, top_left, bottom_right, (0,0,255),1)

            cv2.imshow('showing', frame)
            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break
