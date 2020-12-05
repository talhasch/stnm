import json
import subprocess
from typing import Dict

from flask import Flask, jsonify, request, abort

from stnm.config import get_config_parsed
from stnm.shell import env

app = Flask(__name__)


def communicate(cmd: str, arg: str = "") -> Dict:
    process = subprocess.Popen(["stnm", cmd, arg], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
    return jsonify(get_config_parsed())


@app.route("/api/config", methods=["POST"])
def api_config_post():
    data = request.json

    if type(data) == dict and "input" in data and type(data["input"]) == str and len(data["input"]) > 0:
        return jsonify(communicate("config", data["input"]))

    abort(400)


@app.route("/ui", methods=["GET"])
def ui_index():
    return "coming soon..."
