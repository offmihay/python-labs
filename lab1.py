def calculate_percentage(current, change):
    return current + current * change

def check_result(support, keeping_power):
    if support < 30 and keeping_power < 50:
        return "Росія змінює режим на про-російський"
    elif support > 30 and keeping_power < 50:
        return "Президент де-факто легітимний президент України, управляє рішеннями про партизанський рух із заходу."
    elif support < 30 and keeping_power > 50:
        return "В країні починаються протести. Війна затяжна і шанси з Росією приблизно рівні."
    else:
        return "Війна триває, але Україна все ближче до перемоги"

def main():
    support, keeping_power = 30, 70

    print("Росія напала на Україну. Ви - президент України. Що робитимете?")
    choice1 = input("Втечіть за кордон? 1. Так 2. Ні: ")
    while choice1 not in ["1", "2"]:
        print("Неправильний вибір. Введіть 1 або 2.")
        choice1 = input("Втечіть за кордон? 1. Так 2. Ні: ")

    if choice1 == "1":
        support = calculate_percentage(support, -0.4)
        keeping_power = calculate_percentage(keeping_power, -0.4)
        
        choice2 = input("Продовжувати оборону країни? 1. Так 2. Ні: ")
        while choice2 not in ["1", "2"]:
            print("Неправильний вибір. Введіть 1 або 2.")
            choice2 = input("Продовжувати оборону країни? 1. Так 2. Ні: ")

        if choice2 == "1":
            support = calculate_percentage(support, 0.2)
            keeping_power = calculate_percentage(keeping_power, 0.1)
        else:
            support = calculate_percentage(support, -0.3)
            keeping_power = calculate_percentage(keeping_power, -0.1)
        
        choice3 = input("Запровадити санкції проти Росії? 1. Так 2. Ні: ")
        while choice3 not in ["1", "2"]:
            print("Неправильний вибір. Введіть 1 або 2.")
            choice3 = input("Запровадити санкції проти Росії? 1. Так 2. Ні: ")

        if choice3 == "1":
            support = calculate_percentage(support, 0.1)
            keeping_power = calculate_percentage(keeping_power, 0.1)
        else:
            support = calculate_percentage(support, -0.2)
            keeping_power = calculate_percentage(keeping_power, 0.1)
    
    else:
        support = calculate_percentage(support, 1)
        keeping_power = calculate_percentage(keeping_power, 0.2)

        choice4 = input("Стати символом боротьби і просити допомогу у Заходу? 1. Так 2. Ні: ")
        while choice4 not in ["1", "2"]:
            print("Неправильний вибір. Введіть 1 або 2.")
            choice4 = input("Стати символом боротьби і просити допомогу у Заходу? 1. Так 2. Ні: ")

        if choice4 == "1":
            support = calculate_percentage(support, 0.1)
            keeping_power = calculate_percentage(keeping_power, 0.1)
        else:
            support = calculate_percentage(support, 0.3)
            keeping_power = calculate_percentage(keeping_power, -0.2)

        choice5 = input("Відмовитись від частини території? 1. Так 2. Ні: ")
        while choice5 not in ["1", "2"]:
            print("Неправильний вибір. Введіть 1 або 2.")
            choice5 = input("Відмовитись від частини території? 1. Так 2. Ні: ")

        if choice5 == "1":
            support = calculate_percentage(support, -0.3)
            keeping_power = calculate_percentage(keeping_power, 0.1)

    print(f"Підтримка народу: {round(support, 2)}%")
    print(f"Утримання влади: {round(keeping_power, 2)}%")
    print(check_result(support, keeping_power))

main()