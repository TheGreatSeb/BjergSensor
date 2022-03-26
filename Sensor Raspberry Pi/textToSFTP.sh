sftp pi@192.168.137.21 << stopping
    put data/TDS.txt
    put data/temp.txt
    exit
stopping

rm TDS.txt && rm temp.txt