#!/bin/bash

# Création de l'environnement virtuel
python -m venv venv

# Activation de l'environnement virtuel
source venv/bin/activate

# Mise à jour de pip et installation des dépendances
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "L'environnement virtuel est prêt et les dépendances sont installées."
