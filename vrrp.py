from netmiko import ConnectHandler
import sys

type = input("is it primary Y/N ")
if type=='Y' :
        prio=150
elif type=='N' :
        prio=15
else:
        print("Exiting the program.")
        sys.exit(1)  
USER = input('SSH Username: ')
PASS = input('SSH Password: ')
hostip = input('Switch IP: ')
number_vlan = int(input("how many virtual interfaces "))



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




while number_vlan > 0:
    int = input('give interface eg vlan 10 / e1/0 ')
    intip = input('virtual ip')
 
    

    config = [
                 f'  interface  {int}' ,
        f'vrrp 1 ip {intip} ',
        f'vrrp 1 priority {prio}' ,
        f'vrrp 1 preempt ' ,
        f'vrrp 1 authentication text 123',
                  
            ]

   

   
    output = myssh.send_config_set(config)
    print(output)
    output_wr = myssh.send_command("write memory")
    print(f"Output of 'wr' on {hostname}:\n{output_wr}\n")
    
    number_vlan -= 1
    print(f'Configured int {int}')

input('Press ENTER To Continue')
