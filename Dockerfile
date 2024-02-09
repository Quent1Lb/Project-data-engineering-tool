# Utiliser une image de base Python officielle
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY . /app

# Exposer le port sur lequel l'application Flask s'exécute
EXPOSE 5000
EXPOSE 8888

# Installer les dépendances

RUN pip install --upgrade pip && pip install pipenv && pipenv install --skip-lock
RUN pip install -r requirements.txt
RUN pipenv install notebook

# Exécuter main.py (le spider Scrapy) lors du démarrage du conteneur

CMD [ "python", "main.py", "run", "jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--NotebookApp.token=''"]