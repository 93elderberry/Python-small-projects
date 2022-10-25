import random
play = True
while play:
    print('Добро пожаловать в угадайку!')
    print('Нужен диапазон в котором хочешь угадывать: ')    
    a = input('Введи начало диапазона - это должна быть цифра: ')
    while a.isdigit() == False:
        print('Нужно ввести цифру, идиот! Давай снова.')
        a = input('Введи начало диапазона: ')
    b = input('Введи конец диапазона - это должна быть цифра большая первой: ')
    while b.isdigit() == False or int(a) > int(b):
        print('Нужно ввести цифру больше первой. Давай снова.')
        b = input('Введи конец диапазона: ')
    number = random.randint(int(a), int(b))

    
    def counter_to_words(counter):
        units = ['','одну', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
        tenner = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
        if counter< 20:
            return units[counter]
        if counter in [20,30,40,50,60,70,80,90]:
            return tenner[counter//10]
        if counter> 20:
            return tenner[counter//10] +' ' + units[counter%10]    

    def is_valid(num):
        if num.isdigit():
            num = int(num)
            if int(a) <= num <= int(b):
                return True
            else:
                return False
        else:
            return False
     
    counter = 0

    while True:
        response = input('Введите число в вашем диапозоне:')
        if not is_valid(response):
            print('А может быть все-таки введем число в диапазоне?)')
            continue
        val = int(response) 
    
        if val < number:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                counter += 1
        elif val > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            counter += 1
        else:
            counter += 1
            if counter == 1:
                print(f'Вы угадали за {counter_to_words(counter)} попытку, удивительно!')
                unswer = input('Хотите попробовать снова? Да/Нет ')
                if unswer.lower() == 'lf' or unswer.lower() == 'да': 
                    play = True
                    break
                else:
                    print('Ну чтож, возвращайся когда захочешь, буду ждать!') 
                    play = False
                    break
            if counter %10 in [2,3,4] or counter in [2,3,4]:
                print(f'Вы угадали за {counter_to_words(counter)} попытки, поздравляем!')
                unswer = input('Хотите улучшить результат? Да/Нет ')
                if unswer.lower() == 'lf' or unswer.lower() == 'да':
                    play = True
                    break
                else:
                    print('Ну чтож, возвращайся когда захочешь, буду ждать!') 
                    play = False  
                    break
            else:
                print(f'Вы угадали за {counter_to_words(counter)} попыток, поздравляем!')
                unswer = input('Хотите улучшить результат? Да/Нет ')
                if unswer.lower() == 'lf' or unswer.lower() == 'да':
                    play = True
                    break
                else:
                    print('Точно, пора возвращаться к работе, бездельник!') 
                    play = False 
                    break
    

     