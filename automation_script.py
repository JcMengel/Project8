from ncclient import manager
from ncclient.operations import RPCError

# Define device details
device = {
    'host': '192.168.37.128',
    'port': 830,
    'username': 'cisco',
    'password': 'cisco123!',
}

# NETCONF RPC to retrieve the running-config
get_running_config_rpc = """
<get-config>
    <source>
        <running/>
    </source>
</get-config>
"""

# NETCONF RPC to make configuration changes
edit_config_rpc = """
<edit-config>
    <!-- Your configuration changes go here -->
</edit-config>
"""

# Function to execute NETCONF operations
def execute_netconf_operation(rpc):
    with manager.connect(**device) as m:
        try:
            response = m.edit_config(target='running', config=rpc)
            return response
        except RPCError as e:
            print(f"NETCONF operation failed: {e}")

# Verify current running-config
running_config_response = execute_netconf_operation(get_running_config_rpc)

# Make three changes to the configuration
edit_config_response = execute_netconf_operation(edit_config_rpc)

# Verify the changes
verify_changes_response = execute_netconf_operation(get_running_config_rpc)

# Verify the new running-config
verify_new_running_config_response = execute_netconf_operation(get_running_config_rpc)

# Send notification to WebEx SE Teams group
# (Implement WebEx Teams API integration or use a library like 'webexteamssdk')

# Display results or handle errors as needed
print("Running Config:", running_config_response)
print("Config Changes:", edit_config_response)
print("Verify Changes:", verify_changes_response)
print("New Running Config:", verify_new_running_config_response)

from webexteamssdk import WebexTeamsAPI

# Function to send notification to WebEx Teams group
def send_webex_teams_notification(message):
    # Initialize WebEx Teams API
    api = WebexTeamsAPI('YWQzYjljYjItMjg2NC00ZTQ5LWE0NGYtMmRkM2E0Y2RiYTFhN2ZjOTI3MTMtMzli_P0A1_18f592ad-9e27-4e21-bdda-c79873a7f7cd')

    # Define the group ID or space ID for the WebEx Teams group
    group_id = '1'

    # Send message to the group
    api.messages.create(roomId=group_id, text=message)

# Send notification
send_webex_teams_notification("Configuration update completed.")
