import os
nowdir = os.path.dirname(os.path.abspath(__file__))

def read_sensor_data(location_id:int, QUERY:str):
    import sqlite3, os
    
    sqlite_dir = f"{os.path.dirname(os.path.abspath(__file__))}/../database/sensor_{location_id}.db"
    sq_conn = sqlite3.connect(sqlite_dir)
    sq_cursor = sq_conn.cursor()
    
    sq_cursor.execute(QUERY)
    result = sq_cursor.fetchall()
    
    return result

if __name__ == "__main__":
    QUERY = "SELECT * FROM sensor;"
    result = read_sensor_data(location_id=8, QUERY=QUERY)
    print(result)