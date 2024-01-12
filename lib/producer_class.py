from confluent_kafka import Producer
from time import time
from threading import Thread

class KafkaProducer:
    def __init__(self, conf:dict):
        self.conf = conf
        self.producer_client = Producer(conf)
        # print("Kafka producer created successfully.") # test
        
        #         threads = []
        # threads.append(Thread(target = self.insert_measurement_to_mysql, args = (key, value, nowdate)))
        # threads.append(Thread(target = self.define_grade, args = (topic, key, value, nowdate)))
        # for thread in threads:
        #     thread.start()
    
    def publish_message_thread(self, topic:str, key:str, message, partition:int=None):
        
        def publish_message(data:dict):
            try:
                if data["partition"] == None:
                    self.producer_client.produce(topic = data['topic'], key = data['key'], value = data['message'], timestamp=data['timestamp'])
                else:
                    self.producer_client.produce(topic = data['topic'], key = data['key'], value = data['message'], partition = data['partition'], timestamp=data['timestamp'])
                self.producer_client.flush()
                print(f'Message published successfully to topic {topic}.')
            
            except Exception as E:
                print(E)
        
        timestamp = int(time())
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
    conf = {'bootstrap.servers': 'localhost:9092'}
    producer = KafkaProducer(conf)
    producer.publish_message_thread(topic="location_4", key="1", partition=0, message="40")
    