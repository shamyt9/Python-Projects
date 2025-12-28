import sys
choice=(sys.argv[1])
num1=int(sys.argv[2])
num2=int(sys.argv[3])

match choice:
  case "+":
    print(num1+num2)
  case "-":
    print(num1-num2)
  case _:
    print("invalid")
     


