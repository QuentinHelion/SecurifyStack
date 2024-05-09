import json
import time
from proxmox_api import create_proxmox_api
def clone_lxc_template(proxmox, node, tmpl_ctid, new_ctid, new_ctname):
    try:
        proxmox.nodes(node).lxc(tmpl_ctid).clone.create(
            newid=int(new_ctid),
            hostname=new_ctname,
            full=0
        )
        print(f"LXC template {tmpl_ctid} cloned successfully. New CT ID: {new_ctid}, Name: {new_ctname}")
        time.sleep(3)
    except Exception as e:
        print(f"Failed to clone LXC template {tmpl_ctid}. Error: {e}")

def clone_vm_template(proxmox, node, tmpl_vmid, new_vmid, new_vmname):
    try:
        proxmox.nodes(node).qemu(int(tmpl_vmid)).clone.create(
            newid=int(new_vmid),
            name=new_vmname,
        )
        print(f"VM template {tmpl_vmid} cloned successfully. New VM ID: {new_vmid}, Name: {new_vmname}")
    except Exception as e:
        print(f"Failed to clone VM template {tmpl_vmid}. Error: {e}")

def deploy_machines(api_token, node, json_file):
    proxmox = create_proxmox_api(api_token)
    try:
        with open(json_file, 'r') as f:
            json_data = json.load(f)
            templates = json_data["templates"]
            for template in templates:
                tmpl_id = template["tmpl_id"]
                num_clones = template["num_clones"]
                tmpl_type = template["type"]
                names = template["names"]
                name_prefix = names["prefix"]
                custom_names = names["custom"]
                clone_ids = template["clone_ids"]
                start_number = clone_ids["start_number"]
                
                if clone_ids["custom"] is not None:
                    clone_ids_list = clone_ids["custom"]
                else:
                    clone_ids_list = [str(start_number + i) for i in range(num_clones)]
                
                for i in range(num_clones):
                    new_id = clone_ids_list[i]
                    
                    if custom_names:
                        new_name = f"{custom_names[i]}"
                    else:
                        new_name = f"{name_prefix}{i+1}"
                    print(new_name) 
                    if tmpl_type == "LXC":
                        clone_lxc_template(proxmox, node, tmpl_id, new_id, new_name)
                    elif tmpl_type == "VM":
                        clone_vm_template(proxmox, node, tmpl_id, new_id, new_name)
                    else:
                        print("Unknown template type.")
                    
                    print(f"Deployed {tmpl_type} template {tmpl_id} clone {i+1} with ID {new_id} and name {new_name}")
    except FileNotFoundError:
        print(f"File not found: {json_file}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON in {json_file}: {e}")
    except Exception as e:
        print(f"Error deploying machines: {e}")
