import pandas as pd

# Load the processed data
df = pd.read_csv('data_processed.csv')

# Calculate mental score based on positive and negative means
df["mental_score"] = (df["positive_mean"] - df["negative_mean"]) * 5

# Define genre columns for analysis
genres_columns = ['pop', 'rock', 'hip-hop/rap', 'country', 'classical', 'jazz', 'folk', 'metal', 'electronic/dance', 'others']

def check_genre(genres_str, genre):
    """
    Check if a specific genre appears in the genres string.
    
    Args:
        genres_str (str): String containing all genres
        genre (str): Specific genre to check for
        
    Returns:
        int: 1 if genre is found, 0 otherwise
    """
    genres_str = genres_str.lower()
    genre = genre.lower()
    
    # Handle special cases for genre matching
    if genre == 'hip-hop/rap':
        return 1 if 'hip-hop' in genres_str or 'hip hop' in genres_str or 'rap' in genres_str else 0
    elif genre == 'electronic/dance':
        return 1 if 'electronic' in genres_str or 'dance' in genres_str else 0
    else:
        return 1 if genre in genres_str else 0

# Create binary columns for each genre
for genre in genres_columns:
    df[genre] = df['genres'].apply(lambda x: check_genre(x, genre))

# Load and merge songs data
songs = pd.read_csv('songs.csv')
df = pd.concat([df, songs], axis=1)

# Remove unnecessary columns
columns_to_drop = [
    'Unnamed: 0', 'time', 'genres', 'song', 'song_num', 'title_1', 'author_1',
    'interested', 'distressed', 'excited', 'upset', 'enthusiastic', 'nervous',
    'proud', 'afraid', 'inspired', 'irritable', 'positive_mean', 'negative_mean'
]
df.drop(columns=columns_to_drop, inplace=True)

# Convert categorical variables to numerical
# Gender: Male=0, Female=1
df['gender'] = df['gender'].map({'Male': 0, 'Female': 1})

# Change mood: Yes=1, No=0
df['change_mood'] = df['change_mood'].map({'Yes': 1, 'No': 0})

# One-hot encode hours_per_day
hours_dummies = pd.get_dummies(df['hours_per_day'], dtype=int)
df = pd.concat([df, hours_dummies], axis=1)
df.drop(columns=['hours_per_day'], inplace=True)

# One-hot encode music_type
music_type_mapping = {
    'Music that matches my mood': 'matches_mood',
    "I don't listen to music when feeling down": 'no_music_when_down',
    'Music that contrasts with my mood': 'contrasts_mood',
    'Both': 'both'
}

# Create binary columns for each music type
for value, column_name in music_type_mapping.items():
    df[f'music_type_{column_name}'] = (df['music_type'] == value).astype(int)

# Drop the original music_type column
df.drop(columns=['music_type'], inplace=True)

# Display final dataframe statistics
print("\nFinal DataFrame Statistics:")
print(df.describe())

# Save the processed data to a CSV file
df.to_csv('final_processed_data.csv', index=False)
