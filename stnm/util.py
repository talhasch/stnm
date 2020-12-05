import shutil
from typing import Optional


def which(name: str, path: str = None) -> Optional[str]:
    return shutil.which(name, path=path)
