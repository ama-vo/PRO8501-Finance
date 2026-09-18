# Consignes : 

- Il recense tout l'historique du projet :

**Questions, réponses, décisions, développement, bugs/erreurs, rendus, images.**
- Permet de vérifier la tenue du planning.
- Permet à tout le groupe de savoir ou en sont les autres.
- **Sera noté dans le cadre du module.**


- Le cahier de labo est écrit au jour le jour, et son contenu n'est pas modifié.
- Chaque membre du groupe écrit pour soi même **ses observations**.
- La rédaction n'est pas parfaite, mais elle vous permet de remonter le temps et 
de revenir en arrière.
- S'ajoute à git mais ne le remplace pas.
- Permet de garder une trace de "qui a fait quoi".

# Cahier de labo

> ## Jeudi 3 Sept. - Dimanche 6 Sept. :

## [Groupe]

- Communication en classe : Réflexion sur le choix du projet que nous voulions 
réaliser. 
    _Quels sont les domaines qui nous plaisent ? Qu'est-ce qui nous permettra
    d'aimer ce que l'on va faire ?_
- Domaine trouvé : Le choix s'est porté sur le domaine de la **finance des marchés**.
    _Que faire ? Quels sont les contraintes ? Comment les satisfaire et avec
    quels outils ?_
- Création du projet sur GitHub.
- Création d'un discord avec plusieurs salons pour la communication.
- **Rédaction du cahier des charges.**

Bonne dynamique de groupe. Tout le monde est proactif et apporte ce qu'il souhaite
au projet.

> ## Vendredi 11 Septembre :
## [Groupe]
- Réflexion sur l'architecture faite à la suite du cours que l'on a eu le jour même. 
Nous avons remarqué que, l'architecture sur laquelle nous avions commencé à 
réfléchir correspondait à une architecture en couches et que ce type restait le plus 
cohérent pour le projet que nous réalisons.  
- Réflexion sur l'authentification: Nous avons envisager d'utiliser Google comme SSO, 
mais après discussion entre les membres du groupe il a été décidé d'utiliser le 
format de login : e-mail et mot de passe qui seront stocké dans une base de donnée
en locale + double authentification avec code à usage unique envoyé par mail.

## [Eliott]
- Confection d'un premier schéma très simpliste pour décrire les échanges possibles
entre les différentes familles de composant:

  <img width="466" height="655" alt="image" src="https://github.com/user-attachments/assets/27f3d75b-2076-4c69-b458-0c468ee00a6b" />
- Confection d'une liste d'API que l'on pourrait utiliser pour récupérer les 
informations sur les différents marchés financier:
  - Finnhub
  - TwelveData
  - yfinance python framework
- Réflexion sur de nouvelles "user storie" afin d'avoir une idée plus précise des
fonctionnalités à développer.

## [Amarante] 
- Réflexion sur l'architecture de l'application au travers d'un schéma. 
- Nous avons prévu une application web ambitieuse (beaucoup d'options/de services).
Questionnements sur la faisabilité du projet dans les temps impartis. L'architecture
web faite à ce moment sera déterminante pour la suite et la bonne réalisation du 
projet sans se casser les coudes.
- Nécessité de faire des maquettes du site web pour définir l'emplacement de chaque
composant dans l'optique que ça soit collaboratif et de ne pas perdre du temps à 
refactorer.


## [Oscar] 
- Conception des maquettes du design du futur site de la page d'accueil et de connexion. 
- Élaboration et envoie d'un premier task graph avec les relations entre l'architecture, le backend et l'API financière.
- Réflexion sur la partie responsive et le passage au format mobile. 
- Listing des fonctionnalités du site par rapport aux produits financiers (PEA, ETF, Assurance vie ?, CTO)
qu'on proposera ainsi que de leur portée géographique (US, Europe, émergent)

> ## Mercredi 16 Septembre :

## [Groupe]

- Choix final des API :
  - Finhub, pour la récupération des prix des actions et ETF en temps réels. Cette API reste le choix le plus intéressant dû au faite qu'elle propose un webhook où l'on peut s'abonner à des flux qui envoie des messages à chaque mise à jour du prix d'une action. Limitations = 50 symboles 
  - Alpha Vantage, pour la récupération des prix historique des actions par jour sur 1 an, ou par semaine sur toute l'existence de l'action demandée. Limitations = 25 requêtes par jour.

- Réflexion sur les modèles de données pour la base de donnée de Django.

## [Eliott]

- Téléchargement du framework Django.
- Création du projet Django TaurusCapital, créations des app : authentification et simulation.

## [Amarante]
- Réflexion MCD.
<img width="694" height="568" alt="mcd" src="https://github.com/user-attachments/assets/f2c9be37-4b30-42bb-9452-7df7310b738f" />

## [Oscar]

- Conception du frontend basé sur les maquesttes de design réalisées à la séance précédente.
- Réflexion sur le modèle entité-association du projet. 
