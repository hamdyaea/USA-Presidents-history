#!/usr/bin/python3

# Developer : Hamdy Abou El Anein

# This software is not finish I am working on it. I publish it to test it.

import json
from easygui import *

def parser():
    with open('https://raw.githubusercontent.com/hamdyaea/USA-Presidents-history/master/presidents.json') as json_file:
        data = json.load(json_file)
        print(data[1]["number"])
        print(data[1]["president"])
        print(data[1]["birth_year"])
        print(data[1]["death_year"])
        print(data[1]["took_office"])
        print(data[1]["left_office"])
        print(data[1]["party"])
        #print(data[0]["picture"])
        #print(data[0]["history"])
        print(len(data))

parser()