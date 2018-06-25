# music_classification
## Summary

Used Music Information Retrieval (MIR) techniques to extract features from Nickelback and Pitbull mp3 files, and classified their songs using machine learning!

Full write-up can be found here: [Write-Up](https://www.linkedin.com/pulse/shazam-song-nickelback-pitbull-owen-carey-1/)

## Music and Deep Learning

Imagine this. In a few years, musicians will be able to create music with the help of Artificial Intelligence (AI). In a few *more* years, everyone will be able to create music with the help of AI. The moment it is possible to train a deep learning algorithm on your entire Spotify history in raw audio form, and generate new songs, everyone will be a musician.

We will soon be in a new era of music, reminiscent of the electronic dance music (EDM) disruption of the 1980s. Just as computers began to help artists create music then, AI will help artists create music soon enough too.

Wouldn’t that be so freaking COOL??!

We’re not there yet, but there is [*TONS*](http://www.asimovinstitute.org/analyzing-deep-learning-tools-music/) of on-going research on the applications of deep learning with music. This article focuses on but one of those applications — automated music classification.

 ## Motivation

In the last twenty years the presence of digital music has become ubiquitous. The growth of the internet, music sharing sites, MP3 compression, and enhanced storage capacities has allowed for millions of people to create private music collections all over the world. Since these collections often exceed thousands of songs, the need for content classification, navigation, and recommendations is becoming increasingly important. Most music recommender systems utilize one of two approaches: content based or collaborative based recommendations (or a hybrid of the two). **Content based recommenders** use song features such as *gender of lead vocalist, prevalent use of groove, level of distortion on the electric guitar, and type of background vocals* to provide recommendations of similar music you might like. This is the backbone of Pandora’s [Music Genome Project](https://www.pandora.com/about/mgp), which uses 450 features of each song to make recommendations. The downside of this approach is that *EVERY* song needs to be hand labeled by trained musicologists, which is very costly. **Collaborative based recommenders** make predictions of what might interest a person based on the taste of many other users. It assumes that if person X likes The Beatles, and person Y likes The Beatles and The Rolling Stones, then person X might like The Rolling Stones as well. The downside of this approach is that popular songs are more frequently recommended, rather than obscure songs that you might love!

What if there was a way to take raw audio files, extract information from them, and make more complex recommendations using machine learning? To me, that would be so *COOL*!

There is a lot of machinery that goes behind automated music classification, navigation, and recommendation based on raw audio. So I decided to bite off a small chunk to start…

**As my first dive into processing raw audio, I decided to see if I could build a machine learning model that could distinguish between Nickelback and Pitbull songs!** *… P.S. I chose these artists because they are almost universally hated hehe.*

## Repo Structure

- `mp3_split.py` : This module splits the .mp3 audio files into two second .wav audio files.
- `feature_extraction.py` : This module extracts Music Information Retrieval (MIR) features from .wav files.
- `dataframe_creation.py` : This module runs the feature extraction script on all the .wav files, puts them in a pandas dataframe, and pickles them.
- `visualizations.ipynb` : This notebook includes visualizations of the data.
- `modeling.ipynb` : This notebook contains all of the machine learning and deep learning modeling.