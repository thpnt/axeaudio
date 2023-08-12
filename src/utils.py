#Utils

#File storage

        
def get_most_recent_file(directory) :
    import os
    #list files in directory
    files = os.listdir(directory)
    
    #If the directory is empty, raise error
    if not files:
        raise NameError('The directory provided is empty. Check src/config.py')
        return None

    #Raise an error if there are no audio_files in the directory
    audio_ext = ['.m4a', '.wav', '.mp3']
    files_ext = [f[-4:] for f in files]
    if not any(x in files_ext for x in audio_ext):
        raise  NameError('There is no audio files in the directory provided. Check src/config.py')
        return None

    #join the path to the files list
    path_files = [os.path.join(directory, f) for f in files]

    #Join a list of the date of modification of the file
    files_times = [[f, os.path.getmtime(f)] for f in path_files]
    #sort the list by time of modification
    files_times.sort(key=lambda x:x[1], reverse = True)

    return files_times[0][0]
        
        
def store_raw_transcript(content, directory):
    import os.path

    #Get file_name based on the the audio file that was transcripted
    file_name = get_most_recent_file('data/raw')[:-4][-5:] + '.txt'
    full_path = os.path.join(directory, file_name)

    #Open the file and write the content in it
    file = open(full_path, 'w')
    file.write(content)
    file.close()
