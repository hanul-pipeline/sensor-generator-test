import os, sys

sys.path.append(f"{os.path.dirname(os.path.abspath(__file__))}/../../lib")
from producer_class import KafkaProducer
from sqlite_lib import read_sensor_data
from sensor_lib import create_single_data

# sensor_id 정보로 partition_number 반환
# kafka producer 생성
# sensor 로직에 producer 전달 후 메세지 생성

# define producer
conf = {'bootstrap.servers': 'localhost:9092'}
producer = KafkaProducer(conf)

# location
location_id = 7
sensor_id = 3

# define params
topic = f"location_{location_id}" 
key = str(sensor_id)
partition = read_sensor_data(location_id=location_id,
                             QUERY=f"""
                             SELECT partition_number FROM sensor
                             WHERE sensor_id = {sensor_id}
                             """)[0][0]

# define value
mid_value = 30
scope = 10
decimal = 2

# start creating datas
create_single_data(producer=producer, topic=topic, key=key, partition=partition, 
                   mid_value=mid_value, scope=scope, decimal=decimal)
