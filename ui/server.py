from flask import Flask, render_template, jsonify
from services.stats import get_stats

app = Flask(__name__, template_folder='ui/templates', static_folder='ui/static')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stats")
def stats():
    return jsonify(get_stats())

def start_ui():
    app.run(host="0.0.0.0", port=8080)