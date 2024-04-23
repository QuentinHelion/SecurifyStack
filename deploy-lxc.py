import sys
from proxmoxer import ProxmoxAPI
import urllib3

urllib3.disable_warnings()

# Proxmox server details
proxmox_host = '192.168.1.169'
username = 'root@pam'
node = 'proxmox'
api_token = '574a4eb4-7f2f-4845-8e45-9506fc263a0f'
tmpl_name = 'RTD-Debian'
new_ctid = '1101'
new_ct_name = 'CT-PyDeployment'

def create_proxmox_api():
    try:
        return ProxmoxAPI(proxmox_host, user=username, token_name='testDeploy', token_value=api_token, verify_ssl=False)
    except Exception as e:
        print(f"Error creating Proxmox API object: {e}")
        sys.exit(1)
def clone_lxc_template(proxmox):
    try:
        proxmox.nodes(node).lxc(1001).clone.create(
            newid=new_ctid,
            hostname=new_ct_name,
            full=true,
        )
        print(f"LXC template {tmpl_name} cloned successfully. New CT ID: {new_ctid}, Name: {new_ct_name}")
    except Exception as e:
        print(f"Failed to clone LXC template {tmpl_name}. Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <api_token> <tmpl_name> <new_ctid> <new_ct_name>")
        sys.exit(1)

    api_token = sys.argv[1]
    proxmox = create_proxmox_api()
    clone_lxc_template(proxmox)

if __name__ == "__main__":
    main()
