#Import relevant packages
import os
import wave
import pyaudio
import threading
from pynput import keyboard

#Set is_recording as a global variable
is_recording = True


#Define the function to stop recording when key is pressed
def on_press(key):
    global is_recording
    try:
        if key.char=='s':
            is_recording==False
    except AttributeError:
        pass
    
#Recording :
#First we instantiate the audio recorder with pyaudio

def record_audio(CAB=0,file_name='test',MAX_SECONDS=60,FORMAT=pyaudio.paInt16, CHUNK=4096, CHANNELS=1, RATE=44100) :
    #Instantiate audio recorder
    audio = pyaudio.PyAudio()

    import time

    #set params
    stream = audio.open(format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK)
    
    print(f"Recording will start in 3 seconds... (Press 's' to stop or maximum duration is {MAX_SECONDS} seconds)")
    time.sleep(3)
    print(f"Recording... (Press 's' to stop or maximum duration is {MAX_SECONDS} seconds)")

    frames = []

    
    # Keep recording in chunks until is_recording becomes False
    for _ in range(0, int(RATE / CHUNK * MAX_SECONDS)):
        try:
            data = stream.read(CHUNK)
            frames.append(data)
        except IOError:
            print("Skipped frame due to overflow")

        if not is_recording:
            print("Stopped recording")
            break

        
    #Save the recorded data to a WAV file
    OUTPUT_FILENAME = f"data/raw/{CAB}/{file_name}.wav"
    
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        

# Start listening to keyboard in a separate thread
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Start recording
record_audio()

listener.join()