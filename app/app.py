from flask import Flask
import time
import math

app = Flask(__name__)

def burn_cpu():
    end_time = time.time() + 60
    while time.time() < end_time:
        for i in range(10000000):
            math.sqrt(i)

@app.route("/")
def home():
    return "Observability App Running"

@app.route("/cpu")
def cpu_stress():
    burn_cpu()
    return "CPU stress completed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
