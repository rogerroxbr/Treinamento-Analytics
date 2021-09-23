def arithmetic_arranger(problems, showResults=False):
    results = []
    firstNums = []
    secondNums = []
    operations = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        prob = problem.split()
        firstNums.append(prob[0])
        secondNums.append(prob[2])
        operations.append(prob[1])

        if not prob[0].isdigit() or not prob[2].isdigit():
            return "Error: Numbers must only contain digits."

        if len(prob[0]) > 4 or len(prob[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if showResults:
            if prob[1] == "+":
                results.append(int(prob[0]) + int(prob[2]))
            elif prob[1] == "-":
                results.append(int(prob[0]) - int(prob[2]))
            else:
                return "Error: Operator must be '+' or '-'."

    firstLine = ""
    secondLine = ""
    thirdLine = ""
    fourthLine = ""

    for i in range(len(firstNums)):
        if len(firstNums[i]) > len(secondNums[i]):
            firstLine += "  " + firstNums[i] + "    "
            secondLine += operations[i] + " " * (len(firstNums[i]) - len(secondNums[i]) + 1) + secondNums[i] + "    "
            thirdLine += "-" * (len(firstNums[i]) + 2) + "    "

            if showResults:
                if len(str(results[i])) < len(firstNums[i]):
                    fourthLine += " " * (len(firstNums[i]) - len(str(results[i])) + 3) + str(results[i]) + "    "
                elif len(str(results[i])) > len(firstNums[i]):
                    fourthLine += " " + str(results[i]) + "    "
                else:
                    fourthLine += "  " + str(results[i]) + "    "

        elif len(firstNums[i]) <= len(secondNums[i]):
            secondLine += operations[i] + " " + secondNums[i] + "    "
            firstLine += " " * (len(secondNums[i]) - len(firstNums[i]) + 2) + firstNums[i] + "    "
            thirdLine += "-" * (len(secondNums[i]) + 2) + "    "

            if showResults:
                if len(str(results[i])) < len(secondNums[i]):
                    fourthLine += " " * (len(secondNums[i]) - len(str(results[i])) + 3) + str(results[i]) + "    "
                elif len(str(results[i])) > len(secondNums[i]):
                    fourthLine += " " + str(results[i]) + "    "
                else:
                    fourthLine += "  " + str(results[i]) + "    "

    arranged_problems = firstLine + "\n" + secondLine + "\n" + thirdLine + "\n" + fourthLine

    return arranged_problems


print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
