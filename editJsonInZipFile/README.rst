*******************************************************************************************************
Extract ZIP file. Edit JSON to update with new value of the key. Compress all files to tne new ZIP file
*******************************************************************************************************

.. image:: https://img.shields.io/codecov/c/github/codecov/example-python.svg

Python script to send email about MAC address changes.

* **zipper.py** - Script contains four functions. ``read_zip_file``, ``update_json_file``, ``get_all_file_paths`` and ``prepareZipFile``. 
* ``read_zip_file`` - This function prints content of ZIP file and extract in the same folder.
* ``update_json_file`` - This function opens JSON file and edit defined key to the defined value.
* ``get_all_file_paths`` - This function creates list of the all files from argument PATH.
  ``prepareZipFile`` - This function will use ``get_all_file_paths`` function to get all files PATH and then archive them to the other file.

=====
Usage
=====

Requirements:
    Python3.4 with ``simplejson`` library installed:
        

Syntax:

.. code-block:: bash

    # ./zipper.py
..
