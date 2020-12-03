import json
import subprocess
from typing import Dict

import toml
from flask import Flask, jsonify

from stnm.helper import config_path

app = Flask(__name__)


def communicate(cmd: str) -> Dict:
    process = subprocess.Popen(["stnm", cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    resp = process.communicate()[0].decode("utf-8")
    return json.loads(resp)


@app.route("/api", methods=["GET"])
def api_index():
    return jsonify({"hello": "world"})


@app.route("/api/status", methods=["GET"])
def api_status():
    return jsonify(communicate("status"))


@app.route("/api/start", methods=["POST"])
def api_start():
    return jsonify(communicate("start"))


@app.route("/api/stop", methods=["POST"])
def api_stop():
    return jsonify(communicate("stop"))


@app.route("/api/config", methods=["GET"])
def api_config_get():
    with open(config_path(), "r") as f:
        config_contents = f.read()
        f.close()

    parsed = toml.loads(config_contents)
    return jsonify(parsed)
