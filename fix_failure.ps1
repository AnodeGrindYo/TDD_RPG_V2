param (
    [string]$UniqueBranchSuffix,
    [string]$FeatureName
)

if (-not $UniqueBranchSuffix) {
    $UniqueBranchSuffix = Read-Host -Prompt "Entrez le suffixe unique de la branche failure"
}

if (-not $FeatureName) {
    $FeatureName = Read-Host -Prompt "Entrez le nom de la fonctionnalité"
}

# Récupére les modifications de la branche failure
git fetch origin

# Crée une nouvelle branche pour les corrections à partir de la branche failure
git checkout -b "fix_$FeatureName" "origin/failure/$UniqueBranchSuffix"

# Indique à l'utilisateur de corriger les erreurs
Read-Host -Prompt "Corrigez les erreurs, puis appuyez sur Enter pour continuer..."

# Ajoute et commitez les modifications
git add .
git commit -m "Correction des erreurs sur la branche failure et préparation pour re-push sur dev"

# Revient sur la branche dev
git checkout dev

# Fusionne les modifications de la branche de correction
git merge "fix_$FeatureName"

# Pousse les modifications vers la branche dev
git push origin dev

Write-Host "Modifications poussées avec succès vers dev."
