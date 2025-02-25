import psycopg2

# Fibonacci series generator
def Fibonacci(n):
    """Generates Fibonacci series up to n terms."""
    fib_series = [0, 1] # start with the first two numbers of the Fibonacci sequence
    while len(fib_series) < n: # keep generating numbers until we reach `n` terms
        fib_series.append(fib_series[-1] + fib_series[-2]) # sum of the last two numbers
    return fib_series[:n] # return only the first `n` numbers

# usage 
n_terms = 10
fib_series = Fibonacci(n_terms)
print(f"\nFibonacci Series up to {n_terms} terms: {fib_series}")

# Todo List with postgresql database
def create_connection():
    """Establishes a connection with the postgresql database."""
    try:
        conn = psycopg2.connect(
            dbname="my_database",
            user="myuser",
            password="mypassword",
            host="localhost",
            port="5432"
        )
        print("Connection to the database successful")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
    
def create_table():
    """Creates a Todo table in the database."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Todo (
                    id SERIAL PRIMARY KEY,
                    task TEXT NOT NULL,
                    status BOOLEAN NOT NULL DEFAULT FALSE
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Todo Table Created Successfully")

def add_task(task):
    """Add a new task to the Todo list Table."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Todo (task) VALUES (%s)", (task,))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"✅ Task '{task}' added successfully")

def get_tasks():
    """Retrieve all tasks from the Todo list."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, task, status FROM Todo")
        tasks = cursor.fetchall()
        cursor.close()
        conn.close()
        print("\n Todo List:")
        for task in tasks:
            print(task)
        return tasks
    
def update_task(task_id, status):
    """Update the status of a task by task id."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Todo SET status = %s WHERE id = %s", (status, task_id))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"✅ Task with id {task_id} updated successfully")

def delete_task(task_id):
    """delete a task from the Todo list using the task id."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Todo WHERE id = %s", (task_id,))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"🗑️ Task {task_id} Deleted")

# initialize the Todo table
create_table()

# usage of the Todo list functions
add_task("Oh baby i think i wanna marry you.")
#add_task("Read a book")
#add_task("Update the book")
get_tasks() # to view all the tasks
#update_task(18, True) # update task ID 18 
#get_tasks() # view updated tasks
