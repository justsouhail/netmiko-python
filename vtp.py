from netmiko import ConnectHandler
import sys

type = input("server (s) or client (c)")
USER = input('SSH Username: ')
PASS = input('SSH Password: ')
hostip = input('Switch IP: ')
domain = input('domain: ')
password = input('pass: ')

Switch = {
        'device_type': 'cisco_ios',
        'ip': hostip,
        'username': USER,
        'password': PASS
    }
myssh = ConnectHandler(**Switch)
hostname = myssh.send_command('show run | inc host')
x = hostname.split()
device = x[1]

if  type == 's':
   
    server_type = input("primary ? [Y/N]")

    if server_type== 'Y' :

     config = [
        f'vtp domain {domain}' ,
        f'vtp  version 3',
        f'vtp password {password}',
        f'vtp mode server',
        f'exit',
        f'vtp primary force',
            ]

    elif server_type== 'N' :
     config = [
        f'vtp domain {domain}' ,
        f'vtp  version 3',
        f'vtp password {password}',
        f'vtp mode server',
            ]
    else:
        print("Exiting the program.")
        sys.exit(1)  

elif type== 'c' : 
    config = [
        f'vtp domain {domain}' ,
        f'vtp  version 3',
        f'vtp password {password}',
        f'vtp mode client',
            ]  

else:
        print("Exiting the program.")
        sys.exit(1)  
   
output = myssh.send_config_set(config)
print(output)
output_wr = myssh.send_command("write memory")
print(f"Output of 'wr' on {hostname}:\n{output_wr}\n")
    
    

input('Press ENTER To Continue')
