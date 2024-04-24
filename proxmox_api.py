import os
from proxmoxer import ProxmoxAPI
from dotenv import load_dotenv
import urllib3

urllib3.disable_warnings()

load_dotenv()

def create_proxmox_api(api_token):
    proxmox_host = os.getenv("PROXMOX_HOST")
    username = os.getenv("USERNAME")
    token_id= os.getenv("TOKENID")
    print(username)
    try:
        return ProxmoxAPI(proxmox_host, user=username, token_name=token_id, token_value=api_token, verify_ssl=False)
    except Exception as e:
        print(f"Error creating Proxmox API object: {e}")
        return None

