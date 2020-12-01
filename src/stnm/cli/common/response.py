import json
import sys

ERROR = {
    1: "stacks-node not installed. install manually or run `stnm install",
    2: "stacks-node process not found",
    3: "stacks-node is already running",
    4: "could not stopped node process"
}


def error_response(code: int):
    message = ERROR[code]

    resp = {
        "error": True,
        "message": message
    }

    print(json.dumps(resp))
    sys.exit(1)


SUCCESS = {
    1: "stacks-node process is running",
    2: "stacks-node process was killed",
    3: "stacks-node process started"
}


def success_response(code: int, **kwargs):
    message = SUCCESS[code]

    resp = {
        **{"success": True, "message": message},
        **kwargs
    }

    print(json.dumps(resp))
    sys.exit(0)
