#!/usr/bin/env python
import sys
import os
from flask import Flask, url_for, json, request, Response, jsonify, make_response

app = Flask(__name__)

@app.route('/getRunningContainers', methods = ['GET'])
def api_getcontainer():
    return jsonify(os.popen('docker ps | grep -v CONTAINER').readlines())

@app.route('/createcontainer', methods = ['POST'])
def api_createcontainer():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        if (request.json):
            imagename = str(request.json['imagename'])
            containername = str(request.json['containername'])
            daemonize = str(request.json['daemonize'])            
            exposedPort = str(request.json['exposedPort'])            
            cmd = ('docker run -d --name {} -p {}:80 {}'.format(containername, exposedPort, imagename))

            if imagename and containername:
                if os.system(cmd) == 0:
                    print("Docker executed successful!")
                    return (str(os.system('docker ps | grep {}'.format(containername))))
                else:
                    print("Docker run time happened somtheing wrong!")
        else:
            return "JSON content is wrong!!!"

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"

@app.route('/getcontainer', methods = ['GET'])
def api_hello():
    if 'name' in request.args:
        #return 'Hello ' + request.args['name']
        return jsonify(os.popen('docker ps | grep {}$'.format(request.args['name'])).readlines())
    else:
        return 'To get Container status please use ?name= argument in the url.'

if __name__ == '__main__':
    app.run(host='10.1.42.201', port=80, debug=True)
