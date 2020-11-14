def arithmetic_arranger(problems, solutions=False):
# Arranging vertically an arithmetic problem.

  l1 = ""
  l2 = ""
  l3 = ""
  l4 = ""
  
  for pair, case in enumerate(problems):
    numb1, symbol, numb2 = case.split()

    if not numb1.isdigit() or not numb2.isdigit():
      return "Error: Numbers must only contain digits."

    a = int(numb1)
    b = int(numb2)

    if symbol == "-":
      result = a - b
    else:
      result = a + b

    numb_len = len(max([numb1,numb2], key=len))

    l1 += numb1.rjust(numb_len + 2)
    l2 += symbol + numb2.rjust(numb_len + 1)
    l3 += "-" * (numb_len + 2)
    l4 += str(result).rjust(numb_len + 2)

    if pair < len(problems)-1:
      l1 += " " * (len(problems)-1)
      l2 += " " * (len(problems)-1)
      l3 += " " * (len(problems)-1)
      l4 += " " * (len(problems)-1)

    if not symbol in ["+", "-"]:
      return "Error: Operator must be '+' or '-'."

    if len(numb1) > 4 or len(numb2) > 4:
      return "Error: Numbers cannot be more than four digits."

  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = l1 + "\n" + l2 + "\n" + l3

  if solutions:
    arranged_problems += "\n" + l4

  return arranged_problems




print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))