for j in range(int(input())):
    operators = input().strip()
    while ((operators.find("[]") > -1) or (operators.find("()") > -1)):
        operators = operators.replace("()", "")
        operators = operators.replace("[]", "")
    if (len(operators) == 0):
        print("Yes")
    else:
        print("No")