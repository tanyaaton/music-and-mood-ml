```markdown
# Music and Mood Dataset

This repository contains two related datasets:

1. `SURVEY_DATA.CSV` - Survey responses about music listening habits and emotional states
2. `SONG_FEATURES.CSV` - Audio features of songs mentioned in the survey

## Survey Data

The `SURVEY_DATA.CSV` file contains self-reported data from participants regarding their music listening habits and emotional responses. Each row represents one participant.

### Columns

| Column | Description | Data Type | Values |
|--------|-------------|-----------|--------|
| **timestamp** | When the survey was completed | Datetime | MM/DD/YYYY HH:MM:SS |
| **age** | Age of participant | Integer | Years |
| **gender** | Gender of participant | Categorical | "Male", "Female", etc. |
| **hours_per_day** | Daily music listening time | Categorical | "Less than 1 hour", "1-2 hours", "3-4 hours", "More than 5 hours" |
| **genres** | Preferred music genres | Categorical (multiple) | "Pop 🎶", "Rock 🎸", "Classical 🎻", "Jazz 🎷", "Hip-Hop/Rap 🎤", "Electronic/Dance 🧑‍🎤", "Others" |
| **change_mood** | Whether music changes their mood | Boolean | "Yes", "No" |
| **music_type** | Preferred music when feeling down | Categorical | "Music that matches my mood", "Music that contrasts with my mood", "I don't listen to music when feeling down", "Both" |
| **song_num** | Identifier for the song | String | "song_1" |
| **songtitle_1** | Full title of their chosen song | String | Full song title |
| **author_1** | Artist/performer of the song | String | Artist name |
| **interested** | Rating of how interested they felt | Integer | 1-5 scale |
| **distressed** | Rating of how distressed they felt | Integer | 1-5 scale |
| **excited** | Rating of how excited they felt | Integer | 1-5 scale |
| **upset** | Rating of how upset they felt | Integer | 1-5 scale |
| **enthusiastic** | Rating of how enthusiastic they felt | Integer | 1-5 scale |
| **nervous** | Rating of how nervous they felt | Integer | 1-5 scale |
| **proud** | Rating of how proud they felt | Integer | 1-5 scale |
| **afraid** | Rating of how afraid they felt | Integer | 1-5 scale |
| **inspired** | Rating of how inspired they felt | Integer | 1-5 scale |
| **irritable** | Rating of how irritable they felt | Integer | 1-5 scale |
| **positive_mean** | Average of positive emotion ratings | Float | 1-5 scale average |
| **negative_mean** | Average of negative emotion ratings | Float | 1-5 scale average |

## Song Features

The `SONG_FEATURES.CSV` file contains audio characteristics of each song mentioned in the survey data, based on computational analysis of the audio.

### Columns

| Column | Description | Data Type | Range |
|--------|-------------|-----------|-------|
| **Song** | Full song title with artist | String | Text |
| **Danceability** | How suitable the track is for dancing | Float | 0.0 to 1.0 |
| **Energy** | Perceptual measure of intensity and activity | Float | 0.0 to 1.0 |
| **Valence** | Musical positiveness (happiness, cheerfulness) | Float | 0.0 to 1.0 |
| **Acousticness** | Confidence measure of whether track is acoustic | Float | 0.0 to 1.0 |
| **Instrumentalness** | Predicts whether track contains no vocals | Float | 0.0 to 1.0 |
| **Tempo** | Overall estimated tempo in beats per minute (BPM) | Float | Typically 50-200 |
| **Key** | Overall key of the track | Integer | 0-11 (0=C, 1=C#, 2=D, etc.) |
| **Speechiness** | Presence of spoken words | Float | 0.0 to 1.0 |

## Feature Explanations

### Audio Features

- **Danceability**: Combines tempo, rhythm stability, beat strength, and regularity. Higher values are more danceable.
- **Energy**: Represents intensity and activity. Energetic tracks feel fast, loud, and noisy.
- **Valence**: Describes musical positiveness. High valence tracks sound happy/positive, low valence tracks sound sad/negative.
- **Acousticness**: Confidence measure of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
- **Instrumentalness**: Predicts vocals. Values closer to 1.0 indicate greater likelihood of no vocal content.
- **Tempo**: The speed of the track in beats per minute.
- **Key**: The key of the track, using standard pitch class notation (0 = C, 1 = C#/Db, etc.)
- **Speechiness**: Detects spoken words. Values above 0.66 likely represent speech, values below 0.33 represent music.

### Emotion Measures

- **Positive emotions**: interested, excited, enthusiastic, proud, inspired
- **Negative emotions**: distressed, upset, nervous, afraid, irritable
- **positive_mean**: Average of all positive emotion ratings
- **negative_mean**: Average of all negative emotion ratings

## Usage

This dataset can be used to explore relationships between:

1. Song audio features and emotional responses
2. Music listening habits and emotional states
3. Demographic factors and music preferences
4. Audio properties and genre classifications

## Data Collection

The survey data was collected through self-reported questionnaires. Song features were computationally extracted using audio analysis algorithms similar to those used by music streaming services.
```
