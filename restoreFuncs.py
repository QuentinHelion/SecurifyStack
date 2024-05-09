import json
from proxmox_api import create_proxmox_api

def restore_lxc_backup(proxmox, backup_file, node, vmid):
    try:
        proxmox.nodes(node).lxc.create(
            node=node,
            ostemplate=backup_file,
            vmid=vmid,
            restore=1,
            storage='local-lvm',
        )
        print(f"Backup {backup_file} restored successfully.")
    except Exception as e:
        print(f"Failed to restore backup {backup_file}. Error: {e}")

def restore_qemu_backup(proxmox, backup_file, node, vmid):
    try:
        proxmox.nodes(node).qemu.create(
            archive=backup_file,
            vmid=vmid,
        )
        print(f"Backup {backup_file} restored successfully.")
    except Exception as e:
        print(f"Failed to restore backup {backup_file}. Error: {e}")

def restore_backups(api_token, node, json_file):
    proxmox = create_proxmox_api(api_token)

    if proxmox:
        try:
            with open(json_file, 'r') as f:
                backup_pairs = json.load(f)
            
            for backup_file, vmid in backup_pairs.items():
                if "lxc" in backup_file:
                    restore_lxc_backup(proxmox, backup_file, node, vmid)
                elif "qemu" in backup_file:
                    restore_qemu_backup(proxmox, backup_file, node, vmid)
                else:
                    print("Error unknown backup file")
                    return 1
        except FileNotFoundError:
            print(f"File not found: {json_file}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON in {json_file}: {e}")
        except ValueError as e:
            print(f"Invalid JSON format in {json_file}: {e}")
