print("-------------------------------------------")
print("Добро пожаловать в финансовый калькулятор")
print("-------------------------------------------")
while True:
    num1 = int(input("введите первое число:"))
    num2 = int(input("введите второе число:"))
    sign_operation = input("знак операции(+ - * / // % **) or exit для выхода: ")
    if sign_operation == 'exit':
        print("Выход из калькулятора")
        break
    if sign_operation == '+':
        result = num1 + num2
        print(result)
    elif sign_operation == '-':
        result = num1 - num2
        print(result)
    elif sign_operation == '*':
        result = num1 * num2
        print(result)
    elif sign_operation == '/':
        result = num1 / num2
        print(result)
    elif sign_operation == '//':
        result = num1 // num2
        print(result)
    elif sign_operation == '%':
        result = num1 % num2
        print(result)
    elif sign_operation == '**':
        result = num1 ** num2
        print(result)
    else:
        print("нет решения")
