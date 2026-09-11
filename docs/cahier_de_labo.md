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

[Groupe]

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
[Groupe]
- Réflexion sur l'architecture faite à la suite du cours que l'on a eu le jour même. Nous avons remarqué que, l'architecture sur laquelle nous avions commencé à réfléchir correspondait à une architecture en couches et que ce type restait le plus cohérent pour le projet que nous réalisons.  
- Réflexion sur l'authentification: Nous avons envisager d'utiliser Google comme SSO, mais après discussion entre les membres du groupe il a été décidé d'utiliser le format de login : e-mail et mot de passe qui seront stocké dans une base de donnée en locale + double authentification avec code à usage unique envoyé par mail.
- 
  
[Amarante] 
- 

[Eliott]
- Confection d'un premier schéma très simpliste pour décrire les échanges possibles entre les différentes familles de composant:
  <img width="466" height="655" alt="image" src="https://github.com/user-attachments/assets/27f3d75b-2076-4c69-b458-0c468ee00a6b" />
- Confection d'une liste d'API que l'on pourrait utiliser pour récupérer les informations sur les différents marchés financier:
  - Finnhub
  - TwelveData
  - yfinance python framework
- Réflexion sur de nouvelles "user storie" afin d'avoir une idée plus précise des fonctionnalités à développer.
