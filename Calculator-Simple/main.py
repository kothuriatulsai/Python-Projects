def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


dic = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calc():
  from art import logo

  print(logo)

  
  go = True
  n1 = float(input("What is the first number? "))
  n2 = float(input("What is the second number? "))
  if n1 == int(n1):
    n1 = int(n1)
  if n2 == int(n2):
    n2 = int(n2)
  while go:
    for i in dic:
        print(i)

    op_sym = input("Pick an operation from the line above: ")

    k = dic[op_sym](n1, n2)
    if k == int(k):
      k = int(k)

    print(f"{n1} {op_sym} {n2} = {k}")
    go_to = input(f"Type 'y' to continue calculating with {k}, or type 'n' to start a new calculator: ")
    go_on = False
    if go_to == 'y':
      go_on = True
    else:
      go = False
      calc()
    while go_on:
      op_sym = input("Pick an operation: ")
      n3 = float(input("What is the next number? "))
      if int(n3) == n3:
        n3 = int(n3)
      k1 = dic[op_sym](k, n3)
      if k1 == int(k1):
        k1 = int(k1)
      print(f"{k} {op_sym} {n3} = {k1}")
      k = k1
      go_to = input(f"Type 'y' to continue calculating with {k}, or type 'n' to start a new calculator: ")
      if go_to == "y":
        go_on = True
      else:
        go_on = False
        go = False
        calc()

calc()
