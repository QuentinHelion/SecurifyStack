import sys
from proxmoxer import ProxmoxAPI
import urllib3

urllib3.disable_warnings()

# Proxmox server details
proxmox_host = '192.168.1.169'
username = 'root@pam'
node = 'proxmox'
api_token = '574a4eb4-7f2f-4845-8e45-9506fc263a0f'
vmid = '9000'
newvmid = '1100'
newvmname = 'PyDeployment'

def create_proxmox_api():
    try:
        return ProxmoxAPI(proxmox_host, user=username, token_name='testDeploy', token_value=api_token, verify_ssl=False)
    except Exception as e:
        print(f"Error creating Proxmox API object: {e}")
        sys.exit(1)

def clone_vm(proxmox):
    try:
        proxmox.nodes(node).qemu(vmid).clone.create(
            newid=newvmid,
            name=newvmname
        )
        print(f"VM {vmid} cloned successfully. New VM ID: {newvmid}, Name: {newvmname}")
    except Exception as e:
        print(f"Failed to clone VM {vmid}. Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <api_token>")
        sys.exit(1)

    api_token = sys.argv[1]

    proxmox = create_proxmox_api()
    clone_vm(proxmox)

if __name__ == "__main__":
    main()

