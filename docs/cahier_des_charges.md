~~# Cahier des charges


## 1. Contexte et présentation du projet

### Rappel du périmètre de l'exercice
Dans le cadre du module académique PRO8501 nous devons réaliser un projet informatique dont le sujet est libre de choix.

Ce dernier doit contenir 3 axes :
- **Visuel** : interface web.
- **Réseau** : notion de temps réel (supervision de routeurs, …).
- **Langage** : Python doit être le langage le plus utilisé.

Nous pouvons implémenter des options utilisant des **modèles d'IA** dans 
l'application. Cependant, son utilisation pour le développement est formellement interdit.


### Les français, des gestionnaires financiers hors-pair ? 

Historiquement, les français ont une épargne financière relativement élevée, principalement placée sur des actifs non-risqués tel que les livrets bancaires réglementés ou les contrats d'assurance-vie. Une importante partie du patrimoine des ménages se concentre sur l'immobilier. Alors même que l'accès à la propriété est de plus en plus difficile. Comme l'atteste BFM Finance, le nombre de ménages accédants a reculé de 21,4 % à 19,8% de 2020 à 2026. En revanche, le taux de français propriétaires reste quasi-stable depuis 2014, culminant à 57,8%. Signifiant qu'on constate de moins en moins de primo-propriétaires, mais ceux qui le sont déjà possède davantage de part du parc immobilier en France. Cela est dû notamment à un prix de l'immobilier, des taux d'interêts plus importants, phénomène combiné à un revenu moyen moyen qui n'a pas suivi cette augmentation.

Face à cela, de plus en plus de Français se tournent vers l'investissement boursier. En effet, selon l’Autorité des marchés financiers (AMF), les Français sont de plus en plus nombreux à s’intéresser à l’investissement en bourse. 
En effet, d’après l’AMF ([*La Bourse séduit un nombre record d’investisseurs particuliers en 2025*](https://www.amffrance.org/fr/actualites-publications/communiques/communiques-de-lamf/la-bourse-seduit-un-nombre-record-dinvestisseurs-particuliers-en-2025)), un peu plus de **1,9 million de Français** ont réalisé au moins un achat ou une vente d’actions en 2025, soit une hausse de **21 % par rapport à 2024**.

Plus globalement, entre 2023 et 2025, **1,6 million de nouveaux investisseurs** ont rejoint les marchés financiers, aussi bien sur les actions que sur les ETF (fonds indiciels). 

Ces données témoignent donc d’un **intérêt croissant pour les marchés financiers**, particulièrement auprès des jeunes générations. 

L'investissement boursier implique généralement d'une bonne hygiène et littérature financière. Cependant, l'accès à cette dernière reste très inégale. 


## 2.	Fonctionnalités 

### MVP 
- Suivi du portefeuille de patrimoine en 360 des actifs financiers de l'utilisateur (PEA, Livret, Immobilier, Héritage etc...) 
- Historique de l'évolution du patrimoine de l'utilisateur 
- Gestion des dépenses de la vie courante et revenu 
- L'utilisateur doit pouvoir se connecter à un compte personnel sécurisé avec un système d'authentification Django sera utilisé.
- Outils d'audit interne avec scoring en fonction des objectifs FIRE (Financial Independence, Retire Early)

  
### Lot 1 
- Création de catégories personnelles dans la gestion des dépenses et revenu (e.g. Voyage Italie)
- Projection linéaire du plan d'investissement de l'utilisateur avec concordance des objectifs spécifiés 
- Le partage de sa stratégie à d'autres utilisateurs


### Lot 2
- Rapport des actualités par IA et conseils
- Partage de stratégie à d'autres utilisateurs
  
## 3. Ressources disponibles
- Ressources humaines : trois étudiants en école d'ingénieurs.
- Ressources techniques : inférence IA, cluster IA, machine virtuelle du service MINET.
- Ressources techniques à identifier : accès à une (ou plusieurs) API publique(s) de données financières couvrant actions/ETF européens et taux du Livret A.

L'utilisation du cluster IA pourra être envisagé dans le cas où on décide 
d'entraîner notre propre modèle.


## 4.	Délais

Le livrable est à rendre pour le 9 décembre 2026. Le projet devra être idéalement finalisé le 5 décembre 2026.~~
