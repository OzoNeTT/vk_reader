# Automatic reader of VK 

This program is designed to automatically read VK messages using the API.

Special thanks to [Toliak](https://github.com/Toliak) for helping 

## Installation

### Classic

```ShellSession
$ git clone https://github.com/OzoNeTT/vk_reader
$ cd vk_reader
$ sudo pip install request 
$ sudo pip install lxml
$ sudo pip install vk-api
```

Create `local.py` file and write the following into it

```Python
VK_AUTH = ['VK_LOGIN_IN_BASE64', 'VK_PASS_IN_BASE64']
VK_IGNORE_LIST = ['PEER_ID1', 'PEER_ID2', ...]
```
Run and have fun

### Docker Image

```ShellSession
$ docker build . --tag ${IMAGENAME}
$ docker run -it ${IMAGENAME} python ./reader/start.py
```

