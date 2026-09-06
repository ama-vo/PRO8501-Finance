~~# Cahier des charges


### Exercice 
Dans le cadre du module académique PRO8501 nous devons réaliser un **Projet 
Informatique en Python**.

Cet exercice est un exercice libre dans lequel chaque groupe peut réaliser 
ce qu'il souhaite avec trois critères principaux :
- **Avoir une partie visuelle** : interface web.
- **Avoir une partie réseau** : notion de temps réel (supervision de routeurs, …).
- **Langage** : Python doit être le langage le plus utilisé.

De plus, nous pouvons implémenter des options utilisant des **modèles d'IA** dans 
l'application, néanmoins nous ne pouvons pas en utiliser pour coder.


## 1. Contexte et définition du problème

Selon l’Autorité des marchés financiers (AMF), les Français sont de plus en plus 
nombreux à s’intéresser à l’investissement en bourse. 
En effet, d’après l’AMF ([*La Bourse séduit un nombre record d’investisseurs particuliers en 2025*](https://www.amf-france.org/fr/actualites-publications/communiques/communiques-de-lamf/la-bourse-seduit-un-nombre-record-dinvestisseurs-particuliers-en-2025)), 
un peu plus de **1,9 million de Français** ont réalisé au moins un achat ou une 
vente d’actions en 2025, soit une hausse de **21 % par rapport à 2024**.

Les ETF constituent également un produit d’investissement de plus en plus populaire 
auprès des ménages français. 
En 2025, environ **1,1 million d’investisseurs** ont investi dans des fonds indiciels, 
contre **223 000 en 2020**. 
Le nombre d’investisseurs en ETF a ainsi été multiplié par
cinq en cinq ans.

Cette démocratisation de l’investissement s’accompagne également d’un 
**rajeunissement des investisseurs**. 
Toujours selon l’AMF, l’âge moyen des investisseurs en ETF en France est passé de 
**61,1 ans en 2019 à 41,3 ans en 2024**. 
Chez les 25–35 ans, **45 % des investisseurs actifs** avaient acheté ou vendu 
des ETF au premier semestre 2024, contre seulement **11,7 % en 2019**. 
Cette tendance s’est poursuivie en 2025, avec un âge moyen des investisseurs en 
ETF qui est désormais descendu à 38 ans.

Plus globalement, entre 2023 et 2025, **1,6 million de nouveaux investisseurs** 
ont rejoint les marchés financiers, aussi bien sur les actions que sur les ETF. 
Pour la première fois depuis le 1er janvier 2018, les nouveaux investisseurs ont 
également représenté la catégorie ayant réalisé le plus grand nombre d’ordres d’achat.

Ces données témoignent donc d’un **intérêt croissant pour les marchés financiers**, 
particulièrement auprès des jeunes générations. 
Cependant, pour un investisseur débutant, l’accès aux marchés financiers peut 
rester complexe. 
La diversité des produits disponibles, le vocabulaire financier, le fonctionnement 
des marchés et le nombre important d'information en ligne constituent une barrière de difficulté pouvant freiner l'apprentissage de ce dernier.

Le but de notre projet est donc de répondre à cette problématique :

**Comment permettre aux nouveaux investisseurs, notamment aux jeunes générations, de découvrir les marchés financiers, de comprendre les produits d’investissement et d’expérimenter différentes stratégies sans s’exposer à un risque financier réel ?**

C’est donc dans ce contexte d'adoption progressive par des particuliers de plus en plus jeunes
que s’inscrit notre projet. 
Nous souhaitons, par conséquent, mettre en place une **plateforme fictive d’investissement et d’éducation financière**, 
sous forme de site web, permettant aux utilisateurs de se familiariser avec les mécanismes des marchés 
financiers dans un environnement sans risque réel.



## 2.	Objectifs

Cette plateforme fictive d’investissement, que nous nommerons **Taurus Capital**, 
s’articulera autour de sept grands objectifs, qui guideront son développement :

1) **Simuler des investissements financiers**  
La plateforme permettra à l'utilisateur d'acheter ou de vendre des actions ou ETF, 
à partir de données antérieures ou en temps réel.

2) **Reproduire l'expérience d'un investissement réel**  
On devra permettre à l'utilisateur d’observer l’évolution de la valeur de son 
portefeuille en fonction des fluctuations du marché.

3) **Permettre l’expérimentation de différentes stratégies**  
On donnera la possibilité à l’utilisateur de construire et de modifier un 
portefeuille virtuel afin de comparer différentes approches d’investissement 
et d’en observer les performances. On pourra implémenter des critères comme le 
DCA (Dollar Cost Averaging), c'est-à-dire l'achat programmé périodique, différents
montants de frais d'achat, différentes enveloppes fiscales (PEA, CTO, assurance-vie) 
ou alors différents marchés.

4) **Exploiter les données historiques**
Taurus Capital permettra à l’utilisateur de se placer à une date donnée dans le passé 
et de simuler les conséquences d’un investissement réalisé à cette période. 
Il pourra ainsi analyser après coup, les performances obtenues et mieux comprendre 
l’impact du choix de la date d’investissement.

5) **Assurer un suivi en temps réel** 
À l'aide des sockets réseau notamment, le site devra actualiser régulièrement 
les cours des actifs suivis afin que l’utilisateur puisse observer les fluctuations 
du marché et de son portefeuille virtuel. Cette fonctionnalité permet également 
de répondre à la contrainte de partie réseau et de notion de temps réel du projet.


6) **Fournir des informations pédagogiques** 
Pour répondre à la dimension éducative, une section sera dédié à accompagner 
l’utilisateur dans la compréhension des différents produits financiers, 
du fonctionnement des marchés et des principaux indicateurs utilisés pour 
évaluer un investissement. Cela pourra se présenter sous la forme d'articles ou 
de fiches de synthèse informationnelles.

7) **Intégrer des fonctionnalités basées sur l’intelligence artificielle** 
L'IA étant un sujet qui nous tient à coeur, on aimerait implémenter des fonctionnalités 
capable générer des rapports et des analyses à partir des données disponibles sur 
un secteur, l’état général du marché ou d'une action spécifique. 
Ces rapports pourront notamment mettre en évidence des évolutions 
importantes, des événements d'actualité susceptibles d’influencer 
les marchés ou certains risques associés à un investissement.


## 3.	Périmètre du projet

La finance étant un domaine vaste, nous nous concentrerons dans ce premier temps
sur : 
- l'achat factice de fonds à une date utlérieure ou actuelle.
- la création d'analyses du marché ou de fonds précis grâce à l'IA.

Dans un second temps, nous pourrions, bien que cela ne soit pas l'object de
notre projet à ce stade : 
- créer un simulateur itératif sur _d'anciennes données_ avec la méthode de
Monte Carlo.

## 4.	Description fonctionnelle des besoins

### Profil Investisseur
- L'utilisateur doit pouvoir se connecter à un compte personnel sécurisé.
- L'utilisateur doit pouvoir compléter de nombreuses informations sur son 
profil et ses préférences financières. 

### Investissements financiers factices

- L'utilisateur doit pouvoir faire des ordres d'achat factice (ordre au marché
ou à cours limité).
- L'utilisateur doit pouvoir simuler des plans d'investissement dans le passé.
- L'utilisateur doit pouvoir simuler des plans d'investissement sur le marché 
actuel, qui évolue avec celui-ci.
- L'utilisateur doit pouvoir faire le choix entre 3 types de comptes simulés (PEA, 
Livret A, Compte titre) afin d'étudier différentes stratégies qu'il pourrait 
employer pour son épargne.
- L'utilisateur peut être notifié pour des ordres d'achat, s'il décide de mettre
en place des alertes pour des seuils, ou pour être informé de la création d'un 
rapport automatique.

### Compte rendu IA
- L'utilisateur doit pouvoir accéder une analyse IA détailée de l'ensemble des
fonds d'investissements présents, cela en temps réel lors de sa requête.
- L'utilisateur doit pouvoir créer des rapports se basant sur des nouvelles 
impactant les différents marchés financiers, qui lui indiquent au moins 3 actions 
risquant d'être influencées par ces nouvelles.
- L'utilisateur doit pouvoir accéder à une interface lui permettant de 
s'informer des différences de modalités entre les différentes enveloppes 
de différents courtiers.
  
## 5.	Enveloppe budgétaire et ressources

Les ressources dont nous disposons pour ce projet sont : 
- Ressources humaines : trois étudiants en école d'ingénieurs.
- Ressources techniques : outils Minet, Cluster IA.

L'utilisation du cluster IA pourra être envisagé dans le cas où on décide 
d'entraîner notre propre modèle.

Ce projet étant académique nous ne possédons pas de ressources pécuniaires.

## 6.	Délais

Le livrable est à rendre pour le 9 décembre 2026. Le projet devra être finalisé 
le 5 décembre 2026.~~
