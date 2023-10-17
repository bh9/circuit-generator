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
parser.add_argument('-H', '--holds', action='store_true')

args = parser.parse_args()

# get the exercises from the file
with open('exercises.json') as f:
    data=json.load(f)

# if the group flag is set, limit the exercises to only those in that group
if args.group:
    grouped_data=[x for x in data if args.group in x['groups']]
# otherwise, continue with all the exercises
else:
    grouped_data=data

# if the holds flag is set, continue with all the exercises
if args.holds:
    filtered_data=grouped_data
# otherwise, limit the exercises to only those which aren't holds
else:
    filtered_data=[x for x in grouped_data if not x['hold']]

# try to get a list of exercises of length args.exercises
try:
    exercises=(random.sample(filtered_data, args.exercises))
# if this is impossible (because there are <args.exercises (inc. 0) exercises), return all of them, along with an explanation of why there aren't as many exercises as requested 
except ValueError:
    print("There aren't that many exercises, returning all of them")
    exercises=filtered_data

# loop over the list of exercises generated above
for i in exercises:
    # if the -r flag is set, generate a rep count/time, otherwise, just print the exercise name
    if args.rep_count:
        repcount=args.rep_count*random.randint(i['ratio']['min'],i['ratio']['max'])
        # if the exercise is a hold, then there are no reps, so make the unit seconds instead of reps
        if i['hold']:
            unit = 'second'
        else:
            unit = 'rep'
        # print different messages for symmetric and asymmetric exercises, I get this question every session, so spell it out
        if i['double']:
            print(f'{i["name"]} for {repcount*2} {unit}s ({repcount} each side)')
        else:
            print(f'{i["name"]} for {repcount} {unit}s')
    else:
        print(i['name'])
