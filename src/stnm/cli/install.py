from stnm.cli.common.util import which
import sys
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)


def install():
    if which("stacks-node") is not None:
        logging.info("stacks-node already installed.")
        return

    if which("git") is not None:
        # git is required
        pass

    if which("apt-get") is not None:
        # install essentials
        #  apt-get install build-essential cmake libssl-dev pkg-config
        pass

    if which("rustc") is None:
        # curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
        # source $HOME/.cargo/env
        # assert which("rustc") is not None
        pass

    # git clone https://github.com/blockstack/stacks-blockchain.git
    # cd stacks-blockchain
    # cp target/release/stacks-node $HOME/.cargo/bin
    pass

    home_path = str(Path.home())

    exit()

    node = which("stacks-node")
    git = which("git")
    apt = which("apt-get")
    rustc = which("rustc")

    if sys.platform == "linux":
        pass
        # apt-get install build-essential cmake libssl-dev pkg-config

    print(rustc)
