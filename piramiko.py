import paramiko


#Function called "startssh"

def startssh(host, user, passwd, commands):

  # Create Paramiko Session
  ssh_client = paramiko.SSHClient()

  # Must set the Host key policy as we haven't got the SSH key stored in Known Hosts
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  # Connect to Device
  ssh_client.connect(hostname=host,
                   username=user,
                   password=passwd)

  # if any error the Paramiko will throw an exception, so not checking for errors

  # append output to a file
  output = open('terminaloutput.txt', 'a')
  
  # Making the Output more readable by using these lines as delimiter for each device
  output.write('\n ###################################')
  output.write('\n Connected to ')
  output.write(host)
  output.write('\n ###################################')
  output.write('\n' + 'Running CLI:')
  output.write(commands)
  output.write('\n ###################################')

  # sending the CLI commands to the device
  stdin, stdout, stderr = ssh_client.exec_command(commands)
  outputstring = stdout.read()
  output.write(outputstring)
  output.write('\n')

  # terminate the SSH session
  ssh_client.close()
  return

#End of function  "startssh" 


# Device IP addresses in a list 
netdevices = ['192.168.0.1','192.168.0.1']

#username used to login  
username = 'cisco'

#password for username 
password = 'cisco'

# List of commands to run  
command = ['show ip route','show ip int brie']

# Iterate through the list of devices with the list of commands to execute by calling function "startssh"
for device in netdevices:
    for cmd in command:
        startssh(device, username, password, cmd)
