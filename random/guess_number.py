import random
print('Я загадал число от 1 до 100, попробуй угадать!')

secret = random.randint(1, 100)
attempt = 0

while True:
    user_input = int(input('Введи число: '))
    attempt += 1  

    if user_input < secret:
        print('БОЛЬШЕ')
    elif user_input > secret:
        print('МЕНЬШЕ')
    else:
        print(f"Вы угадали! Это было числ: {secret}.")
        print(f"Количество попыток: {attempt}")
        break