# Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число. Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'. Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'. Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.

import random

# Списки ответов для робота:
seq_word_for_damage_up = [
    '🤖💬 "Твоё число больше, ну давай ещё одну догадку."',
    '🤖💬 "Ну как так-то!? Пробуй ещё раз. Ближе к 99"',
    '🤖💬 "Эх.. Я могу вечно так продолжать, а вот ты нет! Число слишком большое."',
]

seq_word_for_damage_down = [
    '🤖💬 "Твоё число меньше, попытка не пытка. (Пока есть НР 😁)"',
    '🤖💬 "Тебе не отгадать это число! Ха-ха... Твоё число меньше!"',
    '🤖💬 "И снова ошибка! Слишком маленькое число."',
]

seq_word_for_win = [
    '🤖💬 "У тебя получилось, поздравляю!"',
    '🤖💬 "В точку! Поздравляю, ты угадал"',
    '🤖💬 "КАК!? Тебе просто повезло! Ты угадал..."',
]


# Функция проверки игрока на согласие:
def ansver_player_yes_or_no(ansver):
    if ansver == "Да":
        return True
    elif ansver == "Нет":
        return False


# Функция проверки игрока на "Дурока" (Правильный ввод в строку):
def is_valide(data_of_player):
    if data_of_player.isdigit() and 1 <= int(data_of_player) <= 100:
        return True
    else:
        return False


# Функция запуска игры:
def play_game():

    # Настройки игры:
    count_step = 0
    rand_num = random.randint(1, 100)
    heal_player = ["❤️", "❤️", "❤️", "❤️", "❤️", "❤️"]
    seq_damage_icons = ["⚡", "🧨💥"]

    # Игра:
    print(
        "🤖💬 - Отлично! Я загадал число от 1 до 100, твоя задача отгадать. Твой первый вариант?"
    )
    while True:
        if count_step == 6:
            print("GAME OVER 🤕", "\n")
            print("🤖💬 - Попробуем ещё раз?")
            ansver_player_1 = input("Ваш ответ: (Да/Нет) ")
            if ansver_player_yes_or_no(ansver_player_1) == True:
                play_game()
            else:
                print("🤖💬 - Что-ж... Жаль... Ну ладно, до встречи!")
                break

        ansver_player_1 = input("Ваша догатка: (число) ")
        if is_valide(ansver_player_1) == True:
            num_player = int(ansver_player_1)
            if num_player < rand_num:  # Промах -1hp💔
                heal_player[count_step] = "💔"
                count_step += 1

                print(random.choice(seq_word_for_damage_down), "\n")
                print(
                    "Здоровье: [",
                    random.choice(seq_damage_icons),
                    "] -1hp",
                    *heal_player,
                    "\n",
                )

            elif num_player > rand_num:  # Промах -1hp💔
                heal_player[count_step] = "💔"
                count_step += 1

                print(random.choice(seq_word_for_damage_up), "\n")
                print(
                    "Здоровье: [",
                    random.choice(seq_damage_icons),
                    "] -1hp",
                    *heal_player,
                    "\n",
                )
            elif num_player == rand_num:  # Победа!

                print(random.choice(seq_word_for_win), "\n")
                print("🤖💬 - Попробуем ещё раз?")
                ansver_player_1 = input("Ваш ответ: (Да/Нет) ")
                if ansver_player_yes_or_no(ansver_player_1) == True:
                    play_game()
                else:
                    break
        else:
            print("🤖💬 - Хм... Кажется вы ввели не число. Попробуйте ещё раз.")

    print("🤖💬 - Что-ж... Жаль... Ну ладно, до встречи!")


# Приветствие:
print('Добро пожаловать в игру: "ЧИСЛОВАЯ УГАДАЙКА"')
print(
    "📜 Правила:",
    "\n",
    "1. Нужно вводить только числа от 1 до 100",
    "\n",
    "2. Стоп слово: СТОП",
    "3. У вас есть Здоровье: ❤️❤️❤️❤️❤️❤️  | За каждый промах ты теряешь 1hp: 💔",
    "\n",
    sep="",
)
print("🤖💬 - Привет! Поиграем в игру?")
ansver_player = input("Ваш ответ: (Да/Нет) ")

# Проверка согласия игрока:
if ansver_player_yes_or_no(ansver_player) == True:
    play_game()
elif ansver_player_yes_or_no(ansver_player) == False:
    print("🤖💬 - Что-ж... Жаль... Ну ладно, до встречи!")