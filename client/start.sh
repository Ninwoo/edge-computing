#!/bin/bash
cd /tmp/cut_pic/
python tcpsign.py 10.0.9.55 &
python serverfile.py 60000 &
python tcpserver.py  33332 &
python cpuserver.py 12222 &
python join.py '''[ip]''' &