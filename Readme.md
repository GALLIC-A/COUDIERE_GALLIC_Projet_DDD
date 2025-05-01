# Prérequis pour faire fonctionner le projet
## Back-end :
- Avoir Python 3 installé sur sa machine
- Avoir installé les dépendances de requirements.txt
- Avoir effectué les migrations `migrate` dans l'ordre suivant :
  1. `users`
  2. `api`
  3. Puis la migration par défaut de Django (`python manage.py migrate`)
- Avoir exécuté le script Python `alimenter_la_base_de_donnees.py`,.
Ce script permet d'alimenter la base de données SQLite (db.sqlite3) avec les données nécessaires ainsi que les rôles par défaut que peuvent avoir les utilisateurs.

## Front-end :
- Avoir NodeJS installé sur sa machine
- Avoir installé les dépendances 
- Pour lancer le serveur dev, il faut se placer dans Front/app
- Exécuter la commande `npm run serve`

# Application DDD

## Phase 1 : Étude

### Définition des besoins

- **Équipe de direction**  
  - Accès direction  
  - Dashboard direction  

- **Équipe marketing**  
  - Accès marketing  
  - Dashboard marketing  

- **Équipe éditoriale**  
  - Accès édition  
  - Dashboard édition  

- **Client**  
  - Accès client  
  - Dashboard client  

---

### Définition du langage ubiquitaire

#### Bounded Contexts

1. **Analyse Musicale & Recommandation**
2. **Démographie & Tendances**
3. **Interface et Reporting**

---

#### Entités et leurs associations

##### Analyse Musicale & Recommandation

- **Musique**
  - `id`
  - `titre`
  - `artiste`
  - `genre`
  - `dancabilité`
  - `énergie`
  - `bpm`
  - `date_sortie`

- **Analyse**
  - `id`
  - `musique_id` (relation avec Musique)
  - `composantes` (PCA)
  - `variance_expliquée`
  - `corrélations`
  - `clusters` (segmentation)
  - `valeur_de_coude` (pour déterminer le nombre de clusters)
  - `paramètres` (paramètres de modèle)

- **Recommandation**
  - `id`
  - `profil_utilisateur_id`
  - `musique_id`
  - `score`
  - `date_recommandation`

---

##### Démographie & Tendances

- **Utilisateur**
  - `id`
  - `âge`
  - `profession`
  - `localité`
  - `historique_écoutes`

- **Tendance**
  - `id`
  - `période`
  - `genre_populaire`
  - `localité`
  - `statistiques_utilisateur`

---

##### Interface et Reporting

- **Rôle**
  - `id`
  - `nom` (Directeur, Marketing, Éditeur, Client)

- **Utilisateur Plateforme**
  - `id`
  - `nom`
  - `email`
  - `rôle_id`

- **Dashboard**
  - **Direction**
    - Synthèse marketing
    - Historique des actions marketing
    - Historique éditorial
  - **Marketing**
    - Visualisations de données (écoutes, clics, taux de conversion)
    - Gestion des campagnes marketing
  - **Édition**
    - Gestion des recommandations manuelles
    - Tagging des morceaux
  - **Client**
    - Affichage des recommandations
    - Navigation musicale
    - Historique d’écoutes

---

### Domain Events

- `MusiqueÉcoutée` (déclenche mise à jour des tendances et scoring de recommandation)
- `RecommandationGénérée` (événement asynchrone pour log et notification)
- `ProfilMisÀJour` (rafraîchissement des clusters)
- `CampagneMarketingLancée`
- `TagAjoutéÀMusique`

---

### Services Domaines

- **Service de Recommandation**
  - Génération automatique à partir de l’analyse
  - Apprentissage basé sur feedback utilisateur

- **Service d’Analyse**
  - PCA, clustering, statistiques musicales

- **Service Tendances**
  - Agrégation des données démographiques + écoutes
  - Détection des tendances locales

- **Service Reporting**
  - Export des indicateurs clés pour les dashboards

---

### Repositories

- `MusiqueRepository`
- `UtilisateurRepository`
- `RecommandationRepository`
- `AnalyseRepository`
- `TendanceRepository`

---

### Cas d’Utilisation (exemples)

- En tant que **client**, je veux recevoir des recommandations basées sur mes écoutes et sur les tendances locales.
- En tant que **marketeur**, je veux analyser l'impact d’une campagne marketing sur les écoutes par genre.
- En tant que **éditeur**, je veux ajuster manuellement les recommandations.
- En tant que **directeur**, je veux accéder à une synthèse hebdomadaire des performances éditoriales et marketing.



##### Définition des objets de valeur
##### Définition des objets métiers
##### Définition des agrégats
##### Définition des services métiers

### Mapping des bounded context

### Conception de l'architecture
#### Stack
- Django + Vue.js
#### Stockage
- Base de donnée MySQL
#### API REST
#### compatibilité microservices


## Phase 2 Intégration Data Centric :

### Création pipeline ETL

## Phase 3 Sécurité et test :

### Sécurité 

### Tests