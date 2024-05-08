
import mysql.connector as mycoon


mydb = mycoon.connect(host="localhost",user="root",password="student",database="Connection")
cur = mydb.cursor()

def insert(rollno, name, address):
    
    query = "INSERT INTO student (rollno, name, address) VALUES (%s, %s, %s)"
    values = (rollno, name, address)
    cur.execute(query, values)
    mydb.commit()
    print("Row is inserted successfully")
    
def update(rollno, new_address):
    
    query = "UPDATE student SET address = %s WHERE rollno = %s"
    values = (new_address, rollno)
    cur.execute(query, values)
    mydb.commit()
    print("Row is updated successfully")
    
def delete(rollno):
    
    query = "DELETE FROM student WHERE rollno = %s"
    values = (rollno,)
    cur.execute(query, values)
    mydb.commit()
    print("Row is deleted successfully")
    
while True:
    operation = int(input("enter operation value (1=insert/2=update/3=delete): "))

    if operation == 1:
        r = int(input("Enter the rollno: "))
        n = input("Enter the name: ")
        a = input("Enter the address: ")
        insert(r, n, a)

    elif operation == 2:
        r = int(input("Enter the rollno for the update: "))
        new_address = input("Enter the new address: ")
        update(r, new_address)

    elif operation == 3:
        r = int(input("Enter the rollno to delete: "))
        delete(r)
    else:
        break


mydb.close()
