from stnm.cli.common.process import get_node_process

from stnm.cli.common.response import error_response, success_response


def stop():
    process = get_node_process()
    if process is None:
        error_response(2)

    try:
        process.kill()
        success_response(2)
    except Exception:
        error_response(4)
