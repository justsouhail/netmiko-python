from netmiko import ConnectHandler
import sys


USER = input('SSH Username: ')
PASS = input('SSH Password: ')
hostip = input('Switch IP: ')


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

switch_int = (input("How many interfaces "))
   
    


config = [
        f'int range {switch_int}' ,
        f'switchport trunk encapsulation dot1q',
        f'switchport mode trunk',

            ]  


output = myssh.send_config_set(config)
print(output)
output_wr = myssh.send_command("write memory")
print(f"Output of 'wr' on {hostname}:\n{output_wr}\n")
    
    

input('Press ENTER To Continue')
