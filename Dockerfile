
#Image de base Python slim
FROM python:3.12-slim

#Définir répertoire de travail à l'intérieur du conteneur
WORKDIR /app

#Copier le fichiers de dépendances
COPY requirements.txt ./

#Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

#Copier le code de l'application et le modèle dans le conteneur
COPY app.py ./
COPY modele_sentiment.joblib ./

#Expose le port par défaut de FastAPI
EXPOSE 8000

#Commande pour démarrer l'application avec Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

