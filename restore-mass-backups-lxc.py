import sys
import os
import json
from proxmox_api import create_proxmox_api

def restore_vm_backup(proxmox, backup_file, node, vmid):
    try:
        proxmox.nodes(node).lxc.create(
            node=node,
            ostemplate=backup_file,
            vmid=vmid,
            restore=1,
            storage='local-lvm',
        )
        print(f"Backup {backup_file} restored successfully to VM {vmid}.")
    except Exception as e:
        print(f"Failed to restore backup {backup_file} to VM {vmid}. Error: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python restore-lxc.py <api_token> backup_pairs.json")
        sys.exit(1)

    api_token = sys.argv[1]
    json_file = sys.argv[2]

    node = os.getenv("NODE")

    proxmox = create_proxmox_api(api_token)

    if proxmox:
        try:
            with open(json_file, 'r') as f:
                backup_pairs = json.load(f)
            
            for backup_file, vmid in backup_pairs.items():
                restore_vm_backup(proxmox, backup_file, node, vmid)
        except FileNotFoundError:
            print(f"File not found: {json_file}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON in {json_file}: {e}")
        except ValueError as e:
            print(f"Invalid JSON format in {json_file}: {e}")

if __name__ == "__main__":
    main()

