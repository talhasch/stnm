import argparse
import os
import sys

assert sys.version_info[0] == 3 and sys.version_info[1] >= 5, "Requires Python 3.5 or newer"

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))


def main():
    parser = argparse.ArgumentParser(description="")
    cmd_list = (
        "install",
        "status",
        "start",
        "stop",
    )

    parser.add_argument('cmd', choices=cmd_list, nargs='?', default="status")

    args = parser.parse_args()
    cmd = args.cmd

    if cmd == "install":
        from stnm.cli.commands.install import main
        main()

    if cmd == "status":
        from stnm.cli.commands.status import main
        main()

    if cmd == "start":
        from stnm.cli.commands.start import main
        main()

    if cmd == "stop":
        from stnm.cli.commands.stop import main
        main()


if __name__ == '__main__':
    main()
