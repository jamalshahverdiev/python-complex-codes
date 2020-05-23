#### This is the simple REST API to use HAProxy inside of our DevOps environment via CI/CD pipeline. 

[![Video Explanation](https://img.youtube.com/vi/E23p6kZVSN4/0.jpg)](https://www.youtube.com/watch?v=E23p6kZVSN4 "Click to see video on youtube.com") 

##### To execute this python script we must install some needed libraries like as the following:
```zsh
➜  ~ pip3 install -r requirements.txt
```

##### For the `Basic Authentication` I have used `haproxy` username and password inside of the `separated_func_file.py` file which you can change.

##### I have used `access_list.txt` file which contains allowed IP address list. I am reading content of the `access_list.txt` file from `separated_func_file.py` (Add your CI/CD IP address list to the `access_list.txt` file).

##### Get list of the backend configurations:
```zsh
$ curl -XGET -u haproxy:haproxy http://192.168.9.41:5000/backends
```

##### Get backend configuration of the `http_port_80`:
```zsh
$ curl -XGET -u haproxy:haproxy "http://192.168.9.41:5000/getbacksrvs?backend_name=http_port_80"
```

##### Get weight of the server `server1` inside of the backend `http_port_80`
```zsh
$ curl -XGET -u haproxy:haproxy "http://192.168.9.41:5000/getbacksrvwight?backend_name=http_port_80&server_name=server1"
```

##### Set weight to the hither `256` of the server `server1` inside of the backend `http_port_80`:
```zsh
$ curl -XPOST -u haproxy:haproxy "http://192.168.9.41:5000/setbacksrvwight?backend_name=http_port_80&server_name=server1&weight=256"
```

##### Disable traffik to server `server1` inside of the backend `http_port_80`:
```zsh
$ curl -XPOST -u haproxy:haproxy "http://192.168.9.41:5000/drainornot?traffic=disable&backend_name=http_port_80&server_name=server1"
```

##### Enable traffik to server `server1` inside of the backend `http_port_80`:
```zsh
$ curl -XPOST -u haproxy:haproxy "http://192.168.9.41:5000/drainornot?traffic=enable&backend_name=http_port_80&server_name=server1"
```

##### To use this script in the startup we can put `haproxyapi.service` under `/etc/systemd/system` folder. Don't forget create `/etc/haproxyapi` folder and upload source code files under this folder. At the end execute the following commands to activate and enable service.
```zsh
$ systemctl daemon-reload && systemctl --now start haproxyapi 
```
