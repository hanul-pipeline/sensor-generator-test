
def create_single_data(producer, topic, key, partition, mid_value:float, scope:float, decimal:int):
    from time import time, sleep
    from random import uniform
    
    while True:
        try:
            start = time()
            
            data = str(round(uniform(mid_value-scope, mid_value+scope), decimal))
            producer.publish_message_thread(topic=topic, key=key, partition=partition, message=data)
            
            end = time()
            sleep(1 - (end - start))
    
        except KeyboardInterrupt:
            break
        
        except Exception as E:
            print(E)


def create_single_data_with_senario(producer, topic, key, partition, mid_value:float, scope:float, decimal:int):
    from time import time, sleep
    from random import uniform
    
    while True:
        try:
            start = time()
            
            data = str(round(uniform(mid_value-scope, mid_value+scope), decimal))
            producer.publish_message_thread(topic=topic, key=key, partition=partition, message=data)
            
            end = time()
            sleep(1 - (end - start))
    
        except KeyboardInterrupt:
            break
        
        except Exception as E:
            print(E)