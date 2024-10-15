from netmiko import ConnectHandler

# Define the devices and their IP addresses
devices = {
    'sw1': '192.168.11.2',
    'sw-2': '192.168.11.11',
    'sw-3': '192.168.11.3',
    'sw-4': '192.168.11.12',
    'sw-5': '192.168.11.10'
}
destination_network = input("Enter the destination network  ")
subnet_mask = input("Enter the subnet mask (e.g., 255.255.255.0): ")
next_hop = input("Enter the next hop IP (e.g., 192.168.11.1): ")

# Common device parameters
common_params = {
    'device_type': 'cisco_ios',  # Assuming Cisco IOS devices
    'username': 'souhail',  # Replace with your username
    'password': '123',  # Replace with your password
    'secret': '',      # Replace with your secret
}

# VLAN configuration commands
commands = [
    f'ip route {destination_network} {subnet_mask} {next_hop}',
    'do show ip route'
]

# Iterate over the devices and configure VLANs
for device_name, ip_address in devices.items():
    # Update the device parameters with the specific IP address
    device_params = common_params.copy()
    device_params.update({'ip': ip_address})
    
    # Connect to the device
    print(f"Connecting to {device_name} at {ip_address}")
    net_connect = ConnectHandler(**device_params)
    net_connect.enable()
    
    # Send the VLAN configuration commands
    output = net_connect.send_config_set(commands)
    print(output)
    
    # Disconnect from the device
    net_connect.disconnect()
    print(f"Disconnected from {device_name}")

print("route configuration completed on all switches.")