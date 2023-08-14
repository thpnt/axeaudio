from recording import record_audio
from transcription import process_audio
import threading
import tkinter as tk
from tkinter import simpledialog
from config import RECORD_SECONDS_MAX

event = threading.Event()

def gui_record_audio():
    def stop_recording():
        event.set()

    event.clear()
    # Start a timer to stop recording after RECORD_SECONDS_MAX seconds
    timer = threading.Timer(RECORD_SECONDS_MAX, stop_recording)
    timer.start()
    record_audio(status_label, root, event)
    
def gui_stop_record():
    event.set()

def gui_process_audio():
    process_audio(status_label, root)

def quit_app():
    root.destroy()  # Close the GUI window

# Create the main GUI window
root = tk.Tk()
root.title("Audio Processing GUI")

# Set the width and height of the GUI window
window_size = 500
root.geometry(f"{window_size}x{window_size}")

# Customize background color
root.configure(bg="light grey")

# Create the RECORD button
record_button = tk.Button(root, text="RECORD", command=gui_record_audio, bg="light blue", fg="black", bd=2, highlightbackground="light grey")
record_button.pack(pady=20)

# Create the STOP RECORD button
record_button = tk.Button(root, text="STOP RECORD", command=gui_stop_record, bg="light blue", fg="black", bd=2, highlightbackground="light grey")
record_button.pack(pady=20)

# Create the PROCESS button
process_button = tk.Button(root, text="TRANSCRIPT", command=gui_process_audio, bg="light blue", fg="black", bd=2, highlightbackground="light grey")
process_button.pack(pady=20)

# Create the QUIT button
quit_button = tk.Button(root, text="QUIT", command=quit_app, bg="light blue", fg="black", bd=2, highlightbackground="light grey")
quit_button.pack(pady=20)

# Create a label to display status messages
status_label = tk.Label(root, text="", fg="black", bg="light grey")
status_label.pack(pady=10)

# Start the tkinter main loop
root.mainloop()

