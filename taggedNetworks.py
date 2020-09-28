'''
##############################
#
# Filename: taggedNetworks.py
#
# Title: Get Networks with Tags
# Meraki API version: v1
#
# Authored by: Henry Sandefur
# Date: 9/19/2020
# Version: 1.0.0
#
# Functions:
#    getNetworks()
#
##############################
'''

import requests
import json
import sys
from pprint import pprint

#get the org network IDs using a network tag 'api'
def getNetworks(apikey, orgID, tags):
    '''
    getNetworks():
    
    Returns a list of networks from network tags.

        Parameters:
            a (str): The api key
            b (str): The organization ID
            c (array): The array of tags

        Returns:
            networkList (array): The array of networks containing the network ID.

    '''

    t = 0
    tagsOutput =""
    while t< len(tags):
        tagsOutput += ("&tags[]=%s" % tags[t])
        t += 1
        
    url = ("https://api.meraki.com/api/v1/organizations/%s/networks?%s&tagsFilterType=withAllTags" % (orgID, tagsOutput))

    payload = None
    headers = {
      'Accept': '*/*',
      'Content-Type': 'application/json',
      'X-Cisco-Meraki-API-Key': str(apikey)
    }

    '''Response and encode it to json (comes as a string)'''
    response = requests.request("GET", url, headers=headers, data = payload)
    networkList = json.loads(response.text.encode('utf8'))

    return networkList

