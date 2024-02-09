# Project-data-engineering-tool 
Projet de Scraping Web avec Scrapy, Flask, et MongoDB 
Description 
Ce projet est une application de scraping web développée en Python, utilisant Scrapy pour le scraping de données, Flask pour la création d'une API web, et MongoDB pour le stockage des données. Le projet est conçu pour être exécuté dans des conteneurs Docker, assurant ainsi une mise en place et un déploiement faciles. 

la page scrapée est la suivante: https://www.francefleurs.com/428-roses  

  Technologies Utilisées:   
Scrapy : Un framework de scraping web en Python pour extraire les données des sites web.   
Flask : Un micro-framework web en Python pour développer l'API web.    
MongoDB : Une base de données NoSQL pour stocker les données scrapées.    
Docker : Pour containeriser l'application et simplifier le déploiement et l'exécution.    
Docker Compose : Pour définir et exécuter des applications Docker multi-conteneurs.   
Installation et Lancement  
Prérequis:  
  -Docker  
  -Docker Compose  
Étapes d'Installation  
Clonez le dépôt Git :  

  
git clone [url_du_dépôt]  

Naviguez dans le dossier du projet :  


cd [nom_du_dossier_du_projet]  

Lancement de l'Application  
Utilisez Docker Compose pour construire et démarrer les services :  


docker-compose up --build

Accès à l'API  
Une fois l'application en cours d'exécution, accédez à l'API via :  
  
http://[adresse_IP]:5000/  
Remplacez [adresse_IP] par l'adresse IP de la machine hôte ou utilisez localhost si vous exécutez l'application localement.

Le scraping fonctionne mais je n'ai pas réussi faire fonctionner l'API flask

Auteurs
Quentin Lebouc
