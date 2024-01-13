#!/bin/bash

# Need to run `chmod +x ./run-sensors.sh` to use this script.

# find abs path
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# run sensors
nohup python3 "$DIR/../src/location_4/sensor_1.py" & > "$DIR/../log/sensor_1.log"
nohup python3 "$DIR/../src/location_4/sensor_2.py" & > "$DIR/../log/sensor_2.log"

nohup python3 "$DIR/../src/location_7/sensor_3.py" & > "$DIR/../log/sensor_3.log"
nohup python3 "$DIR/../src/location_7/sensor_4.py" & > "$DIR/../log/sensor_4.log"
nohup python3 "$DIR/../src/location_7/sensor_5.py" & > "$DIR/../log/sensor_5.log"
nohup python3 "$DIR/../src/location_7/sensor_6.py" & > "$DIR/../log/sensor_6.log"

nohup python3 "$DIR/../src/location_8/sensor_7.py" & > "$DIR/../log/sensor_7.log"
nohup python3 "$DIR/../src/location_8/sensor_8.py" & > "$DIR/../log/sensor_8.log"
nohup python3 "$DIR/../src/location_8/sensor_9.py" & > "$DIR/../log/sensor_9.log"
