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
def update_salary(connection, number, new_salary):
    sql = "UPDATE employee SET salary = ? where number = ?"
    cursor = connection.cursor()
    cursor.execute(sql, (new_salary,number))
    connection.commit()
    if cursor.rowcount != 0:
        print("Salary updated successfully!")
    else:
        print("No employee with number {number} found.")
number = input("Enter a number: ")
new_salary = input("Enter a new salary : ")
update_salary(connection, number, new_salary)
connection.close()