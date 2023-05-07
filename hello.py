from flask import Flask, json, request,jsonify #import flask class
app = Flask(__name__)
app.config["DEBUG"] = False

seed_num = 0
@app.route('/', methods = ['GET', 'POST']) #GET: send data from api to user
def home():
    global seed_num
    if request.method == 'GET':
        return str(seed_num)
    if request.method == 'POST':
        #read json 'num'
        posted_data = request.get_json()
        seed_value = posted_data['num']
        seed_num = seed_value
        return None

if __name__=='__main__':
    app.run(debug = True, host="0.0.0.0", port=80)
