import shutil
from typing import Optional
import os
from pathlib import Path


def which(name: str) -> Optional[str]:
    return shutil.which(name)


def config_path() -> str:
    return os.path.join(str(Path.home()), "stnm.conf")
