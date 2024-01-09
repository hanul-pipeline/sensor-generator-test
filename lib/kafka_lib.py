from confluent_kafka import Producer

def publish_message(conf, topic:str, key:str, message):
    try:
        producer = Producer(conf)
        producer.produce(topic=topic, key=key, value=message)
        producer.flush()
    except Exception as E:
        print(E)

def publish_message_json(conf, topic:str, key:str, message:dict):
    import json
    
    try:
        producer = Producer(conf)
        producer.produce(topic=topic, key=key, value=json.dumps(message).encode('utf-8'))
        producer.flush()
    except Exception as E:
        print(E)
