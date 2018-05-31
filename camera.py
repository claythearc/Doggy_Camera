# camera.py

import cv2
from audio import AudioRecorder


class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        self.audio = AudioRecorder()
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        barks = self.audio.getbarks()
        cv2.putText(image, "Barks: " + str(barks), (50,  450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255),2,cv2.LINE_AA)
        ret, jpeg = cv2.imencode('.jpg', image)
        self.audio.readaudio()
        return jpeg.tobytes()
