import subprocess
from typing import Optional

import psutil


def get_node_process() -> Optional[psutil.Process]:
    try:
        pid = subprocess.check_output(["pgrep", "-f", "stacks-node"]).decode()
    except subprocess.CalledProcessError:
        return None

    return psutil.Process(int(pid))
