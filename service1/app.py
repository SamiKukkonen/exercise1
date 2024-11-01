import os
import socket
from flask import Flask, jsonify
import subprocess
import requests
import time

app = Flask(__name__)

def get_system_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    processes = subprocess.check_output(["ps", "ax"]).decode("utf-8")
    disk_space = subprocess.check_output(["df", "-h", "/"]).decode("utf-8")
    boot_time = subprocess.check_output(["uptime", "-s"]).decode("utf-8").strip()

    return {
        "ip_address": ip_address,
        "processes": processes,
        "disk_space": disk_space,
        "boot_time": boot_time
    }

@app.route('/request')  # Changed route to match NGINX
def system_info():
    service1_info = get_system_info()

    # Request Service 2's info
    try:
        service2_response = requests.get("http://service2:3000/")
        service2_info = service2_response.json()
    except Exception as e:
        service2_info = {"error": str(e)}

    # Combine Service 1 and Service 2 info
    combined_info = {
        "Service1": service1_info,
        "Service2": service2_info
    }

    # Adding a delay to simulate response time
    time.sleep(int(os.getenv("SLEEP_DELAY", 2)))
    return jsonify(combined_info)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8199)
