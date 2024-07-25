import sys
import os
from restoreFuncs import restore_backups
from deployFuncs import deploy_machines
from runOnProxmox import runOnProxmox
from checkTemplates import check_templates

def main():
    if len(sys.argv) < 4:
        print("Usage: python installer.py <api_token> <proxmox_ssh_password> <backups_file.json> <clones_file.json>")
        sys.exit(1)

    api_token = sys.argv[1]
    backups_file = sys.argv[3]
    clones_file = sys.argv[4]
    node = os.getenv("NODE")

#=========================GET BAKCUP FILES FROM SFTP SERVER INTO THE PROXMOX SERVER=========================

    server = {
        "hostname" : os.getenv("PROXMOXHOST"),
        "username" : os.getenv("PROXMOXUSER"),
        "password" : sys.argv[2],
        "command" : os.getenv("COMMAND")
    }   

#    if not runOnProxmox(server["hostname"], server["username"], server["password"], server["command"]):
#        print("Failed to execute command on Proxmox server.")
#        sys.exit(1)

    check_templates(api_token, node, backups_file)
#=========================RESTORE BACKUP FILES=========================

    try:
        restore_backups(api_token, node, backups_file)
    except Exception as e:
        print(f"Error restoring backups: {e}")
        sys.exit(1)


#=========================DEPLOY MACHINES=========================
    
    try:
        deploy_machines(api_token, node, clones_file)
    except Exception as e:
        print(f"Error deploying machines: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()
