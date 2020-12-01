import json
import sys


def error_response(message: str):
    resp = {
        "error": True,
        "message": message
    }

    print(json.dumps(resp))
    sys.exit(1)


def success_response(message: str, **kwargs):
    resp = {
        **{"success": True, "message": message},
        **kwargs
    }

    print(json.dumps(resp))
    sys.exit(0)
