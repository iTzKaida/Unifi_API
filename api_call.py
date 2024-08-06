import requests

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'INPUT_KEY_HERE'

# Define the headers
headers = {
    'X-API-KEY': api_key,
    'Accept': 'application/json'
}

# URL of the API endpoint
url = 'https://api.ui.com/ea/hosts'

# Define the mapping of controllers to update names
update_labels = [
    "Network-Update",
    "Protect-Update",
    "Access-Update",
    "Talk-Update",
    "Connect-Update",
    "Inner Space Update"
]

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
   
    data = response.json()
    
    # Prepare the list of hostnames, device shortnames, and their update statuses
    host_info = []
    for host in data['data']:
        hostname = host['reportedState'].get('hostname', 'N/A')
        device_shortname = host.get('hardware', {}).get('shortname', 'N/A')
        controllers = host['reportedState'].get('controllers', [])
        
        # Collect update statuses and map them to their labels
        update_statuses = []
        for i, controller in enumerate(controllers):
            update_available = controller.get('updateAvailable', 'N/A')
            if i < len(update_labels):
                label = update_labels[i]
                update_statuses.append(f"{label}: {update_available}")
        
        
        update_status_str = ', '.join(update_statuses)
        host_info.append(f"Hostname: {hostname}, Device Shortname: {device_shortname}, {update_status_str}")
    
    # Save the host information to a text file
    with open('host_info.txt', 'w') as file:
        for info in host_info:
            file.write(info + '\n')
else:
    print(f"Request failed with status code {response.status_code}")