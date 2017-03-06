**********************************************************************************
If MAC address table of Cisco switches is changed, then send email notification!!!
**********************************************************************************

.. image:: https://img.shields.io/codecov/c/github/codecov/example-python.svg

Python script to send email about MAC address changes.

* switchnotificator.py - Script authenticate with in Cisco switches and compare MAC address list from "StaticMacs" file with "outdir/MAC.result" file. If MAC address found then, email will be send to defined person for the security reason.
* createstaticmacs.py - Script checks "StaticMacs" file. If file exists and empty or doesn't exists it will create it.
* iplist - This file must contain IP address list of Cisco switches.


=====
Usage
=====

Requirements:
    Python2.7 with "paramiko" must be installed:
        

Replace e-mail addresses and password indicated in the "switchnotificator.py" file with yours.

Syntax:

.. code-block:: bash

    # git clone https://github.com/jamalshahverdiev/python-general-codes.git
    # cd python-general-codes/switch-notificator
    # ./switchnotificator.py
..

Just add "switchnotificator.py" script to hourly CRON.
