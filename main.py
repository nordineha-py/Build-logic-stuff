from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.get("/hours")
def hours():
    value = datetime.now(timezone.utc).hour
    return jsonify(value=format(value, "08b"))

@app.get("/minutes")
def minutes():
    value = datetime.now(timezone.utc).minute
    return jsonify(value=format(value, "08b"))

@app.get("/seconds")
def seconds():
    value = datetime.now(timezone.utc).second
    return jsonify(value=format(value, "08b"))

app.run(host="0.0.0.0", port=5000)
