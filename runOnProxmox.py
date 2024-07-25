import paramiko

def runOnProxmox(host, username, password, command):
    ssh = paramiko.SSHClient()
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host,username=username, password=password)
        stdin,stdout,stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        if error:
            print(f"SSH command error: {error}")
            return False
        print(output)
        return True
    except paramiko.AuthenticationException:
        print("Authentication failed.")
        return False
    except paramiko.SSHException as err:
        print(f"SSH connection error: {err}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
    finally:
        ssh.close()
