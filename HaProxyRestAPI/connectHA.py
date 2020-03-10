#!/usr/bin/env python3

from separated_func_file import executeCommand, auth_required, filter_cicd
from flask import Flask, request

app = Flask(__name__)

@app.route('/backends', methods=['GET']) 
@filter_cicd
@auth_required
def getBackends():
    return executeCommand('show backend' + '\n')

@app.route('/getbacksrvs', methods=['GET'])
@filter_cicd
@auth_required
def getSelectedBackend():
    if 'backend_name' in request.args:
        return executeCommand('show servers state ' + request.args.get('backend_name') + '\n')
    else:
        return "backend_name required parameter", 404

@app.route('/getbacksrvwight', methods=['GET'])
@filter_cicd
@auth_required
def getBackendServerWeight():
    if 'backend_name' in request.args and 'server_name' in request.args:
        return executeCommand('get weight ' + request.args.get('backend_name') + '/' + request.args.get('server_name') + ' \n')
    else:
        return "server_name and backend_name are required parameters", 404

@app.route('/setbacksrvwight', methods=['POST'])
@filter_cicd
@auth_required
def setBackendServerWeight():
    if 'backend_name' in request.args and 'server_name' in request.args and 'weight' in request.args:
        return executeCommand('set weight ' + request.args.get('backend_name') + '/' + request.args.get('server_name') + ' ' + request.args.get('weight') + '\n')
    else:
        return "backend_name, server_name and weight are required parameters", 404

@app.route('/drainornot', methods=['POST'])
@filter_cicd
@auth_required
def drainOrNot():
    if 'traffic' in request.args and 'backend_name' in request.args and 'server_name' in request.args:
        return executeCommand(request.args.get('traffic') + ' server ' + request.args.get('backend_name') + '/' + request.args.get('server_name') + '\n')
    else:
        return "traffic (enable or disable), backend_name, server_name are required parameters", 404

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
