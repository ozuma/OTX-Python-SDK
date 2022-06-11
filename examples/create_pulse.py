#!/usr/bin/python3

#  Simple example that prints the indicators from a pulse, then replaces them
import json
import os
from OTXv2 import OTXv2


# store OTX API key in environment variable OTX_API_KEY
API_KEY = os.getenv("OTX_API_KEY")

otx = OTXv2(API_KEY)

name='2022/06/xx Phishing Sites, xxx Card (Japan) abusing example.com Domain, at xx.xx.xx.xx'
indicators = [
{"indicator": "www.example.com", "title": "xxx Card", "role": "phishing", "type": "Hostname"}
]

response = otx.create_pulse(name=name ,public=True ,indicators=indicators ,tags=["phishing"] , references=[], targeted_countries=["Japan"] )

## Indicator Schema
#
# "indicators": {
#   "type": "array",
#   "items": {
#     "type": "object",
#     "additionalProperties": false,
#     "required": ["indicator", "type", "description"],
#     "properties": {
#       "indicator": {"type": "string"},
#       "type": {"type": "string"},
#       "title": {"type": "string"},
#       "description": {"type": "string"},
#       "expiration": {"type": "string", "format":  "date-time"},
#       "content": {"type": "string"},
#       "role": {"type": ["string", "null"], "enum": [
#         null, "", "scanning_host", "malware_hosting",
#         "command_and_control", "exploit_kit",
#         "malvertising", "phishing",
#         "bruteforce", "web_attack",
#         "exploit_source", "trojan", "rat",
#         "backdoor", "adware", "hacking_tool",
#         "ransomware", "worm", "macro_malware",
#         "domain_owner", "delivery_email",
#         "unknown", "file_scanning",
#         "memory_scanning", "hunting",
#         "pcap_scanning"
#       ]}
#     }
#   }
