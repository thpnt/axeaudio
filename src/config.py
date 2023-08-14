#Audio recording params
import pyaudio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS_MAX = 20


#File storage params
DATA_DIRECTORY = "data/raw"
TRANSCRIPT_DIRECTORY = "data/raw_transcripts"
EDITED_DIRECTORY = "data/edited_transcripts"