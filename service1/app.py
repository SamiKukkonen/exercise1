import os
import socket
from flask import Flask, jsonify
import subprocess
import requests

app = Flask(__name__)

def get_system_info():
    # Get IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    # Getthe list of running processes
    processes = subprocess.check_output(["ps", "ax"]).decode("utf-8")

    # Get the available disk space
    disk_space = subprocess.check_output(["df", "-h", "/"]).decode("utf-8")

    # Get time since last boot
    boot_time = subprocess.check_output(["uptime", "-s"]).decode("utf-8").strip()

    return {
        "ip_address": ip_address,
        "processes": processes,
        "disk_space": disk_space,
        "boot_time": boot_time
    }

@app.route('/')
def system_info():
    # Get system info of Service 1
    service1_info = get_system_info()

    # Reguest to Service 2 to get its system info
    try:
        service2_response = requests.get("http://service2:3000/")
        service2_info = service2_response.json()
    except Exception as e:
        service2_info = {"error": str(e)}

    # Combine Service 1 and Service 2
    combined_info = {
        "Service1": service1_info,
        "Service2": service2_info
    }

    return jsonify(combined_info)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8199)

