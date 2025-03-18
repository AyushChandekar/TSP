import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ayush@19"
)
cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS TODOAPP")
print("Database created...")

cursor.execute("USE TODOAPP")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tb_todo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task VARCHAR(50) NOT NULL,
        status ENUM('pending', 'completed') DEFAULT 'pending'
    )
''')
print("Table created...")

cursor.execute("SHOW TABLES")
for tbl in cursor:
    print(tbl[0])

while True:
    print("\nTask Management")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    user_choice = input("Enter your choice: ")

    if user_choice == '1':
        task_name = input("Enter task: ")
        cursor.execute("INSERT INTO tb_todo (task) VALUES (%s)", (task_name,))
        connection.commit()
        print("Task added successfully.")

    elif user_choice == '2':
        cursor.execute("SELECT * FROM tb_todo")
        all_tasks = cursor.fetchall()
        print("\nTasks:")
        for task in all_tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Status: {task[2]}")

    elif user_choice == '3':
        task_id = input("Enter task ID to update: ")
        new_status = input("Enter new status (pending/completed): ")
        cursor.execute("UPDATE tb_todo SET status = %s WHERE id = %s", (new_status, int(task_id)))
        connection.commit()
        print("Task updated successfully.")

    elif user_choice == '4':
        task_id = input("Enter task ID to delete: ")
        cursor.execute("DELETE FROM tb_todo WHERE id = %s", (int(task_id),))
        connection.commit()
        print("Task deleted successfully.")

    elif user_choice == '5':
        print("Exiting Task Management...")
        break

    else:
        print("Invalid choice. Please try again.")

connection.close()