#Importing the ascii art
from art import logo

#Defining the functions
#Addition
def add(n1, n2):
    return n1 + n2

# Substraction
def subtract(n1, n2):
    return n1 - n2

# multiplication
def multiply(n1, n2):
    return n1 * n2

# division
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

#Defining the calculator
def calculator():
#printing the art
  print(logo)
#Prompts the user to input a number
  num1 = float(input("What is the first number: "))
#loops through the operations dictionary and prints out the symbols
  for symbol in operations:
      print(symbol)
#Condition for a while loop
  calc_on = True
#While loop to ensure the program repeats
  while calc_on:
#Promts the user to input an operation symbol
      operation_symbol = input("Pick an operation: ")
#Promts the user to input the next number
      num2 = float(input("What's the next number: "))
#Subset the funtion from the operations dictionary with the symbol inputed by the user
      calculator_function = operations[operation_symbol]
#calls the function, calculate the input and save the result to the answer variable
      answer = calculator_function(num1, num2)
#Prints out the calculation as an equation with the answer
      print(f"{num1} {operation_symbol} {num2} = {answer}")
#Asks the user if they would like to continue calculating with the previous result, start afresh or exit the program
      calc = input(
          f"Type 'y' to continue calculating with {answer} or Type 'n' to start a new calculation or 'x' to quit the program: "
      )
#if the user wants to continue with the previous result  num1 = answer
      if calc.lower() == 'y':
          num1 = answer
#if the user enters 'x' the program will end
      elif calc.lower() == 'x':
          calc_on = False
#if the user enters 'n' the program will start afresh
      else:
          calc_on = False
          calculator()
#calling the function
calculator()
