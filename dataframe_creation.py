"""
This module actually extracts the audio features from each of the .wav files.
"""

# Imports 
from feature_extraction import features
from os import listdir
import pandas as pd
import pickle

# Creating list of all Nickelback mp3 paths in my folder
nb_path = '/home/owen/Music/Nickelback_Segments'
nb_mp3 = ['/home/owen/Music/Nickelback_Segments/' + str(f) for f in listdir(nb_path)]

# Creating list of all Nickelback mp3 paths in my folder
pb_path = '/home/owen/Music/Pitbull_Segments'
pb_mp3 = ['/home/owen/Music/Pitbull_Segments/' + str(f) for f in listdir(pb_path)]

# Creating a dataframe to record all summary data
df = pd.DataFrame(columns = ['Artist',
                             'Cent Mean',
                             'Cent Std',
                             'RMSE Mean',
                             'RMSE Std',
                             'Rolloff Mean',
                             'Rolloff Std',
                             'Tempo',
                             'ZCR Mean',
                             'ZCR Std'])

# Extract features from each of the Nickleback audio files
for mp3 in nb_mp3:
    feature_dict = features(mp3)
    if 'Nickelback' in mp3:
        feature_dict['Artist'] = 'Nickelback'
    else:
        feature_dict['Artist'] = 'Pitbull'
    feature_df = pd.DataFrame(feature_dict, index = [0])
    df = pd.concat([df, feature_df])

# Extract features from each of the Pitbull audio files
for mp3 in pb_mp3:
    feature_dict = features(mp3)
    if 'Nickelback' in mp3:
        feature_dict['Artist'] = 'Nickelback'
    else:
        feature_dict['Artist'] = 'Pitbull'
    feature_df = pd.DataFrame(feature_dict, index = [0])
    df = pd.concat([df, feature_df]) 

# Pickle dump the dataframe
pickle.dump(df, open('data/df_music.pkl', 'wb'))