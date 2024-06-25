# TDD_RPG_Exercice

# Comparaison de Différentes Solutions d'Intégration Continue

## 1. **Jenkins**

**Type :** Client lourd

**Fonctionnement :**
Jenkins est un serveur d'automatisation open source écrit en Java. Il permet de configurer des tâches via une interface web ou des fichiers de configuration, et peut intégrer une grande variété d'outils de développement à travers ses plugins.

**Avantages :**
- **Open Source** : Gratuit et largement supporté par la communauté.
- **Extensible** : Grande variété de plugins pour étendre ses fonctionnalités.
- **Flexible** : Peut être configuré pour s'adapter à presque tous les scénarios de CI/CD.

**Inconvénients :**
- **Complexité** : Configuration initiale et maintenance peuvent être compliquées.
- **Interface Utilisateur** : Interface utilisateur vieillissante et peu intuitive.
- **Administration** : Nécessite souvent une gestion dédiée pour les mises à jour et la maintenance.

## 2. **Travis CI**

**Type :** Client léger

**Fonctionnement :**
Travis CI est un service de CI hébergé qui est profondément intégré avec GitHub. Les configurations sont définies dans un fichier `.travis.yml` à la racine du dépôt, où les utilisateurs peuvent spécifier les langages, les versions de langages, les scripts à exécuter, et bien plus.

**Avantages :**
- **Intégration GitHub** : Parfaitement intégré avec GitHub, simple à configurer avec les dépôts GitHub.
- **Facilité d'utilisation** : Configuration facile via le fichier `.travis.yml`.
- **Gratuit pour les projets open source**.

**Inconvénients :**
- **Tarification** : Coût relativement élevé pour les projets privés.
- **Performance** : Parfois des délais d'attente pour le démarrage des builds en raison de la popularité.

## 3. **CircleCI**

**Type :** Client léger

**Fonctionnement :**
CircleCI est une plateforme de CI/CD qui permet de configurer des workflows à travers un fichier de configuration YAML (`.circleci/config.yml`). Les workflows définissent comment les tests et les déploiements sont réalisés à chaque changement de code.

**Avantages :**
- **Rapidité** : Connu pour sa vitesse et son efficacité.
- **Flexibilité** : Supporte les workflows complexes et offre une configuration flexible.
- **Intégration** : Bonne intégration avec divers services et plateformes.

**Inconvénients :**
- **Complexité de configuration** : Peut nécessiter une courbe d'apprentissage pour les configurations avancées.
- **Tarification** : Structure de prix qui peut devenir coûteuse pour les équipes plus grandes.

## 4. **GitHub Actions**

**Type :** Client léger

**Fonctionnement :**
GitHub Actions permet d'automatiser des workflows directement à partir du dépôt GitHub via des fichiers de configuration YAML. Ces workflows peuvent être déclenchés par différents événements GitHub comme les push, les pull requests, ou sur un cron schedule.

**Avantages :**

- **Intégration native GitHub** : Fonctionne de manière fluide avec les dépôts GitHub.
- **Facilité d'utilisation** : Utilisation de YAML pour configurer les workflows.
- **Flexibilité** : Extensible avec des actions personnalisées et une grande variété d'actions disponibles dans le marketplace.
- **Coût** : Gratuit pour les projets open source et généreux plan gratuit pour les projets privés.
- **Performances** : Excellentes performances avec des exécutions parallèles et un démarrage rapide des workflows.

**Inconvénients :**

- **Nouvel outil** : Encore relativement nouveau, donc potentiellement moins de plugins disponibles comparé à Jenkins.
- **Documentation** : Peut nécessiter une exploration initiale de la documentation pour bien comprendre toutes les fonctionnalités.

# Pourquoi Nous Avons Choisi GitHub Actions

Nous avons choisi GitHub Actions pour plusieurs raisons clés :

1. **Intégration Native** : L'intégration directe avec GitHub facilite la configuration et le déclenchement des workflows basés sur des événements spécifiques comme les push, les pull requests, etc.
2. **Facilité d'utilisation** : La configuration en YAML est simple et intuitive, ce qui permet une mise en place rapide et une gestion aisée des workflows.
3. **Coût** : Le plan gratuit pour les projets privés est généreux, ce qui est avantageux pour notre budget.
4. **Flexibilité et Extensibilité** : La possibilité d'utiliser et de créer des actions personnalisées nous permet d'adapter facilement notre pipeline CI à nos besoins spécifiques.
5. **Performances** : Démarrage rapide des builds et exécutions parallèles permettent de réduire le temps de feedback, augmentant ainsi notre efficacité.

