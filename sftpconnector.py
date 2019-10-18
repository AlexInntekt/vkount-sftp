hostname = "spaceport.avproiect.com"
username = "alex"
password = ""
path = '/home/alex/cargo'
 
#srv = pysftp.Connection(host="spaceport.avproiect.com", username="alex", private_key="/home/alex/.ssh/id_rsa")

import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password='', port=7020)
stdin, stdout, stderr = client.exec_command('ls -l')

sftp = client.open_sftp()
sftp.chdir(path)
print(sftp.listdir())

sftp.get('/home/alex/cargo/descarcama.txt','/home/alex/Desktop/descarcama.txt')
sftp.close()
client.close()