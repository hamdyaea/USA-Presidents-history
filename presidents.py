#!/usr/bin/python3

# Developer : Hamdy Abou El Anein

# This software is not finish I am working on it. I publish it to test it.

import json
import urllib.request
from easygui import *

def parser():
    urlData = ("https://raw.githubusercontent.com/hamdyaea/USA-Presidents-history/master/presidents.json")
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    presid = json.loads(data.decode(encoding))
    print(presid[0]["number"])
    print(presid[0]["president"])
    print(presid[0]["birth_year"])
    print(presid[0]["death_year"])
    print(presid[0]["took_office"])
    print(presid[0]["left_office"])
    print(presid[0]["party"])
    print(presid[0]["picture"])
    print(presid[0]["history"])
    print(len(presid))

    image = presid[0]["picture"]
    msg = presid[0]["president"]
    choices = ["Yes", "No", "No opinion"]
    reply = buttonbox(msg, image=image, choices=choices)



parser()