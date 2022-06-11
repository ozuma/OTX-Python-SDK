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

