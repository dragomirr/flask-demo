from flask import Flask
from flask import jsonify
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(get_host_info())

def get_host_info():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return host_ip,hostname
