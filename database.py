import sqlite3


def createTable():
    connection = sqlite3.connect("reminder.db")
    connection.execute("DROP TABLE record")
    connection.execute("CREATE TABLE record(TOPIC TEXT NOT NULL,DECSRIPTION,DATE date,TIME time)")

    connection.execute("INSERT INTO record VALUES(?,?,?,?)",("prasanan",9074401415,"2019-08-18","07:00:00"))

    connection.commit()
    result = connection.execute("SELECT * FROM record")
    print(result)

    for data in result:
       
        print("name: ", data[0])
        print("description: ", data[1])
        print("date: ", data[2])
        print("time: ", data[3])
        
    connection.close()
createTable()    
    
        
