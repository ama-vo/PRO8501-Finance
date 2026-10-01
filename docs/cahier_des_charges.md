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


## 2.	Taurus Capital 

Le but de notre projet est donc de proposer un outils de gestion de patrimoine afin de le rendre accessible au plus grand nombre. 

Pour cela, nous proposons le développement d'une application web qui est basée sur deux noyaux à valider qui serviront de KPI de mesure de notre réussite. 
Le premier point sera de centraliser les données de patrimoine tel que son patrimoine immobilier, l'épargne salariale, les actifs financiers, les différents livrets, le patrimoine matériel ou les dettes, pour en citer quelques-uns. 

Le deuxième point est de proposer également en temps réel la mise à jour du portefeuille d'investissement et de pouvoir proposer le partage entre utilisateurs de leurs portefeuilles. 


## 3.	Description fonctionnelle des besoins

### Profil Investisseur
- L'utilisateur doit pouvoir se connecter à un compte personnel sécurisé. Un système d'authentification Django sera utilisé.
- Complétion des informations sur son son patrimoine et sa stratégie d'investissement.
- Le partage de sa stratégie à autrui.

### Investissements financiers factices

- L'utilisateur doit pouvoir faire des ordres d'achat factice (ordre au marché
ou à cours limité).
- L'utilisateur doit pouvoir simuler des plans d'investissement dans le passé.
- L'utilisateur doit pouvoir simuler des plans d'investissement sur le marché 
actuel, qui évolue en temps réel avec celui-ci.
- L'utilisateur doit pouvoir faire le choix entre 4 types de comptes simulés (PEA, 
Livret A, Compte titre, assurance vie) afin d'étudier différentes stratégies qu'il pourrait 
employer pour son épargne.
- L'utilisateur pourra décider des frais de courtage si il simule un comptes de type PEA ou Compte-Titre.
- L'utilisateur peut être notifié pour des ordres d'achat, s'il décide de mettre
en place des alertes pour des seuils, ou pour être informé de la création d'un 
rapport automatique.
- L'utilisateur doit pouvoir faire des achats programmés périodiques (DCA ou Dollar 
Cost Averaging).
- L'utilisateur doit pouvoir accéder aux montants des frais d'achat.

### Compte rendu IA
- Système de scoring par rapport à sa stratégie d'investissement basé sur la diversification, et la cohérence financière.
- L'utilisateur doit pouvoir accéder une analyse IA détailée de l'ensemble des
fonds d'investissements présents, cela en temps réel lors de sa requête.
- L'utilisateur doit pouvoir créer des rapports se basant sur des nouvelles 
impactant les différents marchés financiers, qui lui indiquent au moins 3 actions 
risquant d'être influencées par ces nouvelles.
- L'utilisateur doit pouvoir accéder à une interface lui permettant de 
s'informer des différences de modalités entre les différentes enveloppes 
de différents courtiers.

### Contenus pédagogiques
- L'utilisateur doit pouvoir accéder à une section dédiée à l'accompagner 
dans la compréhension des différents produits financiers, du fonctionnement des
marchés et des principaux indicateurs utilisés pour évaluer un investissement. 
Cela pourra se présenter sous la forme d'articles ou de fiches de synthèse 
informationnelles.
- L'utilisateur doit pouvoir accéder à un chat dédié pour comparer les enveloppes
fiscales de différentes banques. 
  
## 4. Ressources disponibles
- Ressources humaines : trois étudiants en école d'ingénieurs.
- Ressources techniques : inférence IA, cluster IA, machine virtuelle du service MINET.
- Ressources techniques à identifier : accès à une (ou plusieurs) API publique(s) de données financières couvrant actions/ETF européens et taux du Livret A.

L'utilisation du cluster IA pourra être envisagé dans le cas où on décide 
d'entraîner notre propre modèle.


## 5.	Délais

Le livrable est à rendre pour le 9 décembre 2026. Le projet devra être idéalement finalisé le 5 décembre 2026.~~
