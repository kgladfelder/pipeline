import argparse
import os.path
import json
import logging

def main():
        logger = logging.getLogger("pipeline")
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler("pipeline.log")
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.info("Starting Program")
        parser = argparse.ArgumentParser(description='CSV to JSON converter.')
        parser.add_argument('f', metavar='FILES', type=argparse.FileType('r'), nargs='+')
        args = parser.parse_args()
        logger.info("Arguments Parsed")
        for file in args.f:
                if not file.name.endswith('.csv'):
                        print( 'Invalid file format:', file.name )
                        logger.info( 'Invalid file format:', file.name )
                        continue
                logger.info("Opening file: {}".format(file.name))
                output = {}
                output["Users"] = []
                outputFilename = file.name[:-4] + '.json'
                for line in file:
                        line = line.strip()
                        if line == 'id,first_name,last_name,email':
                                continue
                        logger.debug("{}".format(line))
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
                logger.info("Finished file: {}".format(file.name))

main()