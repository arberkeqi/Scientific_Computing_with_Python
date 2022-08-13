def arithmetic_arranger(problems, answer = False):
  if len(problems) > 5:
    return False
  
  num1 = list()
  num2 = list()
  operators = list()

  for problem in problems:
    line = problem.split()
    num1.append(line[0])
    num2.append(line[2])
    operators.append(line[1])
  
  for i in range(len(problem)):
    if not (num1[i].isdigit() and num2[i].isdigit()):
      print("Error: Numbers must only contain digits.")

  for i in range(len(problem)):
    if len(num1[i] > 4 and num2[i] > 4):
      print("Error: Numbers cannot be more than four digits.")


  if operators == "*" or operators == "/":
    print("Error: Operator must be '+' or '-'.")
  



    # return arranged_problems