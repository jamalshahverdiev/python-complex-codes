**********************************************************************************
Run container via API and get running containers
**********************************************************************************

.. image:: https://img.shields.io/codecov/c/github/codecov/example-python.svg

* **createJson.py** - Script create Json output(**docker ps** execute outout) from running containers.
* **echoTest.py** - Simple API to learn.
* **dockerApi.py** - This script must be executed in the Web server or Flask default web server.


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
