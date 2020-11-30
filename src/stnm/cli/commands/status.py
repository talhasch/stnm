from stnm.cli.process import get_node_process

from stnm.cli.response import error_response, success_response


def main():
    process = get_node_process()

    if process is None:
        error_response("node process not found")

    success_response("node process running", **{"cmd": process.cmdline()})
