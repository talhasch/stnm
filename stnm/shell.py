import os
import shutil
from typing import Optional

from stnm.path import cargo_bin_path

env = os.environ.copy()
env["PATH"] = cargo_bin_path + os.path.pathsep + env["PATH"]


def which(name: str) -> Optional[str]:
    return shutil.which(name, path=env["PATH"])
