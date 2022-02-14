# MySite Portfolio Blog

## *Version 1*

## Plan du projet

### Description

Création d'un `site web blog et portfolio` dans la quelle je partage mes projets et ecrire des tutoriels sous forme d'article. Les utilisateurs peut consulter mes projets, lire mes article (tutoriel) et peut liker mes articles et commenter. L'administracteur (moi) doit créer, modifier et supprimer les articles et projets.

Les principales sujets du site :

* **Machine Learning** : collocter traiter, analyser, modeliser et déployer
* **Dévéloppement Web** : céer des sites application web avec Python (Django, Flask, Streamlit et FastAPI), HTML, CSS et Javascript
* **Dévéloppement Mobile** : céer des sites application mobiles avec Fluter
* **Dashboaring** céer des sites application dashboard avec Power BI et Dash Plotly

Les principales utilisateurs sont : `Recruteur`, `Toutes personnes intéresser`

### USE CASE

Administracteur <---------> se connecter et se déconnecter
Administracteur <---------> créer, modifier et supprimer un article ou projet
Utilisateur <---------> consulter, liker et commenter

## Modèles de données

* **Base de données** : PostgreSQL
* **Tables** : BlogArticle, Comment, TabLike

**La table BlogArticle** :

1. id de l'article
2. titre de l'article
3. catégorie de l'article
4. introduction de l'article
5. body de l'article
6. auteur de l'article : clef étrangère de la table User
7. slug de l'article
8. date de création de l'article
9. image de l'article

**La table Comment** :

1. id du commentaire
2. titre de l'article commenter (post) : clef étrangère de la table BlogArticle
3. prénom de l'auteur du commentaire
4. nom de l'auteur du commentaire
5. email de l'auteur du commentaire
6. métier de l'auteur du commentaire
7. body de l'auteur du commentaire
8. date de création du commentaire

**La table Contact** :

1. nom
2. adresse mail
3. message

## Relation entre les table

BlogArticle N--1 User
BlogArticle 1--N Comment  


## Aplication

**Version 1 :** App_Article
