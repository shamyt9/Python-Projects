A command-line based calculator built using Python that performs basic and advanced arithmetic operations using command-line arguments.
The project also logs every calculation with a timestamp, making it a practical example of CLI tools, file handling, and error handling in Python.

🚀 Features

Perform calculations directly from the command line

Supports multiple arithmetic operations:

Addition (+)

Subtraction (-)

Multiplication (*)

Division (/) with zero-division handling

Power (**)

Percentage (%)

Random number generation (rand)

Input validation for safe execution

Automatic calculation history logging with date & time

Clean and simple CLI interface

🛠️ Technologies & Libraries Used

sys – to read command-line arguments

random – to generate random numbers

datetime – to log timestamps

File Handling – to store calculation history

📌 How It Works

The calculator takes three command-line arguments:

First number

Operator

Second number

Example:

python CLI_CALCULATOR.py 10 + 5


Output:

Result: 15


Each calculation is saved in a history.txt file with a timestamp.

🧾 Sample History Log
Timestamp: 12-01-2025 10:45:30
Calculation: 10 + 5 = 15
--------------------------------------------------

⚠️ Input Validation & Error Handling

Ensures correct number of arguments

Prevents invalid operators

Handles division by zero gracefully

Displays usage instructions for incorrect input

📚 Learning Outcomes

Understanding command-line applications

Using Python built-in libraries effectively

Implementing input validation and exception handling

Working with files for logging and persistence

Writing clean and modular Python functions

🔮 Future Improvements

Support floating-point numbers

Interactive mode (without CLI arguments)

Export history to JSON or CSV

Add unit testing

📄 Usage Syntax
python CLI_CALCULATOR.py <num1> <operator> <num2>

⭐ Why This Project?

This project is ideal for beginners who want to:

Learn how real CLI tools work

Practice Python standard libraries

Build resume-ready automation projects
