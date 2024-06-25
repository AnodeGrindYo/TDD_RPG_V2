#!/bin/bash

# Vérifie si les arguments ont été fournis, sinon demandez-les à l'utilisateur
if [ -z "$1" ]; then
    read -p "Entrez le suffixe unique de la branche failure: " UNIQUE_BRANCH_SUFFIX
else
    UNIQUE_BRANCH_SUFFIX=$1
fi

if [ -z "$2" ]; then
    read -p "Entrez le nom de la fonctionnalité: " FEATURE_NAME
else
    FEATURE_NAME=$2
fi

# Récupére les modifications de la branche failure
git fetch origin

# Crée une nouvelle branche pour les corrections à partir de la branche failure
git checkout -b fix_${FEATURE_NAME} origin/failure/${UNIQUE_BRANCH_SUFFIX}

# Indique à l'utilisateur de corriger les erreurs
echo "Corrigez les erreurs, puis appuyez sur Enter pour continuer..."
read

# Ajoute et commitez les modifications
git add .
git commit -m "Correction des erreurs sur la branche failure et préparation pour re-push sur dev"

# Revient sur la branche dev
git checkout dev

# Fusionne les modifications de la branche de correction
git merge fix_${FEATURE_NAME}

# Pousse les modifications vers la branche dev
git push origin dev

echo "Modifications poussées avec succès vers dev."
