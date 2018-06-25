"""
This module extracts features from .wav audio files using Librosa.
"""

# Imports
import librosa
import numpy as np

# Create function to extract features from .wav file
def features(wav):
    """
    Function to extract audio features from .wav files using the Librosa
    library.
    
    Args:
        wav (str): .wav file location.
    
    Returns:
        features (dict): Music features extracted from the .wav audio files.
    """
    
    # Load the audio waveform
    duration = 10
    y, sr = librosa.load(wav, duration = duration)
    
    # Calculate the spectrogram S of the waveform for future calculations
    S, phase = librosa.magphase(librosa.stft(y))
    
    # Separate harmonic and percussive into two waveforms
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    
    # Calculate tempo
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)
    
    # Calculate RMS Energy summary statistics
    rmse = librosa.feature.rmse(S=S)
    rmse_mean = np.mean(rmse)
    rmse_std = np.std(rmse)
    
    # Calculate Zero Crossing Rate (ZCR) summary statistics
    zcr = librosa.feature.zero_crossing_rate(y)
    zcr_mean = np.mean(zcr)
    zcr_std = np.std(zcr)
    
    # Spectral Centroid summary statistics
    cent = librosa.feature.spectral_centroid(S=S)
    cent_mean = np.mean(cent)
    cent_std = np.std(cent)
    
    # Spectral Rolloff
    rolloff = librosa.feature.spectral_rolloff(S=S, sr=sr)
    rolloff_mean = np.mean(rolloff)
    rolloff_std = np.mean(rolloff)
    
    # Create empy dictionary to story information
    features = {'Tempo': tempo,
                'RMSE Mean' : rmse_mean,
                'RMSE Std' : rmse_std,
                'ZCR Mean' : zcr_mean,
                'ZCR Std' : zcr_std,
                'Cent Mean' : cent_mean,
                'Cent Std' : cent_std,
                'Rolloff Mean': rolloff_mean,
                'Rolloff Std' : rolloff_std
                }
    
    return features