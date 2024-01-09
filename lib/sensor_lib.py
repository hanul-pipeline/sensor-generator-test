from configparser import ConfigParser
import os, sys

now_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from kafka_lib import *

def sensor_module():
    pass

def create_single_data(sensor_info:dict, ):
    from threading import Thread
    from time import time, sleep
    from datetime import datetime
    from random import uniform
    
    mid_value = sensor_info["mid_value"]
    scope = sensor_info["scope"]
    decimal_unit = sensor_info["decimal_unit"]
    
    while True:
        try:
            start = time()
            
            nowdate = datetime.now()
            date_info = nowdate.strftime("%Y-%m-%d")
            time_info = nowdate.strftime("%H:%M:%S")
            data = round(uniform(mid_value-scope, mid_value+scope), decimal_unit)
            print(date_info + "\n" + time_info + "\n" + str(data))
            
            end = time()
            sleep(1 - (end - start))
    
        except KeyboardInterrupt:
            break
        
        except Exception as E:
            print(E)
            
def sensor_module():
    