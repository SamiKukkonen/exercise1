# control_service/app.py
from flask import Flask, jsonify, request
import os
import signal
import sys

app = Flask(__name__)

@app.route('/stop', methods=['POST'])
def stop():
    # Respond to the client before shutting down
    response = jsonify({"message": "Shutting down all services..."})
    response.status_code = 200
    shutdown_server()
    return response

def shutdown_server():
    # Trigger a clean shutdown of the Flask app
    os.kill(os.getpid(), signal.SIGTERM)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
