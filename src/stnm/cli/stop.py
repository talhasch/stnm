from stnm.cli.common.process import get_node_process

from stnm.cli.common.response import error_response, success_response


def stop():
    process = get_node_process()
    if process is None:
        error_response("node process not found")

    try:
        process.kill()
        success_response("node process stopped")
    except Exception:
        error_response("could not stopped node process")
