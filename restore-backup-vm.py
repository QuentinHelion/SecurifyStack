import sys
import os
from proxmox_api import create_proxmox_api

def restore_vm_backup(proxmox, backup_file, node, vmid):
    try:
        proxmox.nodes(node).qemu.create(
            archive=backup_file,
            vmid=vmid,
        )
        print(f"Backup {backup_file} restored successfully.")
    except Exception as e:
        print(f"Failed to restore backup {backup_file}. Error: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python restore_backup.py <api_token> <backup_file>")
        sys.exit(1)

    api_token = sys.argv[1]
    backup_file = sys.argv[2]
    vmid = sys.argv[3] 
    
    node = os.getenv("NODE")

    proxmox = create_proxmox_api(api_token)
    
    if proxmox:
        restore_vm_backup(proxmox, backup_file, node, vmid)

if __name__ == "__main__":
    main()

