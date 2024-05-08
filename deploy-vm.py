import sys
import os
from proxmox_api import create_proxmox_api

# Proxmox server details
#vmid = '9000'
#newvmid = '1100'
#newvmname = 'PyDeployment'

def clone_vm(proxmox, vmid, newvmid, newvmname, node):
    try:
        proxmox.nodes(node).qemu(vmid).clone.create(
            newid=newvmid,
            name=newvmname
        )
        print(f"VM {vmid} cloned successfully. New VM ID: {newvmid}, Name: {newvmname}")
    except Exception as e:
        print(f"Failed to clone VM {vmid}. Error: {e}")

def main():
    if len(sys.argv) < 4:
        print("Usage: python script_name.py <api_token> <vmid> <newvmid> <newvmname>")
        sys.exit(1)

    api_token = sys.argv[1]
    vmid = sys.argv[2] 
    newvmid = sys.argv[3] 
    newvmname = sys.argv[4] 

    node = os.getenv("NODE")

    proxmox = create_proxmox_api(api_token)
    clone_vm(proxmox, vmid, newvmid, newvmname, node)

if __name__ == "__main__":
    main()

