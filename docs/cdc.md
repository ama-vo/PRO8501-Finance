~~# Cahier des charges

## 1. Contexte et définition du problème

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

### Orientation du groupe
L'ensemble de notre groupe a un attrait pour la **finance**.
Ce domaine nous permet d'implémenter l'ensemble des critères qui nous sont 
demandés.
Nous avons donc décidé de réaliser un projet lié à ce domaine.

## 2.	Objectifs

Le projet retenu par l'ensemble du groupe est un **Conseiller et Simulateur 
d'investissement financier**. 

Le but de ce simulateur est d'observer les rendements financiers effectifs ou
potentiels sur des marchés boursiers.
Ainsi, l'utilisateur peut acheter de manière factice des parts de fonds financiers
à une date antérieure (par exemple en janvier 2015) ou bien passer des ordres
factices en direct et voir le cours de son _achat_ fluctuer.

En parallèle de ce mécanisme qui permet à l'utilisateur de s'acculturer aux marchés
financiers, différents rapports génerés à l'aide de l'IA seront disponibles pour 
conseiller et avertir l'utilisateur des informations capitales en direct (cela 
sur des fonds précis ou bien sur le marché en général).

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
  
## 5.	Enveloppe budgetaire, ressources (minet, CLUSTER IA)

Les ressources dont nous disposons pour ce projet sont : 
- Ressources humaines : trois étudiants en école d'ingénieurs.
- Ressources techniques : outils Minet, Cluster IA.

Ce projet étant académique nous ne possédons pas de ressources pécuniaires.

## 6.	Délais (fin du semestre)

Le livrable est à rendre pour le 9 décembre 2026.~~