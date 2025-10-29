import mariadb
connection = mariadb.connect(
    host= '127.0.0.1',
    port= 3306,
    user='root',
    password='RadinB1385',
    database='people',
    autocommit=True
)
print("connected to MariaDB successfully")
def get_employees_by_last_name(connection, last_name):
    sql= "select number,last_name,first_name,salary from employee where last_name = ?"
    cursor = connection.cursor()
    cursor.execute(sql, (last_name,))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(f"Hello! im {row[2]} {row[1]} and my salary is {row[3]} euros per month")
    else:
        print(f"no employees with last name {last_name} found")
    cursor.close()
ln = input("Enter the last name of the employee whose salary you wish to check: ")
get_employees_by_last_name(connection, ln)
connection.close()
print("connection closed")