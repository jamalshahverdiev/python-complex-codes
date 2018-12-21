#!/usr/bin/env python3.4

import zipfile
import os
import simplejson as json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
zipFileName = 'files.zip'
fullZipPath = dir_path + '/' + zipFileName
jsonFileName = dir_path + '/salam.json'
directory = './'

def read_zip_file(fullZipPath):
    with zipfile.ZipFile(fullZipPath) as zfile:
	# Show ZIP file content
        zfile.printdir()

        print('Extracting all files')
        zfile.extractall()
        print('Done!')

def update_json_file(jsonFileName):
    with open(jsonFileName, "r+") as jsonFile:
        data = json.load(jsonFile)

        tmp = data["text"]
        data["text"] = "My New Message"

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile, sort_keys=True, indent=2)
        jsonFile.truncate()

def get_all_file_paths(directory):

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

def prepareZipFile(directory):
    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)

    with zipfile.ZipFile('new_files.zip','w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
    print('All files zipped successfully!')


read_zip_file(fullZipPath)
update_json_file(jsonFileName)
prepareZipFile(directory)
