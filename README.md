# STNM

Stacks blockchain node process manager.

## Getting Started

STNM developed with python. Requires python 3.5+ and pip3. Compatible with Linux and macOS.

### Linux users

The following one-liner code will install dependencies to get started with STNM.

`$ apt update && apt install build-essential python3-pip python3-dev python3-setuptools -y && pip3 install --upgrade pip` 

### macOS users
You can download python installer from here: https://www.python.org/downloads/ if you don't have it installed on your system.

It's always good to upgrade pip.

`$ pip3 install --upgrade pip` 

Additionally you may need to install `git` and `curl` manually if you don't have them installed your system.

## Install 
 
`$ pip3 install stnm -U` 

## Usage

*Most STNM commands output in json format for easy integration.*

### Available commands

### `$ stnm install`

stacks-blockchain auto installer. If you don't have stacks blockchain (stacks-node) installed on your system run this command to install it.

### `$ stnm status`

Outputs stacks-node process status.

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

Starts STNM API and Web UI.

**STNM API** Provides a wrapper HTTP API for STNM commands.

#### Endpoints

##### /api/status [GET]

`$ curl "http://127.0.0.1:8081/api/status"` 

##### /api/start [POST]

`$ curl -X POST "http://127.0.0.1:8081/api/start"` 

##### /api/stop [POST]

`$ curl -X "POST http://127.0.0.1:8081/api/stop"`

##### /api/config [POST]

Updates config file with input passed in json body of http request.

``` 
$ curl -X POST --header "Content-Type: application/json" --data '{"input": "node.miner=true,burnchain.burn_fee_cap=2000"}' "http://127.0.0.1:8081/api/config"
```

##### /api/config [GET]

Returns current config file contents in json and text format.

`$ curl "http://127.0.0.1:8081/api/config"` 

Sample response:

```
{
  "object": {
    "burnchain": {
      "chain": "bitcoin",
      "mode": "krypton",
      "peer_host": "bitcoind.krypton.blockstack.org",
      "peer_port": 18444,
      "process_exit_at_block_height": 5130,
      "rpc_port": 18443
    },
    "mstx_balance": [
      {
        "address": "STB44HYPYAT2BB2QE513NSP81HTMYWBJP02HPGK6",
        "amount": 10000000000000000
      },
      {
        "address": "ST11NJTTKGVT6D1HY4NJRVQWMQM7TVAR091EJ8P2Y",
        "amount": 10000000000000000
      },
      {
        "address": "ST1HB1T8WRNBYB0Y3T7WXZS38NKKPTBR3EG9EPJKR",
        "amount": 10000000000000000
      },
      {
        "address": "STRYYQQ9M8KAF4NS7WNZQYY59X93XEKR31JP64CP",
        "amount": 10000000000000000
      }
    ],
    "node": {
      "bootstrap_node": "048dd4f26101715853533dee005f0915375854fd5be73405f679c1917a5d4d16aaaf3c4c0d7a9c132a36b8c5fe1287f07dad8c910174d789eb24bdfb5ae26f5f27@krypton.blockstack.org:20444",
      "p2p_bind": "0.0.0.0:20444",
      "rpc_bind": "0.0.0.0:20443"
    }
  },
  "raw": "\n[node]\nrpc_bind = \"0.0.0.0:20443\"\np2p_bind = \"0.0.0.0:20444\"\nbootstrap_node = \"048dd4f26101715853533dee005f0915375854fd5be73405f679c1917a5d4d16aaaf3c4c0d7a9c132a36b8c5fe1287f07dad8c910174d789eb24bdfb5ae26f5f27@krypton.blockstack.org:20444\"\n\n[burnchain]\nchain = \"bitcoin\"\nmode = \"krypton\"\npeer_host = \"bitcoind.krypton.blockstack.org\"\nrpc_port = 18443\npeer_port = 18444\nprocess_exit_at_block_height = 5130\n\n[[mstx_balance]]\naddress = \"STB44HYPYAT2BB2QE513NSP81HTMYWBJP02HPGK6\"\namount = 10000000000000000\n\n[[mstx_balance]]\naddress = \"ST11NJTTKGVT6D1HY4NJRVQWMQM7TVAR091EJ8P2Y\"\namount = 10000000000000000\n\n[[mstx_balance]]\naddress = \"ST1HB1T8WRNBYB0Y3T7WXZS38NKKPTBR3EG9EPJKR\"\namount = 10000000000000000\n\n[[mstx_balance]]\naddress = \"STRYYQQ9M8KAF4NS7WNZQYY59X93XEKR31JP64CP\"\namount = 10000000000000000\n"
}
```

##### /api/config-params [GET]

Returns a list of available config options.

Sample response:

```
[
    "node.miner",
    "node.seed",
    "burnchain.burn_fee_cap",
    "burnchain.peer_port",
    "burnchain.process_exit_at_block_height",
    "burnchain.rpc_port"
]
```

#### Environment variables for web application

|	Variable       	|	Default     	|
|	------------	|	------------	|
|	WEB_PORT     	|	8081     	    |
|	WEB_HOST     	|	127.0.0.1       |

