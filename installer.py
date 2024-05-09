import sys
import os
from restoreFuncs import restore_backups
from deployFuncs import deploy_machines
from runOnProxmox import runOnProxmox

def main():
    if len(sys.argv) < 4:
        print("Usage: python installer.py <api_token> <proxmox_ssh_password> <backups_file.json> <clones_file.json>")
        sys.exit(1)
#=========================GET BAKCUP FILES FROM SFTP SERVER INTO THE PROXMOX SERVER=========================

    server = {
        "hostname" : os.getenv("proxmoxhost"),
        "username" : os.getenv("proxmoxuser"),
        "password" : sys.argv[2],
        "command" : os.getenv("command")
    }
    
#    runOnProxmox(server["hostname"], server["username"], server["password"], server["command"])

#=========================RESTORE BACKUP FILES=========================

    api_token = sys.argv[1]
    backups_file = sys.argv[3]
    clones_file = sys.argv[4]
    node = os.getenv("NODE")

#    restore_backups(api_token, node, backups_file)

#=========================DEPLOY MACHINES=========================
    
    deploy_machines(api_token, node, clones_file)   




if __name__ == "__main__":
    main()
