from flask import Flask,request,jsonify
import pandas as pd
import logging
from RiskEvent import RiskEvent
from Trigger import Trigger

app = Flask(__name__)



logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)




@app.route('/calculate', methods=['POST'])
def calculate():


    content = request.json
    logging.info(content)

    triggers = content['triggers']

    trigger_list = [Trigger() for i in triggers]
    objs = []

    for obj in trigger_list:
        objs.add(obj)



    logging.info(objs)


    triggers = []
    floods = Trigger(0.3, -0.8, -0.5)
    political = Trigger(0.2, -0.5, -0.12)
    triggers.append(floods)
    triggers.append(political)

    demand = RiskEvent(0.5, triggers)
    logging.info(demand.calculate_risk())
    return jsonify(demand.calculate_risk())




if __name__ == '__main__':

    app.run(host='localhost',port=8080)



