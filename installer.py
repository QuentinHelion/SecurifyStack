import sys
import os
from restoreFuncs import restore_backups
from runOnProxmox import runOnProxmox

def main():
    if len(sys.argv) < 3:
        print("Usage: python installer.py <api_token> <backup_pairs.json> <proxmox_ssh_password>")
        sys.exit(1)
#=========================GET BAKCUP FILES FROM SFTP SERVER INTO THE PROXMOX SERVER=========================

    server = {
        "hostname" : os.getenv("proxmoxhost"),
        "username" : os.getenv("proxmoxuser"),
        "password" : sys.argv[3],
        "command" : os.getenv("command")
    }
    
    runOnProxmox(server["hostname"], server["username"], server["password"], server["command"])

#=========================RESTORE BACKUP FILES=========================

    api_token = sys.argv[1]
    json_file = sys.argv[2]
    node = os.getenv("NODE")

    restore_backups(api_token, json_file, node)

#=========================DEPLOY MACHINES=========================





if __name__ == "__main__":
    main()
