sftp algae@172.20.10.7 << stopping
    put data/test.txt
    exit
stopping

cat data/test.txt >> data/data.log
echo "" > data/test.txt
