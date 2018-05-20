import argparse
import os.path
import json

def main():
        parser = argparse.ArgumentParser(description='CSV to JSON converter.')
        parser.add_argument('f', metavar='FILES', type=argparse.FileType('r'), nargs='+')
        args = parser.parse_args()
        
        for file in args.f:
                if not file.name.endswith('.csv'):
                        print( 'Invalid file format:', file.name)
                        continue
                output = {}
                output["Users"] = []
                outputFilename = file.name[:-4] + '.json'
                for line in file:
                        line = line.strip()
                        if line == 'id,first_name,last_name,email':
                                continue
                        lineSplit = line.split(',')
                        if len(lineSplit) == 4:
                                user = {}
                                user["ID"] = lineSplit[0]
                                user["First Name"] = lineSplit[1]
                                user["Last Name"] = lineSplit[2]
                                user["Email"] = line[3]
                                output["Users"].append(user)
                with open(outputFilename, 'w') as outfile:
                        json.dump(output, outfile)

main()