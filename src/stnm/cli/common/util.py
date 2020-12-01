import os
import shutil
from pathlib import Path
from typing import Optional


def which(name: str) -> Optional[str]:
    return shutil.which(name)


def config_path() -> str:
    return os.path.abspath(os.path.join(str(Path.home()), "stnm.conf"))
