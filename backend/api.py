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

    trigger_list = [Trigger(i['probability'], i['impact'], i['edge_weight']) for i in triggers]
    objs = []

    for obj in trigger_list:
        objs.append(obj)



    logging.info(objs)




    demand = RiskEvent(0.5, objs)
    energy = RiskEvent(0.3, objs)
    production = RiskEvent(0.2, objs)


    d = demand.calculate_risk()
    e = energy.calculate_risk()
    p = production.calculate_risk()

    result = d + e + p
    
    logging.info(result)
    return jsonify(result)




if __name__ == '__main__':

    app.run(host='localhost',port=8080)



