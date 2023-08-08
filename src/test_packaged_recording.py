import pyaudio
import wave
import os
import threading
from config import CHANNELS, CHUNK, FORMAT, RATE, RECORD_SECONDS_MAX, DIRECTORY

class AudioRecorder:

    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.frames = []
        self.recording_stopped = threading.Event()
        self.stream = None

    def start_recording(self):
        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  input=True,
                                  frames_per_buffer=CHUNK)
        print(f"Recording will start in 3 seconds... (Press 'Ctrl + C ' to stop or maximum duration is {RECORD_SECONDS_MAX} seconds)")

        # Start a timer to stop recording after RECORD_SECONDS seconds
        timer = threading.Timer(RECORD_SECONDS_MAX, self.stop_recording)
        timer.start()

        try:
            while not self.recording_stopped.is_set():
                data = self.stream.read(CHUNK, exception_on_overflow=False)
                self.frames.append(data)
        except KeyboardInterrupt:
            print("Finished recording due to keyboard interrupt.")
        else:
            print("Finished recording due to time limit.")

    def stop_recording(self):
        self.recording_stopped.set()
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()

    def store_file(self, directory=DIRECTORY):
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        nb_files = str(len([f for f in os.listdir(directory) if f.endswith('.wav')]))
        WAVE_OUTPUT_FILENAME = os.path.join(directory, f"test{nb_files}.wav")

        with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(self.frames))
        print(f"File saved as {WAVE_OUTPUT_FILENAME}")

if __name__ == "__main__":
    recorder = AudioRecorder()
    recorder.start_recording()
    recorder.store_file()
