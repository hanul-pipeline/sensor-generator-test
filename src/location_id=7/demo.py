from configparser import ConfigParser
import os, sys

now_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{os.path.dirname(os.path.abspath(__file__))}/../../lib")

from kafka_lib import *

conf = ..
num_partitions = ..

def demo(sensor_info:dict):
    from time import time, sleep
    from datetime import datetime
    from random import uniform
    
    sensor_id = sensor_info["id"]
    mid_value = sensor_info["mid_value"]
    scope = sensor_info["scope"]
    decimal_unit = sensor_info["decimal_unit"]
    
    while True:
        cnt = 0
        try:
            start = time()
            
            nowdate = datetime.now()
            date_info = nowdate.strftime("%Y-%m-%d")
            datetime_info = nowdate.strftime("%Y-%m-%d %H:%M:%S")
            value = round(uniform(mid_value-scope, mid_value+scope), decimal_unit)
            
            topic = sensor
            message = {
                "sensor_id": sensor_id,
                "datetime": datetime_info,
                "measurement": value
            }
            
            publish_message_json(conf, topic, key, message)
            
            cnt += 1
            cnt = 0 if cnt == num_partitions else cnt
                
            end = time()
            sleep(1 - (end - start))
    
        except KeyboardInterrupt:
            break
        
        except Exception as E:
            print(E)