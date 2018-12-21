*******************************************************************************************************
Extract ZIP file. Edit JSON to update with new value of the key. Compress all files to tne new ZIP file
*******************************************************************************************************

.. image:: https://img.shields.io/codecov/c/github/codecov/example-python.svg

Python script to send email about MAC address changes.

* **zipper.py** - Script contains four functions. ``read_zip_file``, ``update_json_file``, ``get_all_file_paths`` and ``prepareZipFile``. 
* **createstaticmacs.py** - Script checks **StaticMacs** file. If file exists and empty or doesn't exists it will create it.
* **iplist** - This file must contain IP address list of Cisco switches.
* To configure gmail settings just edit **frommail**, **fromemailpass**, **tomail** variables in the ``lib/varsfuncs.py`` file.


=====
Usage
=====

Requirements:
    Python3.4 with ``simplejson`` must be installed:
        

Syntax:

.. code-block:: bash

    # ./zipper.py
..
