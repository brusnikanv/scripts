import paramiko, sys


def connect_device():


    host = "10.16.50.61"
    port = 22
    username = "root"
    password = "ya_lublu_delat_karasa_311"

    command = "tail -n 10 /userdata/log/ace_device.log"

    print()

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

    with open('filename.txt', 'w') as f:
        sys.stdout = f
        stdin, stdout, stderr = ssh.exec_command(command)
        lines = stdout.readlines()
        print(lines)

if __name__ == "__main__":
        connect_device()
