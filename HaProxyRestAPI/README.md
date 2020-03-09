#### This is the simple REST API to use HAProxy inside of our DevOps environment via CI/CD pipeline. 

##### To execute this python script we must install some needed libraries like as the following:
```zsh
➜  ~ pip3 install -r requirements.txt
```

##### For the `Basic Authentication` I have used `haproxy` username and password inside of the `separated_func_file.py` file which you can change.

##### Get list of the backend configurations:
```zsh
$ curl -XGET -u haproxy:haproxy http://127.0.0.1:5000/backends
```

##### Get backend configuration of the `http_port_80`:
```zsh
$ curl -XGET -u haproxy:haproxy "http://127.0.0.1:5000/getbacksrvs?backend_name=http_port_80"
```

##### Get weight of the server `server1` inside of the backend `http_port_80`
```zsh
$ curl -XGET -u haproxy:haproxy "http://127.0.0.1:5000/getbacksrvwight?backend_name=http_port_80&server_name=server1"
```

##### Set weight to the hither `256` of the server `server1` inside of the backend `http_port_80`:
```zsh
$ curl -XPOST -u haproxy:haproxy "http://127.0.0.1:5000/setbacksrvwight?backend_name=http_port_80&server_name=server1&weight=256"
```

##### Disable traffik to server `server1` inside of the backend `http_port_80`:
```zsh
$ curl -XPOST -u haproxy:haproxy "http://127.0.0.1:5000/drainornot?traffic=disable&backend_name=http_port_80&server_name=server1"
```

##### Enable traffik to server `server1` inside of the backend `http_port_80`:
```zsh
$ curl -XPOST -u haproxy:haproxy "http://127.0.0.1:5000/drainornot?traffic=enable&backend_name=http_port_80&server_name=server1"
```
