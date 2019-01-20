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
    Python2.7 or Python3.4 with ``flask`` must be installed:
        

Syntax:

.. code-block:: bash

    # pip install flask
    # git clone https://github.com/jamalshahverdiev/python-general-codes.git
    # cd python-general-codes/simple-docker-flask-api
    # ./dockerApi.py
..


* Get contaner status with the name **web**:

.. code-block:: bash

    # curl http://10.1.42.201/getcontainer?name=web
..

* Get status of all running containers:

.. code-block:: bash

    # curl http://10.1.42.201/getRunningContainers
..


* Create new container with the payload data from **jsondata.json** file. In the JSON file we must define values of the needed fields.
* **imagename** - in the value must be defined image name from https://hub.docker.com 
* **containername** - in the value must be defined container name which will be executed in the server
* **exposedPort** - in the value must be defined the port number which will be exposed to the Host OS

.. code-block:: bash
  
    # curl -v -s -XPOST -H "Content-type: application/json" http://10.1.42.201/createcontainer -d @jsondata.json
..
