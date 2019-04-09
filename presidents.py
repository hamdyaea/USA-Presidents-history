#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein

# This software is not finish I am working on it. I publish it to test it.

# Make changes to the json file only with pycharm and json viewer.
# The data can take time to be fully updated on the server-side. (raw json).

import json
import urllib.request
from easygui import *
import wget
import os
import sys

key = 0

def first():
    global key

    if key > (len(presid)-1):
        key = 0

    filepath = "president.png"

    if os.path.exists(filepath):
        os.remove(filepath)

    url = presid[key]["picture"]
    filename = wget.download(url, out="president.png")


    image = "president.png"
    msg = ((presid[key]["president"])\
            +str("\n")+str("President number : ")+str(presid[key]["number"])\
            +str("\n")+str("Political party : ")+str(presid[key]["party"])\
            +str("\n")+str("Birth year : ")+str(presid[key]["birth_year"])+str(" Death year : ")+str(presid[key]["death_year"])\
            +str("\n")+str("Took office : ")+str(presid[key]["took_office"])+str(" Left office : ")+str(presid[key]["left_office"])\
            +str("\n")+str(presid[key]["history"]))

    if key < (len(presid)-1):
        choices = ["Next"]
    else:
        choices = ["Begin","Quit"]

    reply = buttonbox(msg, image=image, choices=choices)

    if reply == "Next":
        key = key + 1
        first()
    elif reply == "Begin":
        key = 0
        parser()
    elif reply == "president.png":
        key = key + 1
        first()
    else:
        sys.exit(0)

def parser():
    global presid
    url = "https://raw.githubusercontent.com/hamdyaea/USA-Presidents-history/master/pictures/presidentseal.png"
    filepath = "presseal.png"
    if os.path.exists(filepath):
        os.remove(filepath)
    filename = wget.download(url, out="presseal.png")
    image = "presseal.png"
    msg = "The purpose of the program is to introduce a little more the history of the presidents of the states units. The data will be changed when there is a change in the presidency of the United States. Developer - Author : Hamdy Abou El Anein"
    choices = ["Continue"]
    reply = buttonbox(msg, image=image, choices=choices)
    print(reply)
    if reply == "Continue" or "presidenseal.png":
        urlData = ("https://raw.githubusercontent.com/hamdyaea/USA-Presidents-history/master/presidents.json")
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        presid = json.loads(data.decode(encoding))
    else:
        sys.exit(0)


    first()

parser()