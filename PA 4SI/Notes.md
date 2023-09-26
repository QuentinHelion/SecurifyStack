**

MACHINE PROXMOX

  

- Il faut un serveur physique chez le client mais :

- Installer manuellement PROXMOX ? 

- Avantage : Utiliser toutes les ressources pour la virtualisation

- Probleme : Où mettre la webapp ? (on suppose que cest un docker)

- Possibilité d'un ISO customisé (avec fichiers des reponses de l'install : technique unattended installation)

  

- Installer une distrib pour tout heberger (Debian) : 

- Avantages : Permettra de scripter l'install de Proxmox / Permettra de mettre la webapp dessus

- Probleme : on aura un OS  + Proxmox : on perd en ressources

  

IMPOSSIBLE DE CREER CETTE MACHINE A PARTIR DE NOTRE WEBAPP, AVOIR UNE MACHINE AVEC PROXMOX EST UN PRE-REQUIS, on va juste essayer de trouver la meilleure solution qu'on peut proposer au client

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

TECHNOS POUR LA WEBAPP

  

Propositions pour le Front-end : 

- React + JS 

- React + TS (la même chose mais en 100x plus chiant, mais le code est facile à lire)

  

Propositions pour le Back-end :

- JS :D : un modèle MVC (Models, View, Controllers) pour les endpoints de l'API

  

DASHBOARDS : 

  

- 1 pour edit le/les fichiers de conf Terraform (pour déployer les machines , préciser les ressources etc …) possibilités template + full custom
    
- 1 pour edit le/les fichiers de conf Ansible (la config systèmes : création de users etc …) possibilités template + full custom
    
- 1 pour visualiser les logs 
    
- 1 pour monitorer les VMs (graphes de perf depuis proxmox)
    
- 1 page de DOC
    

  

Système de droits sur les users (admin avec MFA …)

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

INFRA

  

Machines Windows :

1 environnement AD avec : 

- 2 DC (répliqué / redondé)

- 1 poste client (pour les logs)

- ...

  

Contenaires Docker : 

 L'agent de LOGS 

 un serveur web

 ...

  

Machines Linux

1 poste client (pour les logs)

  

Trouver un moyen d’implementer kubernetes 

  
  

SYSTEME DE SAUVEGARDE!!!!!

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

LE LOG AGENT

  

3 Composants essentiels : 

  

- Un collecteur de logs 
    
- Un indexeur / filtre de logs
    
- Un viewer de logs intéractif (navigation etc)
    

  

Ajouter un système d’alertes par importance par mails et notifs (omg un appli mobile en plus ??? )

  

Choisir des indexs de logs précis pour créer des scripts de mitigation et les configurer à être déployés automatiquement dès qu’un event avec cet ID remonte

  
  
**