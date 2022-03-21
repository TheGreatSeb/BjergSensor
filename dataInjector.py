import sqlite3

#Connecting to Database
conn = sqlite3.connect('database/test.db')
memoryConn = sqlite3.connect(':memory:')
cur = conn.cursor()
#reading text file
text_file = open("data/test.txt", "r")
lines = text_file.readlines()
print(lines)
#writing text data into database
for line in lines:
    cur.execute('INSERT INTO temp (T) VALUES (' + str(int(line)) + ');')
conn.commit()
text_file.close()
conn.close()