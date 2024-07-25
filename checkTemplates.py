import json
from proxmox_api import create_proxmox_api

def check_templates(api_token, node, json_file):
    proxmox = create_proxmox_api(api_token)
    if proxmox:
        try:
             # Get the list of all VMs and templates on the node
            all_vms = proxmox.nodes(node).qemu.get() + proxmox.nodes(node).lxc.get()
            # Filter out the templates
            templates = [vm for vm in all_vms if vm['template'] == 1]
            #print(all_vms)
            # Extract the names of the templates
            templatesList = {vm['vmid'] for vm in templates}
            template_names = {int(item) for item in templatesList}
            with open(json_file, 'r') as f:
                backup_pairs = json.load(f)

            templatesRestored = set(backup_pairs.values())
            templates_to_check = {int(item) for item in templatesRestored}

            # Check which templates in templates_to_check are present on the Proxmox server
            missing_templates = [template for template in templates_to_check if template not in template_names]
            present_templates = [template for template in templates_to_check if template in template_names]
            
            # Display the results
            if present_templates:
                print("The following templates are present:")
                for template in present_templates:
                    print(f"[ \u2714\ufe0e ] {template}")
            else:
                print("None of the specified templates are present.")
            
            if missing_templates:
                print("The following templates are missing:")
                for template in missing_templates:
                    print(f"[ \u274c] {template}")
            else:
                print("All specified templates are present on the Proxmox server.")

        except Exception as e:
            print(f"An error occurred: {e}")

