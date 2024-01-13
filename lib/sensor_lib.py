
def create_boolean_data_with_scenarios(producer, topic, key, partition, start_date, cnt):
    from datetime import datetime
    from time import time, sleep
    
    # index counter
    index = 0
    
    while True:
        try:
            start = time()
        
            # check nowdate & run scenario task
            nowdate = datetime.now().strftime("%Y-%m-%d_%H:%M")
            if nowdate == start_date:
                index += 1
                print(1)
                producer.publish_message_thread(topic=topic, key=key, partition=partition, message="1")
                if index == cnt:
                    break
            else:
                print(0)
                producer.publish_message_thread(topic=topic, key=key, partition=partition, message="0")
                
            # set period as 1
            end = time()
            sleep(1 - (end - start))
    
        except KeyboardInterrupt:
            break
        
        except Exception as E:
            print(E)

def create_single_data_with_scenarios(producer, scenarios):
    from time import time, sleep
    from datetime import datetime
    from random import uniform
    
    for scenario in scenarios:
        try:
            # index counter
            index = 0
            
            while True:
                start = time()
                
                # check nowdate & run scenario task
                nowdate = datetime.now().strftime("%Y-%m-%d_%H:%M")
                if nowdate == scenario['start_date']:
                    index += 1
                    data = str(round(uniform(scenario['mid_value']-scenario['scope'], scenario['mid_value']+scenario['scope']), scenario['decimal']) + index * scenario['amount'])
                    print(data)
                    producer.publish_message_thread(topic=scenario['topic'], key=scenario['key'], partition=scenario['partition'], message=data)
                    
                    if index == scenario['cnt']:
                        break
                
                # run normal task
                else:
                    data = str(round(uniform(scenario['mid_value']-scenario['scope'], scenario['mid_value']+scenario['scope']), scenario['decimal']))
                    print(data)
                    producer.publish_message_thread(topic=scenario['topic'], key=scenario['key'], partition=scenario['partition'], message=data)     
                
                # set period as 1
                end = time()
                sleep(1 - (end - start))
                
        except KeyboardInterrupt:
            break
        
        except Exception as E:
            print(E)
            
