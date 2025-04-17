# Music and Mood Dataset Explainer

## SURVEY_DATA.CSV
This file contains survey responses about music listening habits and emotional states:
- TIME (datetime): When the survey was completed (MM/DD/YYYY HH:MM:SS)
- AGE (integer): Age of participant in years
- GENDER (string): Gender of participant
- HOURS_PER_DAY (string): Daily music listening time ("Less than 1 hour", "1-2 hours", etc.)
- GENRES (string): Preferred music genres (multiple possible like "Pop 🎶", "Rock 🎸", etc.)
- CHANGE_MOOD (string): Whether music changes their mood ("Yes", "No")
- MUSIC_TYPE (string): Preferred music when feeling down (e.g., "Music that matches my mood")
- SONG_NUM (string): Number for the song for each surveyee (e.g., "song_1")
- SONG (string): Full song title with artist
- TITLE_1 (string): Full title of their chosen song
- AUTHOR_1 (string): Artist/performer of the song
- INTERESTED, DISTRESSED, EXCITED, UPSET, ENTHUSIASTIC, NERVOUS, PROUD, AFRAID, INSPIRED, IRRITABLE (integer): Emotional ratings on 1-5 scale
- POSITIVE_MEAN (float): Average of positive emotion ratings (interested, excited, enthusiastic, proud, inspired)
- NEGATIVE_MEAN (float): Average of negative emotion ratings (distressed, upset, nervous, afraid, irritable)

## SONG_FEATURES.CSV
This file contains audio characteristics of each song mentioned in the survey:
- SONG (string): Full song title with artist
- DANCEABILITY (float): How suitable for dancing (0.0-1.0)
- ENERGY (float): Intensity and activity level (0.0-1.0)
- VALENCE (float): Musical positiveness/happiness (0.0-1.0)
- ACOUSTICNESS (float): Confidence measure of acoustic quality (0.0-1.0)
- INSTRUMENTALNESS (float): Prediction of no vocals (0.0-1.0)
- TEMPO (float): Speed in beats per minute (BPM)
- KEY (integer): Musical key (0=C, 1=C#, 2=D, etc.)
- SPEECHINESS (float): Presence of spoken words (0.0-1.0)

This dataset can be used to explore relationships between song audio features, emotional health, music habits, and demographic factors.
