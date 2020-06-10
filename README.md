# python-django-liste-de-course
liste de course (CRUD, barrer debarrer un article)

BIENVENU A VOTRE LISTE DE COURSE

Commencez par cloner le projet avec la commande :
  - git clone https://github.com/Phetparisouk/listeCourse.git

Ce site realise en python (Django) vous permet de :
  - rajouter des articles a votre liste de courses,
  - la supprimer de la liste en cliquant sur le bouton-texte "supprimer" tout a gauche
  - l'editer en cliquant sur le libelle de l'article
  - la barrer ou la debarrer en cliquant sur le buton-texte "barrer"-"debarrer"


Le css se trouve dans la racine dans le dossier "static" <br/>
Les vues (affichage se trouve dans le dossier /liste/templates)<br/>
Le model de bdd -> /liste/models.py<br/>
Formulaire -> liste/forms.py<br/>
Route -> liste/urls.py<br/>
methode de views -> views.py


  

Pour cela il vous faudra installer le langage python dans votre machine local, mais aussi le module pylint sous cette commande:
  - pip install pylint-django
  
Avant de lancer le serveur, positionnez vous a la racine du projet et lancez les commandes pour faire les migrations de la BDD :
  - python manage.py makemigrations
  - python manage.py migrate
  
Enfin, lancez le server avec la commande :
  - python manage.py runserver
- Puis allez voir le resultat dans http://127.0.0.1:8000 (ou autre port mentionne dans votre console une fois que vous avez lancer la commande).


Pour etre plus guider, veuillez voir les 2 images en png "Guide en image" et "Guide en image - editer un article".



PS : Si vous utilisez VScode comme IDE, veuillez copier-coller ces parametres 
dans "C:\Users\{votre-nom-d-utilisateur}\AppData\Roaming\Code\User\settings.json" :
    {
        "python.linting.pylintArgs": [
            "--load-plugins=pylint_django",
            "--errors-only"
        ],
        "[python]": {
        },
    }
                    


