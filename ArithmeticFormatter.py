def arithmetic_arranger(problems, answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    for problem in problems:
        operands = problem.split()
        if operands[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not operands[0].isdigit() or not operands[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(operands[0]) > 4 or len(operands[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(operands[0]), len(operands[2])) + 2
        line1 += operands[0].rjust(width) + '    '
        line2 += operands[1] + ' ' + operands[2].rjust(width - 2) + '    '
        line3 += '-' * width + '    '
        if answers:
            if operands[1] == '+':
                res = int(operands[0]) + int(operands[2])
            else:
                res = int(operands[0]) - int(operands[2])
            line4 += str(res).rjust(width) + '    '

    arranged_problems = line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip()
    if answers:
        arranged_problems += '\n' + line4.rstrip()

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')