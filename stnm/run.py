import argparse
import os
import sys

assert sys.version_info[0] == 3 and sys.version_info[1] >= 5, "Requires Python 3.5 or newer"

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

if sys.platform not in ["linux", "linux2", "darwin"]:
    print("stnm supports only macos and linux")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="")
    cmd_list = (
        "install",
        "status",
        "start",
        "stop",
        "config",
        "web",
        "test"
    )

    parser.add_argument("cmd", choices=cmd_list, nargs="?", default="")
    parser.add_argument("arg", nargs="?", default="")

    args = parser.parse_args()
    cmd = args.cmd
    arg = args.arg

    if cmd == "config" and arg == "":
        parser.error("configuration parameter required. e.g node.miner=true")

    from stnm import main
    main(cmd, arg)


if __name__ == '__main__':
    main()
