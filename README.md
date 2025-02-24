# Todo List & Fibonacci Series with PostgreSQL

# Project Description

This project demonstrates two main functionalities:

Fibonacci Series Generator: A Python function that generates the Fibonacci sequence up to a specified number of terms.

To-Do List Management using PostgreSQL: A set of Python functions that allow users to create, update, retrieve, and delete tasks from a PostgreSQL database.

# Requirements

Ensure you have the following installed:

Python 3.10

PostgreSQL

psycopg2 (PostgreSQL adapter for Python)

To install psycopg2, run:

    pip install psycopg2

# Database Setup

Before running the code, ensure that:

PostgreSQL is installed and running.

A PostgreSQL database named my_database exists.

The user credentials (myuser, my**\*\*\***) have the necessary permissions.

The database connection parameters match your PostgreSQL setup.

# How to Run the Project

1. Fibonacci Series Generator

The function Fibonacci(n) generates the first n terms of the Fibonacci sequence. Example usage:

n_terms = 10
fib_series = Fibonacci(n_terms)
print(f"\nFibonacci Series up to {n_terms} terms: {fib_series}")

2. To-Do List Management

Create Database Connection

create_connection()

Create the To-Do Table

create_table()

Add a Task

add_task("Complete Python assignment")

Retrieve All Tasks

get_tasks()

Update Task Status

update_task(task_id=1, status=True)

Delete a Task

delete_task(task_id=1)

# Code Overview

Fibonacci Sequence: Implements a function to generate Fibonacci numbers.

# Database Functions:

create_connection(): Establishes a connection to PostgreSQL.

create_table(): Creates the Todo table if it doesn’t exist.

add_task(task): Inserts a new task.

get_tasks(): Fetches all tasks.

update_task(task_id, status): Updates a task's status.

delete_task(task_id): Removes a task.

# Expected Output

Connection to the database successful
✅ Todo Table Created Successfully
✅ Task 'Complete Python assignment' added successfully
✅ Task 'Read a book' added successfully
✅ Task 'Update the book' added successfully

Todo List:
(1, 'Complete Python assignment', False)
(2, 'Read a book', False)
(3, 'Update the book', False)

✅ Task with id 1 updated successfully

Todo List:
(1, 'Complete Python assignment', True)
(2, 'Read a book', False)
(3, 'Update the book', False)

# License

This project is open-source and free to use.
