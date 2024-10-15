#f = open("c:/Users/legion/Desktop/network automation/file2.txt", "x")
from netmiko import ConnectHandler


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


cmd =    'show run'

output = myssh.send_command(cmd)
with open(f'{device}.txt', 'w') as file:
   file.write(output)
print(output)
print('done')


