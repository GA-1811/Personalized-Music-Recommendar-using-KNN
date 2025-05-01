from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from model import MusicRecommender

app = Flask(__name__)

# Initialize recommender system
recommender = MusicRecommender('data/music_data.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == 'POST':
        # Get user preferences from form
        user_data = {
            'danceability': float(request.form['danceability']),
            'energy': float(request.form['energy']),
            'valence': float(request.form['valence']),
            'tempo': float(request.form['tempo']),
            'popularity': float(request.form['popularity'])
        }
        
        # Get recommendations
        recommendations = recommender.get_recommendations(user_data)
        
        return render_template('recommendations.html', 
                             recommendations=recommendations.to_dict('records'))

if __name__ == '__main__':
    app.run(debug=True)