import os
nowdir = os.path.dirname(os.path.abspath(__file__))

def return_conn(database:str):
    from configparser import ConfigParser
    from mysql import connector
    import os
    
    # define config
    config = ConfigParser()
    config.read(f"{nowdir}/../config/config.ini")
    
    # return mysql params
    host = config.get("mysql", "host")
    user = config.get("mysql", "user")
    passwd = config.get("mysql", "passwd")

    # define configs & create conn
    config = {
        'user': user,
        'password': passwd,
        'host': host,
        'database': database
    }
    conn = connector.connect(**config)
    
    return conn
    
def update_sqlite_sensor(location_id:int):
    import sqlite3
    
    # define conn & cursor
    conn = return_conn(database="information")
    cursor = conn.cursor()
    
    # get data schemas
    cursor.execute(f"DESCRIBE sensor")
    columns = cursor.fetchall()
    
    # get datas
    cursor.execute(f"SELECT * FROM sensor WHERE location_id = {location_id}")
    datas = cursor.fetchall()
    print(datas)
    
    # close conn
    conn.close()
    
    # define sqlite conn & cursor
    sqlite_dir = f"{nowdir}/../database/sensor_{location_id}.db"
    sq_conn = sqlite3.connect(sqlite_dir)
    sq_cursor = sq_conn.cursor()
    
    # create table
    QUERY = f"CREATE TABLE IF NOT EXISTS sensor ("
    for column in columns:
        column_name = column[0]
        data_type = column[1]
        QUERY += f"{column_name} {data_type}, "
    QUERY = QUERY.rstrip(', ') + ")"
    sq_cursor.execute(QUERY)
    
    # insert data
    for row in datas:
        placeholders = ', '.join(['?' for _ in range(len(row))])
        QUERY = f"INSERT INTO sensor VALUES ({placeholders})"
        sq_cursor.execute(QUERY, row)
        sq_conn.commit()

if __name__ == "__main__":
    update_sqlite_sensor(location_id="4")
    update_sqlite_sensor(location_id="7")
    update_sqlite_sensor(location_id="8")
    