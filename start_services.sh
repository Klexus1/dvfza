#!/bin/sh

service ssh start &
python3 -m flask run --host=0.0.0.0 &
sleep infinity