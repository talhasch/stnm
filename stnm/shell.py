import os
import shutil
import subprocess
from typing import Optional

import psutil

from stnm.constants import CARGO_BIN_PATH

env = os.environ.copy()
env["PATH"] = CARGO_BIN_PATH + os.path.pathsep + env["PATH"]


def which(name: str) -> Optional[str]:
    return shutil.which(name, path=env["PATH"])


def get_node_process() -> Optional[psutil.Process]:
    try:
        pid = subprocess.check_output(["pgrep", "-f", "stacks-node"]).decode()
    except subprocess.CalledProcessError:
        return None

    return psutil.Process(int(pid))
