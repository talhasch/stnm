# STNM

Stacks blockchain node process manager.

## Getting Started

STNM developed with python. Requires python 3.5+ and pip3. Compatible with Linux and macOS.

### Linux users

Make sure you have following python dependencies installed on your system.

`$ apt update && apt install build-essential python3-pip python3-dev python3-setuptools -y` 

### macOS users
You can download python installer from here https://www.python.org/downloads/ if you don't have it installed on your system.

Additionally you may need to install `git` and `curl` manually if you don't have them installed your system.

## Install with pip (easier way)
 
`$ pip3 install stnm -U` 

## Install from source code

`$ git clone https://github.com/talhasch/stnm && cd stnm && pip3 install -e .` 

## Usage

Most STNM commands output in json format for easy integration.

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

Outputs current config file as text by default.

An additional input like below allows to modify config file:

`$ stnm config node.miner=true`

More than one config entry can be separated with comma:

`$ stnm config node.miner=true,burnchain.burn_fee_cap=2000`

```
Config Input Structure

        +---------------------+
        |      parameter      |
        +---------------------+
input = burnchain.burn_fee_cap=20000000
        |section |     key    | value |
        +-----------------------------+
        |        config entry         |
        +-----------------------------+
```

Available config parameters:

```
node.miner : boolean
node.seed : string
burnchain.burn_fee_cap : integer
burnchain.process_exit_at_block_height : integer
burnchain.rpc_port : integer
burnchain.peer_port : integer
```

Possible outputs:

```{"success": true, "message": "config file updated"}```

```{"error": true, "message": "not a valid config entry 'node.minerr' example: node.miner=true"}```

```{"error": true, "message": "'node.minerr' doesn't exits in available parameters"}```

```{"error": true, "message": "validation failed with message: 'truee is not a valid boolean value. Use True or true or False or false'"}```

***config update doesn't restart stacks-node process. manual `stnm stop` & `stnm start` actions required to make config file updated with stacks-node process.***

### `$ stnm web`

Starts STNM API and Mining Bot Web UI.

STNM API Provides a wrapper HTTP API for STNM commands.

#### Endpoints

##### /api/status [GET]

`$ curl "http://127.0.0.1:8081/api/status"` 

##### /api/start [POST]

`$ curl -X POST "http://127.0.0.1:8081/api/start"` 

##### /api/stop [POST]

`$ curl -X "POST http://127.0.0.1:8081/api/stop"`

##### /api/config [GET]

Returns current config file as json.

`$ curl "http://127.0.0.1:8081/api/config"` 

##### /api/config [POST]

Updates config file with input passed in json body of http request.

`$ curl -X POST --header "Content-Type: application/json" --data '{"input": "node.miner=true,burnchain.burn_fee_cap=2000"}' "http://127.0.0.1:8081/api/config"`

#### Environment variables for web application

|	Variable       	|	Default     	|
|	------------	|	------------	|
|	WEB_PORT     	|	8081     	    |
|	WEB_HOST     	|	127.0.0.1       |

