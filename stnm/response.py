import json
import sys

ERROR = {
    1: "stacks-node not installed. install manually or run `stnm install",
    2: "stacks-node process is not running",
    3: "stacks-node is already running",
    4: "could not stopped node process",
    5: "not a valid config entry '{}' example: node.miner=true",
    6: "'{}' doesn't exits in available parameters",
    7: "validation failed with message: '{}'",
}


def error_response(code: int, *arg):
    message = ERROR[code]

    resp = {
        "error": True,
        "message": message.format(*arg)
    }

    print(json.dumps(resp))
    sys.exit(1)


SUCCESS = {
    1: "stacks-node process is running",
    2: "stacks-node process killed",
    3: "stacks-node process started",
    4: "config file updated"
}


def success_response(code: int, **kwargs):
    message = SUCCESS[code]

    resp = {
        **{"success": True, "message": message},
        **kwargs
    }

    print(json.dumps(resp))
    sys.exit(0)
