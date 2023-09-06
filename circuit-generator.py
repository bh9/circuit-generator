#!/usr/bin/env python3

import json
import argparse
import random

parser = argparse.ArgumentParser(
        prog='circuit-generator',
        description='a small tool for generating circuits from a json structure')

parser.add_argument('-e', '--exercises', type=int, required=True)
parser.add_argument('-g', '--group')
parser.add_argument('-r', '--rep-count', type=int)

args = parser.parse_args()
with open('exercises.json') as f:
    data=json.load(f)

if args.group:
    filtered_data=[x for x in data if args.group in x['groups']]
else:
    filtered_data=data

try:
    exercises=(random.sample(filtered_data, args.exercises))
except ValueError:
    print("There aren't that many exercises, returning all of them")
    exercises=filtered_data

for i in exercises:
    if args.rep_count:
        repcount=args.rep_count*random.randint(i['ratio']['min'],i['ratio']['max'])
        if i['double']:
            print(f'{i["name"]} for {repcount*2} reps ({repcount} each side)')
        else:
            print(f'{i["name"]} for {repcount} reps')
    else:
        print(i['name'])
