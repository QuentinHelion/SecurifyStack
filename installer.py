import sys
import os
import json
from proxmox_api import create_proxmox_api
from restoreFuncs import *
from runOnProxmox import runOnProxmox

def main():
    server = {
        "hostname" : os.getenv("PROXMOX_HOST"),
        "username" : "root",
        "password" : sys.argv[3]
    }
    commandToRun = "./getBkps.sh"
    runOnProxmox(server["hostname"], server["username"], server["password"], commandToRun)
#    if len(sys.argv) < 3:
#        print("Usage: python restore-mass-backups-lxc.py <api_token> backup_pairs.json")
#        sys.exit(1)
#
#    api_token = sys.argv[1]
#    json_file = sys.argv[2]
#
#    node = os.getenv("NODE")
#
#    proxmox = create_proxmox_api(api_token)
#
#    if proxmox:
#        try:
#            with open(json_file, 'r') as f:
#                backup_pairs = json.load(f)
#            
#            for backup_file, vmid in backup_pairs.items():
#                if "lxc" in backup_file:
#                    restore_lxc_backup(proxmox, backup_file, node, vmid)
#                elif "qemu" in backup_file:
#                    restore_qemu_backup(proxmox, backup_file, node, vmid)
#                else:
#                    print("Error unknown backup file")
#                    return 1
#        except FileNotFoundError:
#            print(f"File not found: {json_file}")
#        except json.JSONDecodeError as e:
#            print(f"Error parsing JSON in {json_file}: {e}")
#        except ValueError as e:
#            print(f"Invalid JSON format in {json_file}: {e}")

if __name__ == "__main__":
    main()
