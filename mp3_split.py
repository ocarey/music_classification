"""
This module splits the .mp3 audio files into two-second .wav files.
"""

# Imports
from os import listdir
from pydub import AudioSegment


def nickelback_splitter(mp3):
    """
    Function that reads in a mp3 and splits it into 2 second chunks.
    
    Args:
        mp3 (str): File location
    
    Returns:
        None.
    """
    
    # Create a mp3 file name
    name = mp3.split()[-1].split('.')[0]
    print(name)
    
    # Open the mp3 using pydub's AudioSegment class
    mp3 = AudioSegment.from_file(mp3)
    
    # Split sound in 2-second slices and export
    for i, chunk in enumerate(mp3[::2000]):
        with open("/home/owen/Music/Nickelback_Segments/%s-%s.wav" % (name, i), "wb") as f:
            chunk.export(f, format="wav")
    
    return


def pitbull_splitter(mp3):
    """
    Function that reads in a mp3 and splits it into 2 second chunks.
    
    Args:
        mp3 (str): File location
    
    Returns:
        None.
    """
    
    # Create a mp3 file name
    name = mp3.split()[-1].split('.')[0]
    print(name)
    
    # Open the mp3 using pydub's AudioSegment class
    mp3 = AudioSegment.from_file(mp3)
    
    # Split sound in 2-second slices and export
    for i, chunk in enumerate(mp3[::2000]):
        with open("/home/owen/Music/Pitbull_Segments/%s-%s.wav" % (name, i), "wb") as f:
            chunk.export(f, format="wav")
    
    return


# Creating list of all Nickelback mp3s paths in my folder
nb_path = '/home/owen/Music/Nickelback'
nb_mp3 = ['/home/owen/Music/Nickelback/' + str(f) for f in listdir(nb_path)]

# Creating list of all Pitbull mp3s paths in my folder
pb_path = '/home/owen/Music/Pitbull'
pb_mp3 = ['/home/owen/Music/Pitbull/' + str(f) for f in listdir(pb_path)]

# Split the full length Nickelback .mp3 files into two second .wav files
for mp3 in nb_mp3:
    nickelback_splitter(mp3)

# Split the full length Pitbull .mp3 files into two second .wav files
for mp3 in pb_mp3:
    pitbull_splitter(mp3)