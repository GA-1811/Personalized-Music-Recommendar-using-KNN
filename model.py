import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler

class MusicRecommender:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.scaler = MinMaxScaler()
        self.model = None
        self._prepare_data()
        
    def _prepare_data(self):
        # Select features for recommendation
        self.features = self.data[['danceability', 'energy', 'valence', 'tempo', 'popularity']]
        
        # Normalize features
        self.scaled_features = self.scaler.fit_transform(self.features)
        
        # Train KNN model
        self.model = NearestNeighbors(n_neighbors=5, metric='cosine')
        self.model.fit(self.scaled_features)
    
    def get_recommendations(self, user_preferences):
        # Prepare user input
        user_input = pd.DataFrame([user_preferences])
        scaled_input = self.scaler.transform(user_input)
        
        # Find nearest neighbors
        distances, indices = self.model.kneighbors(scaled_input)
        
        # Get recommended songs
        recommendations = self.data.iloc[indices[0]]
        
        return recommendations[['song_title', 'artist', 'genre', 'danceability', 'energy']]