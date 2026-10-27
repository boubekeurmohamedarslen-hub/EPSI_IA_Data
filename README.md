# EPSI IA & Data Science

Dépôt regroupant mes exercices réalisés dans le cadre de ma formation en Intelligence Artificielle et Data Science à l'EPSI. Chaque script se lance seul et travaille sur un petit jeu de données écrit dans le code.

Mes projets plus complets sont dans des dépôts séparés :

- [Sentinel-X](https://github.com/boubekeurmohamedarslen-hub/Sentinel-X) : surveillance sur ESP32-CAM, YOLO, reconnaissance faciale YuNet/SFace, MQTT et dashboard Django
- [analyse_agricole](https://github.com/boubekeurmohamedarslen-hub/analyse_agricole) : audit et nettoyage d'un jeu de données agricoles avec Pandas

## Structure

### 01_python

Bases de Python : conditions, boucles, listes, fonctions et chaînes de caractères.

| Fichier | Contenu |
|---|---|
| `moyenne_notes.py` | moyenne d'une liste de notes et résultat validé ou non |
| `notes_validees.py` | boucle sur une liste de notes, première DataFrame Pandas |
| `fonction_evaluer_note.py` | fonction à plusieurs seuils (excellent, admis, refus) |
| `fonction_admission.py` | fonction avec `return` |
| `examen_blanc_notes_admises.py` | filtrer une liste dans une fonction |
| `boucle_while.py` | boucle `while` |
| `manipulation_chaines.py` | `lower()`, `split()`, `append()`, `sort()` |

### 02_pandas_data_analysis

Manipulation et analyse de données avec Pandas : filtres combinés, moyennes, minimums et maximums, tri, colonnes calculées avec `apply()`.

| Fichier | Contenu |
|---|---|
| `dataframe_et_graphique.py` | création d'une DataFrame et diagramme en barres Matplotlib |
| `filtres_admis_majeurs.py` | filtres avec `&` et `\|`, admis et non admis |
| `tri_et_moyenne.py` | moyenne et tri avec `sort_values()` |
| `analyse_classe.py` | statistiques d'une classe, filtre note et âge, évaluation par élève |
| `analyse_employes.py` | salaires, ancienneté, classement des salaires, profils expérimentés |
| `resultats_etudiants.py` | colonne de résultat ajoutée avec `apply()` |
| `reprise_pandas.py` | exercice de synthèse : classement, écart à la moyenne, position par rapport à la moyenne |

### 03_machine_learning

Premiers modèles avec Scikit-learn : régression linéaire qui prédit une note à partir des heures de travail.

| Fichier | Contenu |
|---|---|
| `regression_lineaire.py` | `fit()` puis `predict()` sur un seul jeu de données |
| `regression_train_test.py` | séparation train/test avec `train_test_split`, comparaison des vraies notes et des prédictions |

### 04_notebooks

| Fichier | Contenu |
|---|---|
| `verification_environnement.ipynb` | vérification de l'installation de NumPy, Pandas, Matplotlib et Scikit-learn |

## Lancer les scripts

```bash
pip install -r requirements.txt
python 02_pandas_data_analysis/analyse_classe.py
```

## Technologies

Python • Pandas • NumPy • Matplotlib • Scikit-learn • Jupyter • Git • GitHub

## Parcours

Je suis étudiant en Expert IA & Data Science à l'EPSI, avec une formation initiale en Automatique et Systèmes.

Mon parcours m'a également permis de travailler sur le traitement du signal, notamment autour des signaux PPG/NIR, ainsi que sur des projets liés aux systèmes intelligents.

## Objectif professionnel

Je recherche une alternance en Île-de-France dans les domaines :

- Intelligence Artificielle
- Machine Learning
- Data Science
- Data Analysis
- Data Engineering

Ce dépôt sera régulièrement enrichi avec mes futurs exercices Data et Machine Learning.
