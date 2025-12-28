import sys
import random as rd
import datetime

num1=int(sys.argv[1])
operator=(sys.argv[2])
num2=int(sys.argv[3])


  
def add(a,b):return a+b
def sub(a,b):return a-b
def mul(a,b):return a*b
def divide(a,b):
  if b==0:
    raise ZeroDivisionError("cant divide by zero")
  return a/b
  
  
def per(a,b):
  return a/b*100



operations={"+":add(num1,num2),
            "-":sub(num1,num2),
            "*":mul(num1,num2),
            "/":divide(num1,num2),
            "**":pow(num1,num2),
            "%":per(num1,num2),
            "rand":lambda a,b:rd.randint(a,b)
            }

# INPUT VALIDATION
if not sys.argv[1].isdigit() or sys.argv[2] not in operations or not sys.argv[3].isdigit() or len(sys.argv)>4:
  print("Usage: python CLI_CALCULATOR.py <num1> <operator> <num2>")
  sys.exit()

    
try:
    result = operations[operator](num1, num2)
    print("Result:", result)

    # ---------- History Logging ----------
    with open("history.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"Calculation: {num1} {operator} {num2} = {result}\n")
        file.write("-" * 50 + "\n")

except Exception as e:
    print("Error:", e)
      
    
    
