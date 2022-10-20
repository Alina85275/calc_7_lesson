import operations_rational as op
import sys

def x():
    firstnum = float(input('Выберите первое рациональное число: ').replace(',', '.'))
    return firstnum

def y():
    secondnum = float(input('Выберите второе рациональное число: ').replace(',', '.'))
    return secondnum

def selectoperation():
    global operation
    operation = (input(f'Выберите оператор: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Неверный синтаксис')

def res(firstnum, secondnum):
    if  operation == '+':
        res = firstnum + secondnum
        result = round(res, 3)
        return result
    elif operation == '-':
        res = firstnum - secondnum
        result = round(res, 3)
        return result
    elif operation == '*':
        res = firstnum * secondnum
        result = round(res, 3)
        return result
    elif operation == '/':
        res = firstnum / secondnum
        result = round(res, 3)
        return result
    else:
        print('Неверный синтаксис')

def mainterminal():
    global file
    x = op.x()
    while True:
        y = op.y()
        oper = op.selectoperation()
        res = op.res(x, y)
        file = 'results.txt'
        with open('results.txt', 'a') as data:
            data.write(f'the result of {x} {oper} {y} = {res}\n')
        print(f'the result of {x} {oper} {y} = {res}\n(записано в txt file)' )
        again = input('Вы хотите рассчитать другие числа? Yes/No: ').lower()
        if again == 'yes':
            useresult = input('Вы хотите использовать результат последней операции? Yes/No: ').lower()
            if useresult == 'yes':
                x = res
                continue
            elif useresult == 'no':
                break
            else:
                sys.exit()           
        else:   
            sys.exit()