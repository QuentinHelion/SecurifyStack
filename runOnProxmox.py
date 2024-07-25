import paramiko

def runOnProxmox(host, username, password, command):
    ssh = paramiko.SSHClient()
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host,username=username, password=password)
        stdin,stdout,stderr = ssh.exec_command(command)
        print(stdout.read().decode())
    except paramiko.AuthenticationException:
        print("Auth failed")
    except paramiko.SSHException as err:
        print(f"Error setting SSH connection : {err}")
    finally:
        ssh.close()

