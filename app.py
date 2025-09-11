from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


#Chargement du modèle au démarrage de l'application
model = joblib.load("modele_sentiment.joblib")


class Sentiment(BaseModel):
    review: str


app = FastAPI()

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500/Front-end_TP_sentiment/index.html",
    "https://frontend-sentiment-detection.onrender.com"

    # Ajoutez d'autres origines autorisées si nécessaire
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
def predict_sentiment(review: Sentiment):
    prediction = model.predict([review.review])
    sentiment_mapping = {0: "negative", 1: "positive"}
    predicted_sentiment = sentiment_mapping[prediction[0]]
    return {"prediction": predicted_sentiment}




"""
#première essai:
@app.post("/predict")
def predict_sentiment(input: Sentiment):
    #Conversion des données d'entrée liste pr sklearn
    data = [input.review]

    #Prédiction
    prediction = model.predict(data)[0]
    #return {"predicted_sentiment": int(prediction)}


#Le modèle prédit une classe (0,1), on peut la mapper
    #au nom du sentiment pour une meilleure lisibilité

    sentiments = {0: "négatif", 1: "positif"}
    predicted_sentiment = sentiments[int(prediction)]

    return {"predicted_sentiment": predicted_sentiment}
"""

    
#Lancez l'application FastAPI avec Uvicorn
#uvicorn app:app --reload



"""from fastapi import FastAPI
from pydantic import BaseModel
import joblib

model = joblib.load("pipeline_sentiment.joblib")

class ReviewData(BaseModel):
    text: str

app = FastAPI()

@app.post("/predict")
def predict_sentiment(review: ReviewData):
    prediction = model.predict([review.text])
    sentiment_mapping = {0: "negative", 1: "positive"}
    predicted_sentiment = sentiment_mapping[prediction[0]]
    return {"prediction": predicted_sentiment}
    """