#README DU GROUPE E5 

#STRUCTURE DE NOTRE DOSSIER
Dans le repértoire du projet(flask), vous trouverez 
* plusieurs dossiers (dont) :
	Static    : contient des images et des styles utilisés pour donner un meilleur apérçu de notre site web.
	Templates : contenant les fichiers html.

* 3 fichiers: app.py, functions.py, inginious.sqlite.
	App.py           : fichier à utiliser pour lancer le site web et contient quelques fonctions qui manipule la base de donnée.
	Functions.py     : contient quelques fonctions qui manipule la base de donnée.
	Inginious.sqlite : base de donnée de ce projet.

#STRUCTURES DE NOS FONCTIONS (DANS APP.PY)
* fonction 'home()' 	: renvoit la page principale de notre site web.

ensuite, les fonctions pour chaque cours. Il y a 4 fonctions par cours:

* fonction 'nom_du_cours'        	: Calcule le nombre de soumission dans ce cours.

* fonction 'generalnom_de_cours' 	: calcule le nombre de soumission global par mois.

* 'error()'                     	: calcule le pourcentage de nombre des soumissions qui ont été réussi, échoué, renvoyé 'error', etc. 

* fonction 'fct_for_"nom_de_cours"' : renvoit la moyenne de réussite de chaque tâche du cours en question.

puis:

* fonction 'contact()'  : renvoit la page de contact.

#STRUCTURE DE NOTRE SITE WEB
Sur le site web:

Nous avons créé un menu qui contient tous les cours de la base de donnée et une petite description(si vous descendez vers le bas). Dans chaque cours, vous trouverez l'analyse des différents aspects présentés sous forme des graphiques.

#POUR LANCER NOTRE SITE WEB 

Pour lancer notre site web, il vous faut écrire " python 'app.py' " dans le terminal en veillant bien être dans le dossier 'flask'.
Normalement, ça va vous envoyer un lien : 127.0.... que vous pouvez copier et le coller dans google chrome ou autre pour demarrer notre site web.


