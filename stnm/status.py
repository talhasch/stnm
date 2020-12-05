from stnm.response import error_response, success_response
from stnm.shell import get_node_process


def status():
    process = get_node_process()

    if process is None:
        error_response(2)

    success_response(1, **{"pid": process.pid})
