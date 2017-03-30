**********************************************************************************
If MAC address table of Cisco switches is changed, then send email notification!!!
**********************************************************************************

.. image:: https://img.shields.io/codecov/c/github/codecov/example-python.svg

Python script to send email about MAC address changes.

* **switchnotificator.py** - Script authenticate with in Cisco switches and compare MAC address list from **StaticMacs** file with ``outdir/MAC.result`` file. If MAC address not found then, email will be send to defined Network Administrator for the security reason.
* **createstaticmacs.py** - Script checks **StaticMacs** file. If file exists and empty or doesn't exists it will create it.
* **iplist** - This file must contain IP address list of Cisco switches.
* To configure gmail settings just edit **frommail**, **fromemailpass**, **tomail** variables in the ``lib/varsfuncs.py`` file.


=====
Usage
=====

Requirements:
    Python2.7 or Python3.4 with ``paramiko`` must be installed:
        

Replace e-mail addresses and password indicated in the ``switchnotificator.py`` file with yours.

Syntax:

.. code-block:: bash

    # git clone https://github.com/jamalshahverdiev/python-general-codes.git
    # cd python-general-codes/switch-notificator
    # ./switchnotificator.py switchusername 'switch_long_password' vlanID
..


* If you want use ``switchnotificator.py`` script automatically every minute, just add the following line to your crontab file::

     * * * * * /root/switch-notificator/switchnotificator.py switchusername 'switch_long_password' vlanID
