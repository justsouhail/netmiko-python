from netmiko import ConnectHandler

devices = {
    # 'sw1': '192.168.11.50',
# 'sw2': '192.168.11.51',
# 'sw3': '192.168.11.52',
'sw4': '192.168.11.53',
# 'sw5': '192.168.11.54',
# 'sw6': '192.168.11.55',
# 'sw7': '192.168.11.56',

}
commands = []
while True:
    command = input("Enter command (or 'done' to finish): ")
    if command.lower() == 'done':
        break
    elif command.strip(): 
        commands.append(command)
        print(f"Command added: {command}")  


common_params = {
    'device_type': 'cisco_ios',  
    'username': 'souhail',  
    'password': '123',  
            'secret': '',     
}

for device_name, ip_address in devices.items():
    # Update the device parameters with the specific IP address
    device_params = common_params.copy()
    device_params.update({'ip': ip_address})
    
    # Connect to the device
    print(f"Connecting to {device_name} at {ip_address}")
    net_connect = ConnectHandler(**device_params)
    net_connect.enable()
    
    # Send the  configuration commands
    output = net_connect.send_config_set(commands)
    print(output)
    output_wr = net_connect.send_command("write memory")
    print(f"Output of 'wr' on {device_name}:\n{output_wr}\n")
    
    # Disconnect from the device
    net_connect.disconnect()
    print(f"Disconnected from {device_name}")

print( "completed ")