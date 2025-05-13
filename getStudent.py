import mysql.connector
def get_database_connection():
    connection = mysql.connector.connect(user='sadiah16',
                                         password='233001585',
                                         host='10.8.37.226',
                                         database='sadiah16_db')
    return connection

def execute_statement(connection, statement):
    cursor = connection.cursor()
    cursor.execute(statement)
    results = []

    for row in cursor:
        results.append(row)

    cursor.close()
    connection.close()

    return results

def get_student_schedule(student_id):
    statement = "CALL Get_Student_Schedule(" + student_id + ")"
    return execute_statement(get_database_connection(), statement)

student_id = input("Enter a student ID: ")
results = get_student_schedule(student_id)

for result in results:
    print("Period: " + str(result[1]))
    print("Course: " + result[2])
    print("Room: " + result[3])
    print("Teacher: " + result[4])
    print()