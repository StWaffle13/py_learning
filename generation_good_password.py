# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

import random

# Наборы символов:
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_?"
spec_sim = "il1Lo0O"

chars = ""  # Содержит все символы, которые могут быть в генерируемом пароле


def check_answer_human(data_human):
    if data_human.lower() == "д":
        return True
    elif data_human.lower() == "н":
        return False


def start_generate_password(length, char):
    password = ""
    for i in range(length):
        password += random.choice(char)
    return password


# Начало
print("🤖💬 - Привет! Ты запустил генератор пароля.")
print("🤖💬 - Начнём генерацию?", "\n")
answer_human = input("Ваш ответ: (Д/Н) ")

# Согласие пользователя
if check_answer_human(answer_human) == True:
    print()
    print("🤖💬 - Какое кол-во паролей вам нужно?")
    amount_password = int(input("Нужное вам кол-во паролей: "))

    print()
    print("🤖💬 - Какую длинну пароля желаете?")
    length_password = int(input("Длинна ваших паролей: "))

    print()
    print("🤖💬 - Мне включить цифры в пароль?")
    answer_human_num_in_pass = input("Ваш ответ: (Д/Н)")
    if check_answer_human(answer_human_num_in_pass) == True:
        chars += digits

    print()
    print("🤖💬 - Мне включить прописные буквы в пароль?")
    answer_human_abc_in_pass = input("Ваш ответ: (Д/Н)")
    if check_answer_human(answer_human_abc_in_pass) == True:
        chars += lowercase_letters

    print()
    print("🤖💬 - Мне включить строчные буквы в пароль?")
    answer_human_ABC_in_pass = input("Ваш ответ: (Д/Н)")
    if check_answer_human(answer_human_ABC_in_pass) == True:
        chars += uppercase_letters

    print()
    print("🤖💬 - Мне включить спец.символы в пароль?")
    answer_human_spec_in_pass = input("Ваш ответ: (Д/Н)")
    if check_answer_human(answer_human_spec_in_pass) == True:
        chars += punctuation

    # Не реализовал пока что
    # print('🤖💬 - Исключить "плохие" символы?')
    # answer_human_badsim_in_pass = input("Ваш ответ: (Д/Н)")

    print()
    print("🤖💬 - Данные собраны. Начинаю генерацию...")
    if amount_password > 1:
        print(
            "🤖💬 - Ваши пароли:",
            "\n",
        )
        for _ in range(amount_password):
            print(start_generate_password(length_password, chars))
    else:
        print(
            "🤖💬 - Ваш пароль:",
            "\n",
        )
        print(start_generate_password(length_password, chars))
else:
    print("🤖💬 - Что-ж... Ладно. До встречи!", "\n")
