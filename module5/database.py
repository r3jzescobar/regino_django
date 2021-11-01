from typing import final
import psycopg2

try:
    conn =psycopg2.connect(host ='127.0.0.1', port ='5432',user = 'postgres', password ='postgres123',
        database = 'testdb')
    cursor = conn.cursor()
    #print(conn.get_dsn_parameters(),"\n")
    cursor.execute("select version();")
    record = cursor.fetchone()
    print(f"You are connected to the server - {record}", "\n")

    create_table_query = """CREATE TABLE IF NOT EXISTS employee
    (ID INT PRIMARY KEY NOT NULL, NAME VARCHAR(50) NOT NULL,
    ADDRESS TEXT, DEPT VARCHAR(50))
    """
    cursor.execute(create_table_query)
    print("table created sucessfully")

    #insert query
    # insert_query = """INSERT INTO employee(ID , NAME , DEPT,ADDRESS)VALUES
    # (%s, %s , %s, %s)"""
    # record_to_insert1=(1,"sam", "Delhi", "HR")
    # record_to_insert2=(2,"Gian", "MANILA", "CHEF")
    # cursor.execute(insert_query, record_to_insert1)
    # cursor.execute(insert_query, record_to_insert2)
    # conn.commit()
    # count = cursor.rowcount
    # print(f"{count} record successfully")
    
    select_query = "select * from employee"
    cursor.execute(select_query,(1))
    records = cursor.fetchall()
    print(f"records sucessfully")
    print("ID", "NAME", "ADDRESS","DEPT")
    for row in records:
        print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
    print(f"records in employees:{records}")

    # update_query= "UPDATE employee set NAME = %s where NAME = %s"
    # cursor.execute(update_query,("Karl" , "Sam"))
    print("Record updated")
    # conn.commit()
    # select_query = "select * from employee"
    # cursor.execute(select_query)
    # records=cursor.fetchall()
    # print(f"records in employees:{records}")

    delete_query = "DELETE FROM employee  where ID = %s"
    cursor.execute(delete_query,(2, ))
    print("record deleted")
    select_query = "select * from employee"
    cursor.execute(select_query)
    records=cursor.fetchall()
    print(f"records in employees:{records}")
      

except Exception as err:
    print(f"unable to connet to DB. Error:{str(err)}")

finally:
    conn.close()
    cursor.close()





