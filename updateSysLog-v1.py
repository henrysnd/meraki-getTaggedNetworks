'''
##############################
#
# Filename: updateSysLog-v1.py
#
# Title: Set Syslog Server
# Meraki API version: v1
#
# Authored by: Henry Sandefur
# Date: 9/29/2020
# Version: 1.0.0
#
# Purpose: 
#   Sets the syslog server for netflow (5tuple) data and security events
#
#
##############################
'''


import requests
import json
import sys
import taggedNetworks


# ==VARIABLES==
orgID = "" #YOUR ORG ID
apikey = "" #YOUR API KEY
tags = ["tag1", "tag2", "tag3"]
host = "" #YOUR SYSLOG IP

# ==CODE EXECUTION==

#get our tagged networks
networks = taggedNetworks.getNetworks(apikey, orgID, tags)


#iterate through the network IDs and make the changes needed
for network in networks:

    #TODO -- Put whatever here, we have a list of networks with tags!!!

    url = ("https://api.meraki.com/api/v1/networks/%s/syslogServers" % network['id'])

    payload = '''{
        "servers": [
            {
                "host": "%s",
                "port": 1514,
                "roles": [
                    "Flows",
                    "URLs",
                    "Security events",
                    "Appliance event log",
                    "Air Marshal events",
                    "Wireless event log",
                    "Switch event log"
                ]
            }
        ]
    }''' % host

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": str(apikey)
    }

    response = requests.request('PUT', url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

