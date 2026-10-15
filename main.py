
from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

def to_bcd(value):
    tens = value // 10
    ones = value % 10
    return format(tens, "04b") + format(ones, "04b")

@app.get("/hours")
def hours():
    value = datetime.now(timezone.utc).hour
    return jsonify(value=to_bcd(value))

@app.get("/minutes")
def minutes():
    value = datetime.now(timezone.utc).minute
    return jsonify(value=to_bcd(value))

@app.get("/seconds")
def seconds():
    value = datetime.now(timezone.utc).second
    return jsonify(value=to_bcd(value))
