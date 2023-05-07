from flask import Flask, json, request,jsonify #import flask class
import socket 
import subprocess
import sys

app = Flask(__name__)
app.config["DEBUG"] = True

seed_num = 0
@app.route('/', methods = ['GET', 'POST']) #GET: send data from api to user
def home():
    if request.method == 'GET':
        return socker.gethostname() 
    if request.method == 'POST':
        theproc = subprocess.Popen([sys.executable, "stress_cpu.py"])
        theproc.communicate()

if __name__=='__main__':
    app.run(debug = True, host="0.0.0.0", port=80)
