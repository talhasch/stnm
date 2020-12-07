import json
import os
from typing import Dict

from flask import Flask, jsonify, request, abort, render_template

from stnm.config import get_config_parsed, get_config, AVAILABLE_PARAMS
from stnm.shell import which

app = Flask(__name__)

this_dir = os.path.abspath(os.path.dirname(__file__))


def communicate(cmd: str, arg: str = "") -> Dict:
    executable = which("stnm")
    out = os.popen("{} {} {} &".format(executable, cmd, arg)).read()
    return json.loads(out)


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
    config = get_config().strip()
    config_parsed = get_config_parsed()

    resp = {
        "raw": config,
        "object": config_parsed
    }

    return jsonify(resp)


@app.route("/api/config", methods=["POST"])
def api_config_post():
    data = request.json

    if type(data) == dict and "input" in data and type(data["input"]) == str and len(data["input"]) > 0:
        return jsonify(communicate("config", data["input"]))

    abort(400)


@app.route("/api/config-params", methods=["GET"])
def api_config_params():
    return jsonify(list(AVAILABLE_PARAMS.keys()))


@app.route("/ui", methods=["GET"])
def ui_index():
    return render_template("index.jinja2")
