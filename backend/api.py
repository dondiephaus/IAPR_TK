from flask import Flask,request,jsonify
import pandas as pd
import logging

app = Flask(__name__)



logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)




@app.route('/calculate', methods=['POST'])
def calculate():

    return jsonify(0)




if __name__ == '__main__':

    app.run(host='localhost',port=8080)



