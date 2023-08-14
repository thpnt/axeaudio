def record_audio(status_label, root) :
    import pyaudio
    import wave
    import time
    import os
    import threading
    from config import CHANNELS, CHUNK, FORMAT, RATE, RECORD_SECONDS_MAX, DATA_DIRECTORY

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    status_label.config(text = f"Recording will start in 3 seconds... (Press 's' to stop or maximum duration is {RECORD_SECONDS_MAX} seconds)")
    root.update()
    time.sleep(3)
    status_label.config(text = f"Recording... (Press 'Ctrl + C' to stop or maximum duration is {RECORD_SECONDS_MAX} seconds)")
    root.update()
    
    frames = []
    recording_stopped = threading.Event()

    def stop_recording():
        recording_stopped.set()

    # Start a timer to stop recording after RECORD_SECONDS_MAX seconds
    timer = threading.Timer(RECORD_SECONDS_MAX, stop_recording)
    timer.start()

    try:
        while not recording_stopped.is_set():
            data = stream.read(CHUNK, exception_on_overflow = False)
            frames.append(data)
    except KeyboardInterrupt:
        status_label.config(text="Finished recording due to keyboard interrupt.")
        root.update()
    else:
        status_label.config(text = "Finished recording due to time limit.")
        root.update()

    stream.stop_stream()
    stream.close()
    p.terminate()
    
    status_label.config(text = 'Storing audio file....')
    root.update()
    
    dir = os.makedirs(DATA_DIRECTORY, exist_ok=True)
    file_name = "test" + str(len(os.listdir(DATA_DIRECTORY))-1) + ".wav"
    WAVE_OUTPUT_FILENAME = f"{DATA_DIRECTORY}/{file_name}"
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        
    status_label.config(text = "File stored as {WAVE_OUTPUT_FILENAME}. \n You can now transcript your audio file.")
    return