import os, sys

sys.path.append(f"{os.path.dirname(os.path.abspath(__file__))}/../../lib")
from producer_class import KafkaProducer
from sqlite_lib import read_sensor_data
from sensor_lib import create_single_data_with_scenarios

# sensor_id 정보로 partition_number 반환
# kafka producer 생성
# sensor 로직에 producer 전달 후 메세지 생성

# define producer
conf = {'bootstrap.servers': 'localhost:9092'}
producer = KafkaProducer(conf)

# location
location_id = 8
sensor_id = 9

# define params
topic = f"location_{location_id}" 
key = str(sensor_id)
partition = read_sensor_data(location_id=location_id,
                             QUERY=f"""
                             SELECT partition_number FROM sensor
                             WHERE sensor_id = {sensor_id}
                             """)[0][0]

# define value 
scenarios = [
    {
        'topic': topic,
        'key': key,
        'partition': partition,
        'start_date': '2024-01-14_00:00',
        'mid_value': 120.0,
        'scope': 0.08,
        'decimal': 3,
        'cnt': 57600,
        'amount': 0
    }
]

# define main
def main():
    try:
        create_single_data_with_scenarios(producer, scenarios)
    except Exception as E:
        print(E) # <--- fix
        print("RESTARTING SCRIPT.") # <--- fix
        main()
        
if __name__ == "__main__":
    main()
    