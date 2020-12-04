import shutil
from typing import Optional


def which(name: str) -> Optional[str]:
    return shutil.which(name)

