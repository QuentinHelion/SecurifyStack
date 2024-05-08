## Run command :

python3 deploy-lxc.py {API-TOKEN-SECRET}

python3 deploy-vm.py {API-TOKEN-SECRET}

## Steps of the installer :

1. Add ssh key to sftp server
2. Download backups
3. Move backups to /var/lib/vz/dump
4. Restore backups
5. Clone for the templates


