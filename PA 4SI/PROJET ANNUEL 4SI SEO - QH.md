### Nom du projet : SecurifyStack

### Logo : 



### **Résumé du Projet : Gestion Centralisée et Sécurisée de l'Infrastructure avec un Système de logs Personnalisé**

Ce projet vise à automatiser, sécuriser et rationaliser la gestion de l'infrastructure pour les administrateurs système grâce à une application web centralisée. Les composants clés et les objectifs incluent :

**1. Provisionnement du serveur Proxmox :**

- Installation automatisée et configuration de base d'un serveur Proxmox sur un matériel physique, servant d'infrastructure pour le déploiement de machines virtuelles.

**2. Dashboards sur une Application Web :**

- Des dashboards unifiés sur une application web qui permettent aux utilisateurs de :
    - Créer, configurer et supprimer des machines virtuelles en utilisant Terraform et Ansible.
    - Accéder à un visualiseur de journaux personnalisé intégré avec des graphiques pour l'analyse des logs.
    - Surveiller les données de performance de chaque machine virtuelle, extraites directement de Proxmox (RAM utilisée, espace disque libre ...)
- La web app sera développée en React + TypeScript pour le frontend et du JS classique pour le backend (suivant un modèle MVC)

**3. IaC : Infrastructure as Code (Terraform et Ansible) :**

- Terraform pour la provision des composants de l'infrastructure, y compris les machines virtuelles, les réseaux et le stockage.
- Ansible pour la configuration après la provision et la gestion au niveau du système, offrant des options de flexibilité et de personnalisation.

**4. Intégration d'un Système de logs Personnalisé :**

- Un système de journalisation personnalisé développé from scratch, automatiquement implémenté avec chaque machine virtuelle déployée, centralisant les logs pour une analyse efficace.
- Des scripts prédéfinis dans le système de logs pour réagir instantanément aux événements suspects. Pour des événements indexés spécifiques, le système déclenchera des alertes et déploiera des scripts pour résoudre les problèmes rapidement.

**5. Sécurité et Contrôle d'accès :**

- Syteme d'authentification avec LDAPS (seuls les membres du groupe DC-admins peuvent accéder à l'interface + MFA)


**6. Aide Complète et Documentation :**

- Une page d'aide dédiée à l'intérieur de l'application web, offrant une documentation détaillée couvrant tous les aspects du projet, de la configuration initiale aux configurations avancées.

**7. Sauvegarde et Récupération en Cas de Catastrophe :**

- Mise en place de solutions de sauvegarde automatisées pour les machines virtuelles et le serveur Proxmox. Offre des options de sauvegardes planifiées et de restauration facile en cas de défaillance du système.

**8. Alertes et Notifications :**

- Mise en place de mécanismes d'alerte qui notifient les administrateurs des événements critiques ou des problèmes au sein de l'infrastructure. Permet la personnalisation des seuils d'alerte et des canaux de livraison (e-mail, SMS, etc.).

**9. Scripts et Automatisation Personnalisés :**

- Offre aux utilisateurs avancés la possibilité d'écrire des scripts personnalisés ou des flux de travail d'automatisation directement dans l'application web, leur permettant d'adapter le système à leurs besoins uniques.


## Scénario d'utilisation :

###  **Déploiement :**

Pour le déploiement, deux méthodes sont disponibles :

1. **Déploiement via Template :** L'utilisateur a la possibilité d'utiliser une infrastructure pré-configurée sous forme de modèle (template). Voici un schéma du template :

	[SCHEMA]
    
2. **Déploiement Personnalisé :** Pour plus de flexibilité, la webapp permet aux utilisateurs de personnaliser les fichiers de configuration selon leurs besoins. Ils peuvent ainsi créer une infrastructure sur mesure en utilisant la webapp.


### **Utilisation :**

Une fois le déploiement terminé, l'accès à la webapp (les 3 dashboards) est simple. L'utilisateur peut y accéder via l'adresse IP du serveur web local.