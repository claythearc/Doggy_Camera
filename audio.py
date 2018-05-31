import pyaudio
import audioop
import time

class AudioRecorder():

    def __init__(self):
        self._chunk = 1024
        self._FORMAT = pyaudio.paInt16
        self._CHANNELS = 2
        self._RATE = 44100
        self.audio = pyaudio.PyAudio()
        self.RECORD_SECONDS = 0.5
        self.barks = 0
        self.lastbark = time.time()

    def readaudio(self):
        stream = self.audio.open(format=self._FORMAT, channels=self._CHANNELS,
                                 rate=self._RATE, input=True,
                                 frames_per_buffer=self._chunk)
        frames = []
        for i in range(0, int(self._RATE / self._chunk * self.RECORD_SECONDS)):
            data = stream.read(self._chunk)
            frames.append(data)
            rms = audioop.rms(data, 2)
            if rms > 200:
                if (self.lastbark + 5) < time.time():
                    self.barks += 1
                    self.lastbark = time.time()


    def closeaudio(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def getbarks(self):
        return self.barks


