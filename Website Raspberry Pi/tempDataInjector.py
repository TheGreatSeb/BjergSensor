#Injector for temp

import sqlite3

#Connecting to Database
conn = sqlite3.connect('database/main.db')
memoryConn = sqlite3.connect(':memory:')
cur = conn.cursor()
#reading text file
text_file = open("data/temp.txt", "r")
lines = text_file.readlines()
lines[0]
print(lines)
#writing text data into database
for line in lines:
    cur.execute('INSERT INTO temp (T) VALUES (' + str(int(line)) + ');')
conn.commit()
text_file.close()
conn.close()