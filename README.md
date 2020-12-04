# STNM

Stacks node process manager.

## Getting Started

STNM written with python. Requires python 3.5+ and pip3. Compatible with Linux and macOS.

### Linux users

Make sure you have pip3 and python3dev packages installed on your system.

`$ apt install python3-pip python3-dev` 

### macOS users
You can download python installer from here https://www.python.org/downloads/ if you don't have it installed on your system.

### Installation with pip3 (easier way)
 
`$ pip3 install stnm` 

### Installation from source code

`$ git clone https://github.com/talhasch/stnm && cd stnm && pip3 install -e .` 

## Usage

Most STNM commands outputs in json format for easy integration.

### Available commands

### `$ stnm install`

stacks-blockchain auto installer. If you don't have stacks blockchain (stacks-node) installed on your system run this command to install it.

### `$ stnm status`

Outputs stacks-node process status with json format.

Possible outputs:

`{"success": true, "message": "stacks-node process is running", "pid": 1234}`

`{"error": true, "message": "stacks-node process is not running"}`


### `$ stnm start`

Starts stacks-node process.

Possible outputs:

`{"success": true, "message": "stacks-node process started", "pid": 1234}`

`{"error": true, "message": "stacks-node is already running"}`


### `$ stnm stop`

Stops (kills) stacks-node process.

Possible outputs:

`{"success": true, "message": "stacks-node process killed"}`

`{"error": true, "message": "stacks-node process is not running"}`

### `$ stnm config`

Config command outputs current config file by default.

takes an additional input parameter


```
        +---------------------+
        |      parameter      |
        +---------------------+
input = burnchain.burn_fee_cap=20000000
        |section |     key    | value |
        +-----------------------------+
        |          entry              |
        +-----------------------------+
```

### API

Provides a wrapper HTTP API for STNM commands.

#### Endpoints

##### /api/status [GET]

`$ curl http://127.0.0.1:8081/api/status` 

##### /api/start [POST]

`$ curl -X POST http://127.0.0.1:8081/api/start` 

##### /api/stop [POST]

`$ curl -X POST http://127.0.0.1:8081/api/stop`

##### /api/config [GET]

Returns current config file as json.

`$ curl http://127.0.0.1:8081/api/config` 

##### /api/config [POST]

Updates config file with input passed in json body of http request.

`$ curl -X POST --header "Content-Type: application/json" --data '{"input": "node.miner=true,burnchain.burn_fee_cap=2000"}' "http://127.0.0.1:8081/api/config"`


### Mining bot web UI

coming soon...


