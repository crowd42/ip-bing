#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import requests

# ip_bing take 3 arguments, the last two are optional
parser = argparse.ArgumentParser(
    description="Find websites hosted on the same IP address")
parser.add_argument('-i', '--ip', help="The IP address of the web server")
parser.add_argument('-c', '--count', help='Number of results to return')
parser.add_argument('-f', '--file', help='Save the output into a text file')
parser.add_argument(
    '-o',
    '--offset',
    help='start in results number x, default: 0')
args = parser.parse_args()

if not args.ip:
    parser.print_help()
    exit()
# Subscription key which provides access to this API.
headers = {'Ocp-Apim-Subscription-Key': '182d8d5d520f40b5a5ec47ab9376d656'}

# Request URL
url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

# The keyword (dork) to pass to bing
keyword = 'ip:' + args.ip
payloads = {'q': keyword, 'count': args.count, 'offset': args.offset}
response = requests.get(url, params=payloads, headers=headers)

# Get the response as json content
content = response.json()
data = content['webPages']['value']
for i in range(len(data)):
    print(data[i]['url'])
    # We also the save output as file in the current directory, so we can use
    # later with other programs for example
    try:
        with open(args.file, 'a') as f:
            f.write(data[i]['url'] + '\n')
    except TypeError:
        pass
