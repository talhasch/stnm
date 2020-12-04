from stnm.cli.common.process import get_node_process

from stnm.cli.common.response import error_response, success_response


def status():
    process = get_node_process()

    if process is None:
        error_response(2)

    success_response(1, **{"pid": process.pid})
