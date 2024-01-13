from confluent_kafka import Producer
from time import time
from threading import Thread

class KafkaProducer:
    def __init__(self, conf:dict):
        self.conf = conf
        self.producer_client = Producer(conf)
    
    def publish_message_thread(self, topic:str, key:str, message, partition:int=None):
        # define function (based on dict infos)
        def publish_message(data:dict):
            try:
                if data["partition"] == None:
                    self.producer_client.produce(topic = data['topic'], key = data['key'], value = data['message'], timestamp=data['timestamp'])
                else:
                    self.producer_client.produce(topic = data['topic'], key = data['key'], value = data['message'], partition = data['partition'], timestamp=data['timestamp'])
                self.producer_client.flush()
            
            except Exception as E:
                print(E)
        
        # add timestamp
        timestamp = int(time())
        
        # define dict & start thread
        try:
            data = {
                'topic': topic,
                'key': key,
                'partition': partition,
                'message': message,
                'timestamp': timestamp
            }
            thread = Thread(target = publish_message, args=(data,))
            thread.start()
        
        except Exception as E:
            print(f'Error appeared while publising message to topic {topic}. - {E}')

if __name__ == "__main__":
    pass
    # test to write json messages
    # import json
    # conf = {'bootstrap.servers': 'localhost:9092'}
    # producer = KafkaProducer(conf)
    # producer.publish_message_thread(topic="location_7", key="3", partition=0, message=json.dumps({'value': 66, 'key': 3}).encode('utf-8'))
    