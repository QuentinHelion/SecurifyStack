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
