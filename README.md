# Video detection
Python software for video object detection using OpenCV
## Description 
This program is designed to search for a given object in the video.  A photo image is used as the object for the search. The video source can be either a video from the user's computer or a video from a webcam. 
Supported video formats: AVI, MP4, MOV, MKV 
Supported image formats: png, jpg

The program has a convenient graphical interface for convenient operation.

After selecting a video file from your computer, the user will be able to view, stop or restart it in the preview window.

---

### The design of the application looks like this
<p align="center">
  <img  src="https://github.com/Egor-S-N/VideoSearching/assets/63055406/ecac5ec9-f833-4ab4-a58f-c36ec6e840b6">
</p>

---

Processing takes place in real time, the results are shown to the user on the screen, and are also saved to the results folder with the date and time of the start of the algorithm.
## How to use

1. Install or clone this project 
2. Install the [missing libraries](/requirements.txt) through command:  `pip3 install -r requirements.txt`
3. run program from folder: 'VideoSearching' with command: `python main.py`
4. select video source (from files / from camera) and also select object description (image / text)
5. click on the button "Execute"

After pressing the button, the result of the work will be shown to the user in real time, and images with the found object will be saved in the results folder





## 📝 License
Copyright © 2023 [Nifakin Egor](https://github.com/Egor-S-N).<br>This project is [MIT](https://github.com/Egor-S-N/VideoSearching/blob/main/LICENSE) licensed.


