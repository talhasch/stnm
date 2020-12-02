import json
import subprocess

from flask import Flask, jsonify
from typing import Dict

app = Flask(__name__)


def communicate(cmd: str) -> Dict:
    process = subprocess.Popen(["stnm", cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    resp = process.communicate()[0].decode("utf-8")
    return json.loads(resp)


@app.route("/api")
def api_index():
    return jsonify({"hello": "world"})


@app.route("/api/status")
def api_status():
    return jsonify(communicate("status"))


@app.route("/api/start")
def api_start():
    return jsonify(communicate("start"))


@app.route("/api/stop")
def api_stop():
    return jsonify(communicate("stop"))
