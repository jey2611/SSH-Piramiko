import paramiko


def startssh(host, user, passwd, commands):
 

    ssh_client = paramiko.SSHClient()

    # Must set the Host key policy as we haven't got the SSH key stored in Known Hosts
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    ssh_client.connect(hostname=host,
                       username=user,
                       password=passwd)

    # append output to a file
    output = open('terminaloutput.txt', 'a')

    output.write('\n ###################################')
    output.write('\n Connected to ')
    output.write(host)
    output.write('\n ###################################')

    stdin, stdout, stderr = ssh_client.exec_command(commands)
    outputstring = stdout.read()
    output.write(outputstring)
    output.write('\n')

    # terminate the SSH session
    ssh_client.close()



    return



netdevices = ['xxxxxx','xxxxx','xxxxxx']
username = 'xxxx'
password = 'xxxx'
command = ['xxxxxxx', 'xxxxxx']

#with open('devices.txt','r') as devices:


for device in netdevices:

    try:
        startssh(device, username, password, command)

    except Exception as error:
        print ('\n Authentication Failed or connection error for device ' + device)
    else:
        print (device + ' actions Completed without errors')

    
