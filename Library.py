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

    def show_video2(self):
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
                cv2.putText(frame, "Object found", (pt[0], pt[1] - 10), cv2.FONT_ITALIC, 2 , (255,255,255),1 )

            # min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result)
            # height, width= template.shape[:2]
            # top_left= max_loc
            # bottom_right= (top_left[0] + width, top_left[1] + height)
            # cv2.rectangle(frame, top_left, bottom_right, (0,0,255),1)

            cv2.imshow('showing', frame)
            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break
        
    def show_video(self):

        # Load the reference image to be detected
        reference_image = cv2.imread(self._image_source, cv2.IMREAD_GRAYSCALE)

        # Create the object detection algorithm
        detector = cv2.SIFT_create()

        # Find keypoints and descriptors for the reference image
        keypoints, descriptors = detector.detectAndCompute(reference_image, None)

        # Load the video file
        video_capture = cv2.VideoCapture(self._video_source)

        # Loop through each frame of the video
        while video_capture.isOpened():
            ret, frame = video_capture.read()

            # Convert the frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Find keypoints and descriptors for the current frame
            current_keypoints, current_descriptors = detector.detectAndCompute(gray_frame, None)

            # Match the keypoints and descriptors for the reference image and the current frame
            matcher = cv2.FlannBasedMatcher({'algorithm': 0, 'trees': 5}, {'checks': 50})
            matches = matcher.knnMatch(descriptors, current_descriptors, k=2)

            # Filter the matches by distance and ratio
            good_matches = []
            for m, n in matches:
                if m.distance < 0.7 * n.distance:
                    good_matches.append(m)

            # If there are enough good matches, draw a rectangle around the detected object
            if len(good_matches) > 10:
                reference_points = [keypoints[m.queryIdx].pt for m in good_matches]
                current_points = [current_keypoints[m.trainIdx].pt for m in good_matches]
                H, mask = cv2.findHomography(np.float32(reference_points), np.float32(current_points), cv2.RANSAC, 5.0)
                h, w = reference_image.shape
                corners = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
                current_corners = cv2.perspectiveTransform(corners, H)
                frame = cv2.polylines(frame, [np.int32(current_corners)], True, (0, 0, 255), 2)
                [np.int32(current_corners)[0]][0][0]
                try:
                    x,y = [np.int32(current_corners)[0]][0][0]
                    cv2.putText(frame, "Object found", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1 )
                except:
                    pass

            # Display the current frame
            cv2.imshow('Video', frame)

            # Exit the loop if the user presses the 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the video capture and destroy all windows
        video_capture.release()
        cv2.destroyAllWindows()

