#!/usr/bin/env python3

import zipfile
import simplejson as json
import os
import argparse

dir_path = os.path.dirname(os.path.realpath(__file__))
directory = './'

def read_zip_file(fullZipPath):
    """ Extract all ZIP file content """
    with zipfile.ZipFile(fullZipPath) as zfile:
	# Show ZIP file content
        zfile.printdir()

        print('Extracting all files')
        zfile.extractall()
        print('Done!')

def update_json_file(jsonFileName, key, value):
    """ Update in Json file.
        Input as argument file name, key tu update and value of the key
    """
    with open(jsonFileName, "r+") as jsonFile:
        data = json.load(jsonFile)

        tmp = data[key]
        data[key] = value

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile, sort_keys=True, indent=2)
        jsonFile.truncate()

def get_all_file_paths(directory):
    """ Get all files path in the current directory """
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths

def prepareZipFile(directory, newFileToZip):
    """ Get all files path and then prepare new Zip with these files """
    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

    # printing the list of all files to be zipped
    print('The following files will be zipped:')
    for file_name in file_paths:
        print(file_name)

    with zipfile.ZipFile(newFileToZip,'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
    print('All files zipped successfully!')


def run(args):
    """ Main run function to call other functions to execute with arguments """
    input_zipfile = args.zipinput # these match the "dest": dest="zipinput"
    output_zipfile = args.ziptoout # from dest="ziptoout"
    json_filename = args.jsonfile # from dest="jsonfile"
    read_zip_file(dir_path + '/' + input_zipfile)
    update_json_file(dir_path + '/' + json_filename, 'text', 'Yeni Mena')
    prepareZipFile(directory, output_zipfile)

def main():
    """ Main function to get arguments from console """
    parser=argparse.ArgumentParser(description="Extract and edit JSON file from ZIP. Then create new ZIP from edited file.")
    parser.add_argument("-zin",help="Input Zip filename" ,dest="zipinput", type=str, required=True)
    parser.add_argument("-zout",help="Output Zip filename" ,dest="ziptoout", type=str, required=True)
    parser.add_argument("-jsonf",help="JSON file to edit" ,dest="jsonfile", type=str, required=True)
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)


if __name__=="__main__":
        main()

