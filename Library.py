import cv2
import numpy as np
def sift_detector(new_image, image_template):
    # Function that compares input image to template
    # It then returns the number of SIFT matches between them
    image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    image2 = image_template

    # Create SIFT detector object
    #sift = cv2.SIFT()
    sift = cv2.xfeatures2d.SIFT_create()
    # Obtain the keypoints and descriptors using SIFT
    keypoints_1, descriptors_1 = sift.detectAndCompute(image1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(image2, None)

    # Define parameters for our Flann Matcher
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 3)
    search_params = dict(checks = 100)

    # Create the Flann Matcher object
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # Obtain matches using K-Nearest Neighbor Method
    # the result 'matchs' is the number of similar matches found in both images
    matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

    # Store good matches using Lowe's ratio test
    good_matches = []
    for m,n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m) 
    return len(good_matches)
    



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
      
        # img_rgb = cv2.imread('Sources/Screenshot_1.png')
        # img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        # template = cv2.imread('Sources/Screenshot_3.png',0)
        # w, h = template.shape[::-1]

        # res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        # threshold = 0.8
        # loc = np.where( res >= threshold)
        # for pt in zip(*loc[::-1]):
        #     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

        # cv2.imwrite('res.png',img_rgb)

        # img_rgb = cv2.imread('Sources/Screenshot_1.png')
        # img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        video = cv2.VideoCapture(self._video_source)
        template = cv2.imread(self._image_source,0)
        w, h = template.shape[::-1]
        while video.isOpened():
            ret, frame = video.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
            threshold = 0.63
            loc = np.where( res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

            cv2.imshow('res.png',frame)
            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break








# # def show_video():
# #     video = cv2.VideoCapture(source='Sources/forest1080.mp4')
# #     while video.isOpened():
# #         ret, frame = video.read()
# #         cv2.imshow('test', frame)
# #         print(video.get(5))
# #         if cv2.waitKey(1) == ord('q'):
# #             break
