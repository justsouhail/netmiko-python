from netmiko import ConnectHandler

switch_num = int(input("How many vlan: "))
USER = input('SSH Username: ')
PASS = input('SSH Password: ')
hostip = input('Switch IP: ')

while switch_num > 0:
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

    switch_vlan = int(input("give vlan id"))

    switch_int = (input("How many interfaces "))

    print('Configuring ethernet ' + x[1])
    
    # Configuring VLANs from 2 to 100
    acces = [
        f'int range {switch_int}' ,
        f'switchport mode access',
        f'switchport acces vlan {switch_vlan}',
        f'switchport port-security',
        f'switchport port-security violation shutdown'

            ]

    
    # Sending VLAN configuration
    output = myssh.send_config_set(acces)
    print(output)
    output_wr = myssh.send_command("write memory")
    print(f"Output of 'wr' on {hostname}:\n{output_wr}\n")
    
    switch_num -= 1
    print('Configured VLANs on ' + x[1])

input('Press ENTER To Continue')
