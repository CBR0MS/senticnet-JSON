"""
Convert the senticnet python array of values to JSON

Tested and works with SenticNet5 and SenticNet4 python dictionaries
downloaded from http://sentic.net/downloads/

For usage information, see readme.md 

MIT License
"""

import json 
import copy
import argparse
from senticnet5 import * # the senticnet5 python array 

parser = argparse.ArgumentParser()
parser.add_argument("-p", action='store_true', help="pretty print to JSON file ")
parser.add_argument("-d", nargs='+', help="delete specific values from the senticnet5 dictionary")
parser.add_argument('--values', action='store_true', help='print value labels from the senticnet5 dictionary')
args = parser.parse_args()

# value labels in the senticnet array 
senticVals = ['pleasantness_value', 'attention_value', 'sensitivity_value','aptitude_value', 'primary_mood', 'secondary_mood', 'polarity_label', 'polarity_value', 'semantics1', 'semantics2', 'semantics3', 'semantics4', 'semantics5'] 

if args.values:
    for i in range(len(senticVals)):
        print("index: ", i, "\tvalue: ", senticVals[i])
    print("to delete a section from the senticnet5 dictionary, use the command -d followed by indices of this array")
else:
    # make a direct json copy of the senticnet5 array
    print("writing json from senticnet... ")
    with open('senticnet5.json', 'w') as outfile:
        json.dump(senticnet, outfile)

# pretty print files given argument 
if args.p:
    print("pretty printing json to file... ")
    obj = None
    with open('senticnet5.json') as source:
        obj = json.load(source)
        outfile = open('senticnet5.json', 'w')
        outfile.write(json.dumps(obj, indent=4, sort_keys=True))
        outfile.close()

# check if there are sections to delete
if args.d:
    args.d = list(set(map(int, args.d)))
    args.d.sort()
    # check that arguments are valid
    for arg in args.d:
        if (int(arg) > 12 or int(arg) < 0):
            raise ValueError("indices to delete must be between 0 and 12, inclusive")

    senticnet5_smaller = copy.deepcopy(senticnet)

    # delete specified indices 
    print ("deleting sections: ")
    indicesToShow = copy.deepcopy(args.d)
    for i in range(len(args.d)):
        index = indicesToShow.pop(0)
        print("index: ", index, "\tvalue: ", senticVals[index])
    print("from senticnet to make senticnet-smaller... ")
    for word in senticnet5_smaller.values():
        indicesToDelete = copy.deepcopy(args.d)
        for i in range(len(indicesToDelete)):
            indexToDelete = indicesToDelete.pop()
            word.pop(int(indexToDelete))

    # make a json copy of the smaller array
    print("writing json from senticnet-smaller... ")
    with open('senticnet5-smaller.json', 'w') as outfile:
        json.dump(senticnet5_smaller, outfile)

    # pretty print smaller JSON 
    if args.p:
        print("pretty printing json to file... ")
        with open('senticnet5-smaller.json') as source:
            obj = json.load(source)
            outfile = open('senticnet5-smaller.json', 'w')
            outfile.write(json.dumps(obj, indent=4, sort_keys=True))
            outfile.close()

print("done")

