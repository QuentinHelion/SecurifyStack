#!/bin/bash

# Check if the user has provided at least one argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <id1,id2,...,idN>"
    exit 1
fi

# Function to classify and list VMs and LXCs to be deleted
classify_and_list() {
    local ids=("$@")
    local vms_to_delete=()
    local lxcs_to_delete=()
    local unrecognized_ids=()

    # Get lists of all VMs and LXCs
    mapfile -t all_vms < <(qm list | awk 'NR>1 {print $1}')
    mapfile -t all_lxcs < <(pct list | awk 'NR>1 {print $1}')

    # Classify IDs
    for id in "${ids[@]}"; do
        if [[ " ${all_vms[*]} " =~ " $id " ]]; then
            vms_to_delete+=("$id")
        elif [[ " ${all_lxcs[*]} " =~ " $id " ]]; then
            lxcs_to_delete+=("$id")
        else
            unrecognized_ids+=("$id")
        fi
    done

    # Print the list of VMs and LXCs to be deleted
    if [ ${#vms_to_delete[@]} -ne 0 ]; then
        echo "VMs to be deleted: ${vms_to_delete[*]}"
    fi
    if [ ${#lxcs_to_delete[@]} -ne 0 ]; then
        echo "LXCs to be deleted: ${lxcs_to_delete[*]}"
    fi
    if [ ${#unrecognized_ids[@]} -ne 0 ]; then
        echo "Unrecognized IDs: ${unrecognized_ids[*]}"
    fi

    # Store lists globally for later use
    VM_IDS_TO_DELETE=("${vms_to_delete[@]}")
    LXC_IDS_TO_DELETE=("${lxcs_to_delete[@]}")
    UNRECOGNIZED_IDS=("${unrecognized_ids[@]}")
}

# Function to delete VM or LXC based on ID
delete_by_id() {
    local id=$1
    local type=$2

    if [ "$type" == "vm" ]; then
        echo "Deleting VM with ID $id"
        qm destroy "$id"
    elif [ "$type" == "lxc" ]; then
        echo "Deleting LXC with ID $id"
        pct destroy "$id"
    else
        echo "Error: Unrecognized type $type for ID $id"
    fi
}

# Ask for user confirmation
ask_confirmation() {
    local vms="${1:-none}"
    local lxcs="${2:-none}"
    local unrecognized="${3:-none}"
    echo "You are about to delete the following VMs/LXCs:"
    echo "VMs to be deleted: ${vms}"
    echo "LXCs to be deleted: ${lxcs}"
    if [[ "${unrecognized}" != "none" ]]; then
        echo "Unrecognized IDs: ${unrecognized}"
    fi
    read -r -p "Are you sure you want to proceed? (yes/no) " response
    case "$response" in
        [yY][eE][sS]|[yY])
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

# Split the input into an array based on commas
IFS=',' read -r -a ids <<< "$1"

# Classify and list VMs and LXCs to be deleted
classify_and_list "${ids[@]}"

# Check if there are valid IDs to delete
if [ ${#VM_IDS_TO_DELETE[@]} -eq 0 ] && [ ${#LXC_IDS_TO_DELETE[@]} -eq 0 ]; then
    if [ ${#UNRECOGNIZED_IDS[@]} -gt 0 ]; then
        echo "Error: No VM or LXC found matching the IDs: ${UNRECOGNIZED_IDS[*]}"
    else
        echo "Error: No valid VM or LXC IDs provided."
    fi
    exit 1
fi

# Confirm deletion
vm_ids_string="${VM_IDS_TO_DELETE[*]}"
lxc_ids_string="${LXC_IDS_TO_DELETE[*]}"
unrecognized_ids_string="${UNRECOGNIZED_IDS[*]}"

if ask_confirmation "$vm_ids_string" "$lxc_ids_string" "$unrecognized_ids_string"; then
for id in "${VM_IDS_TO_DELETE[@]}"; do
delete_by_id "$id" "vm"
done
for id in "${LXC_IDS_TO_DELETE[@]}"; do
delete_by_id "$id" "lxc"
done
else
echo "Deletion cancelled."
fi
