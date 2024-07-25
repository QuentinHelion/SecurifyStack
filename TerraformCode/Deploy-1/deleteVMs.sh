#!/bin/bash

# Set the directory containing the state files
STATE_DIR="States"

# Loop through each .tfstate file in the directory
for state_file in "$STATE_DIR"/*.tfstate; 
do
  # Check if the file exists
  if [ -f "$state_file" ]; then
    # Extract the filename without the directory
    filename=$(basename "$state_file")
    
    # Execute the terraform destroy command
    terraform destroy -state="$STATE_DIR/$filename" -auto-approve
    
    # Remove the state file
    rm "$STATE_DIR/$filename"
  else
    echo "No .tfstate files found in the directory."
  fi
done

