import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder="app/templates")

instance1_ip = os.getenv("INSTANCE1_IP")
instance2_ip = os.getenv("INSTANCE2_IP")

@app.route('/')
def home():
    return render_template('index.html', instance1_ip=instance1_ip, instance2_ip=instance2_ip)

@app.route('/proxy/square-area', methods=['POST'])
def proxy_square_area():
    data = request.json
    response = requests.post(f"http://{instance1_ip}:8080/function/square-area", json=data)
    return jsonify(response.json())

@app.route('/proxy/cube-area', methods=['POST'])
def proxy_cube_area():
    data = request.json
    response = requests.post(f"http://{instance2_ip}:8080/function/cube-area", json=data)
    return jsonify(response.json())