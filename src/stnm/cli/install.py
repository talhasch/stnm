import os
import shutil
import subprocess
from pathlib import Path

from stnm.cli.common.util import which

GREEN_COLOR = "\033[92m"
RED_COLOR = "\033[91m"
GRAY_COLOR = "\033[90m"
END_COLOR = "\033[0m"


def success(s: str):
    print("{}{}{}".format(GREEN_COLOR, s, END_COLOR))


def error(s: str):
    print("{}{}{}".format(RED_COLOR, s, END_COLOR))


def info(s: str):
    print("{}{}{}".format(GRAY_COLOR, s, END_COLOR))


def run_cmd(cmd: str) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, shell=True, universal_newlines=True)


def install():
    if which("stacks-node") is not None:
        success("stacks-node already installed.")
        return

    if which("git") is None:
        error("git is not found on your system. please install it first.")
        return

    if which("apt-get") is not None:
        info("install essentials for linux...")
        cmd = "apt-get install build-essential cmake libssl-dev pkg-config -y"
        if run_cmd(cmd).returncode != 0:
            error("an error occurred while installing essentials.")
        else:
            success("essentials installed successfully.")

    info("checking rust...")
    if run_cmd("rustc --version").returncode != 0:
        info("installing rust.")
        cmd = "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y"
        if run_cmd(cmd).returncode != 0:
            error("an error occurred while installing rust.")
        else:
            success("rust installed successfully.")
    else:
        success("rust is already installed.")

    home_dir = os.path.abspath(str(Path.home()))

    chain_dir = os.path.join(home_dir, "stacks-blockchain-stnm")
    if os.path.isdir(chain_dir):
        shutil.rmtree(chain_dir)

    cmd = "git clone https://github.com/blockstack/stacks-blockchain.git {}".format(chain_dir)
    info("downloading stacks-blockchain...")
    if run_cmd(cmd).returncode != 0:
        error("an error occurred while downloading.")
    else:
        success("stacks-blockchain downloaded.")

    os.chdir(chain_dir)

    cmd = "cargo build --workspace --release --bin stacks-node"
    info("building stacks-blockchain...")
    if run_cmd(cmd).returncode != 0:
        error("an error occurred while building.")
    else:
        success("stacks-blockchain has built successfully.")

    bin_source = os.path.join(chain_dir, "target", "release", "stacks-node")
    bin_dest = os.path.join(home_dir, ".cargo", "bin")
    shutil.copyfile(bin_source, bin_dest)
    success("stacks-node binary copied to cargo directory.")

    # clean up
    shutil.rmtree(chain_dir)

    assert which("stacks-node") is not None

    success("installation completed successfully 🎉")
