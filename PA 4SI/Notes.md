## MACHINE PROXMOX

  
Il faut un serveur physique chez le client mais :

 Installer manuellement PROXMOX ? 

 Avantage : Utiliser toutes les ressources pour la virtualisation

 Probleme : Où mettre la webapp ? (on suppose que cest un docker) / PE sur le poste de l'admin

 Possibilité d'un ISO customisé (avec fichiers des reponses de l'install : technique unattended installation)



 Installer une distrib pour tout heberger (Debian) : 

 Avantages : Permettra de scripter l'install de Proxmox / Permettra de mettre la webapp dessus

 Probleme : on aura un OS  + Proxmox : on perd en ressources



*IMPOSSIBLE DE CREER CETTE MACHINE A PARTIR DE NOTRE WEBAPP, AVOIR UNE MACHINE AVEC PROXMOX EST UN PRE-REQUIS, on va juste essayer de trouver la meilleure solution qu'on peut proposer au client

  
  

  
  
  

## TECHNOS POUR LA WEBAPP

  

Propositions pour le Front-end : 

- React + JS 

- React + TS (la même chose mais en 100x plus chiant, mais le code est facile à lire)

  

Propositions pour le Back-end :

- JS :D : un modèle MVC (Models, View, Controllers) pour les endpoints de l'API
comme ansible, le backend se connectera en SSH sur les machines pour 'executer les scripts de remédiati'
  

## DASHBOARDS : 

### INSTALLER : sur le poste d'un admin
 * 1 pour edit le/les fichiers de conf Terraform (pour déployer les machines , préciser les ressources etc …) possibilités template + full custom
    
- 1 pour edit le/les fichiers de conf Ansible (la config systèmes : création de users etc …) possibilités template + full custom

-  page de DOC


### WEB APP COMPLETE  :

Syteme d'authentification avec LDAPS (seul les membres du groupe IT peuvent reussir a s authentifier et seuls les membres du groupe DC-admins peuvent accéder à l interface en edit + MFA)

* 1 pour edit le/les fichiers de conf Terraform (pour déployer les machines , préciser les ressources etc …) possibilités template + full custom
    
- 1 pour edit le/les fichiers de conf Ansible (la config systèmes : création de users etc …) possibilités template + full custom

- 1 pour visualiser les logs / mettre en place des triggers pour des ID de logs précis
    
- 1 pour monitorer les VMs (à voir)
    
- 1 page de DOC
    

  


  
  
  
  
  
  

## INFRA

  

Machines Windows :

1 environnement AD avec : 

- 2 DC (répliqué / redondé)

- 1 poste client (pour generer les logs) (deply la machine)

* les machiens ephemeres pour se connecter en vpn (soit win soit linux)

- ...

  

Contenaires Docker : 

 1 contenaire pour Logstach
 
 1 contenaire ElasticSearch (indexation, filtre)

 un serveur web la vraie webapp
  

Trouver un moyen d’implementer kubernetes 

  
  
VLAN 1 : SRV WINDOWS (2 DC (redondés) + 1 DHCP et FILES ) 
VLAN 2 : Contenaires ? 
VLAN 3 : LOG et SOC (ip des contenaires qu on va créé 1 ou 2 ou plus on verra) 
VLAN 4 : les machines clientes 
VLAN 5 : sauvegardes? 
VLAN 6 : transfert de logs (les inputs pour la webapp) aura un VPN qui pointe dessus




## SYSTEME DE SAUVEGARDE!!!!!

save tout le proxmox
  







## LE LOG AGENT

  

3 Composants essentiels : 

  

- Un collecteur de logs 
    
- Un indexeur / filtre de logs
    
- Un viewer de logs intéractif (navigation etc)
    

  

Ajouter un système d’alertes par importance par mails et notifs (omg un appli mobile en plus ??? )


Choisir des indexs de logs précis pour créer des scripts de mitigation et les configurer à être déployés automatiquement dès qu’un event avec cet ID remonte




------------
![[Pasted image 20231018071936.png]]


    

AVANT DECEMBRE :

INSTALLER :
	Docker Linux (lancer sript commandes priomxo (template...) + terraform installé sur le docker +ansible installé sur le docker) + une commande de lancement (en bash ou python)

INFRA :
Firewall :  Pfesnse
	Securité : 
		- Accessible que en VLAN Management (à voir)
		- Accessible en LDAP (seuls les utilisateurs du groupe DC admin peuvent accèder) + on garde l'admin locale du pfsense
		- Redondance avec CARP (Master - Slave) Ip virtuelle à config sur les machines
		- Backup en cas d'incident
		- Anti DDOS 
		- Plugin Adresse MAC dans les logs (nom à trouver)
		- Règles en interne clean (par port) + description de la règle
		- PAS DE DHCP SUR LE PFSENSE
		...

VPN : 
	- OpenVPN sur proxmox (inconvénient : il faut ouvrir le port sur le VRAI ROUTEUR)
	- Gestion des users : créer sur le fichier depuis le serveur OpenVPN
	- Ajouter MFA (voir si c'est gratos)
	- Voir pour pointer le réseau de destination du réseau VPN

SRVWINDOWS :
	- ROLES : 
		- ADDS 
		- DHCP pour tous les VLANs
		- DNS 
		- WSUS (pour le serveur et les machines clientes Windows)
	- Sécurité sur le DC : 
		!!!! PARTIE A DOCUMENTER EN DETAILS POUR LE CLIENT !!!!
		- Disable NTLM et utiliser que Kerberos
		- Rendu du PA Pentest AD pour les mesures de sécurité contre les attaques de base
		- Voir pour LDAPS
		- LAPS pour gestion des admins locaux des postes clients (OVERKILL)
	- Automatiser le process ?
	- SYSMON

CONTENEURS :
	- APACHE2 + DB



APRES DECEMBRE :

Gestion des sauvegardes 

Intégrer LOGGEUR :
	- SYSLOG + PARSEUR PYTHON ou ELK 

WEB APP COMPLETE  :

Syteme d'authentification avec LDAPS (seul les membres du groupe IT peuvent reussir a s authentifier et seuls les membres du groupe DC-admins peuvent accéder à l interface en edit + MFA)

* 1 pour edit le/les fichiers de conf Terraform (pour déployer les machines , préciser les ressources etc …) possibilités template + full custom
    
- 1 pour edit le/les fichiers de conf Ansible (la config systèmes : création de users etc …) possibilités template + full custom

- 1 pour visualiser les logs / mettre en place des triggers pour des ID de logs précis
    
- 1 pour monitorer les VMs (à voir)
    
- 1 page de DOC