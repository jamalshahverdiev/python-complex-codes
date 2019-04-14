*******************************************************************************************************
Extract ZIP file. Edit JSON to update with new value of the key. Compress all files to tne new ZIP file
*******************************************************************************************************

.. image:: https://img.shields.io/codecov/c/github/codecov/example-python.svg

Python script to extract ZIP file utdate JOSN key/value and create new ZIP file. 

* **editjsoninzip.py** - Script contains four functions. ``read_zip_file``, ``update_json_file``, ``get_all_file_paths`` and ``prepareZipFile``. 
* ``read_zip_file`` - This function prints content of ZIP file and extract in the same folder.
* ``update_json_file`` - This function opens JSON file and edit defined key to the defined value.
* ``get_all_file_paths`` - This function creates list of the all files from argument PATH.
* ``prepareZipFile`` - This function will use ``get_all_file_paths`` function to get all files PATH and then archive them to the other file.

=====
Usage
=====

Requirements:
    Python3.4 with ``simplejson`` and ``argparse`` library installed:
        

Syntax:

.. code-block:: bash

    # ./editjsoninzip.py
    usage: editjsoninzip.py [-h] -zin ZIPINPUT -zout ZIPTOOUT -jsonf JSONFILE
    editjsoninzip.py: error: the following arguments are required: -zin, -zout, -jsonf
..
