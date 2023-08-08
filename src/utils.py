#Utils

#File storage
def store_raw_transcript(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

def store_processed_transcript(content, filename):
    with open(filename, 'w') as file:
        file.write(content)