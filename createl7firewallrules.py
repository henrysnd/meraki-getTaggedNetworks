'''
##############################
#
# Filename: l7firewallrules-v1.py
#
# Title: Set Syslog Server
# Meraki API version: v1
#
# Authored by: Henry Sandefur
# Date: 3/13/2024
# Version: 1.0.0
#
# Purpose: 
#   Sets the layer 7 firewall rules
#
#
##############################
'''

import sys
import requests
import json
import taggedNetworks


# ==VARIABLES==
orgID = "" #YOUR ORG ID
apikey = "" #YOUR API KEY
tags = ["tag1", "tag2"]


# ==CODE EXECUTION==

#get our tagged networks
networks = taggedNetworks.getNetworks(apikey, orgID, tags)


#iterate through the network IDs and make the changes needed
for network in networks:

    #TODO -- Put whatever here, we have a list of networks with tags!!!


    url = ("https://api.meraki.com/api/v1/networks/%s/appliance/firewall/l7FirewallRules" % network['id'])

    payload = '''{
        "rules": [
            {
                "policy": "deny",
                "type": "ipRange",
                "value": "10.0.0.0/23"
            }
        ]
    }'''

    headers = {
        "Authorization": "Bearer " + str(apikey),
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.request('PUT', url, headers=headers, data = payload)

    print(network['name'] + ": ")

    print(response.text.encode('utf8'))



