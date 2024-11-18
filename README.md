# PragChess

**PragChess** est une application graphique de jeu d'échecs minimaliste développée en Python avec Tkinter. Ce projet met en œuvre un plateau d'échecs fonctionnel permettant de déplacer des pièces conformément aux règles standard du jeu d'échecs.

## Fonctionnalités

- Interface graphique utilisant Tkinter.
- Déplacement des pièces en respectant les règles d'échecs.
- Tour par tour : gestion des joueurs (noirs et blancs).
- Visualisation en direct des mouvements sur le plateau.
- Gestion des règles de base pour toutes les pièces (pions, tours, cavaliers, fous, reines et rois).

## Prérequis

- Python 3.11
- Bibliothèque Tkinter (fournie par défaut avec Python pour la plupart des distributions)
- Les fichiers d'icônes des pièces d'échecs doivent être placés dans un dossier nommé `PNG2`, situé dans le même répertoire que le fichier principal.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/NSI-research/PragChess.git
   ```
2. Assurez-vous que le fichier d'icône `jeu-dechecs.ico` et les images des pièces (dans le dossier `PNG2`) sont disponibles dans le répertoire principal.

## Utilisation

1. Lancez l'application :
   ```bash
   python main0.2.py
   ```
2. Jouez en cliquant sur les cases pour sélectionner une pièce, puis sur la destination pour effectuer un mouvement.
3. Le jeu alterne entre les "Tours des Blancs" et les "Tours des Noirs".

## Structure du programme

- **Matrice** : représente l'état actuel du plateau sous forme de tableau 2D.
- **Fonction Play()** : gère la logique de mouvement des pièces.
- **Interface utilisateur** : construite avec Tkinter pour gérer les interactions.

## Développeur

- Auteur : **Lodjo28**
- Date : 12 mars 2024
- Version : 0.2

## Contribuer

Les contributions sont les bienvenues ! Si vous trouvez un bug ou souhaitez ajouter des fonctionnalités, n'hésitez pas à soumettre une pull request ou à ouvrir une issue.
