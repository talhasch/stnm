import os
from pathlib import Path

devnull = open(os.devnull, "wb")
home_path = os.path.abspath(str(Path.home()))
cargo_bin_path = os.path.join(home_path, ".cargo", "bin")
