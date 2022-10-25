
en_alphabet= [chr(i) for i in range(65,91)] + [chr(j) for j in range(97,123)]
ru_alphabet = [chr(i) for i in range(1040,1104)]


def caesar_shifr(phrase):
    if lang.lower() in ['en', 'eng','англ','ут']:
        alphabet, n = en_alphabet, 26
    if lang.lower() in ['ru', 'he', 'рус', 'ру']:
        alphabet, n = ru_alphabet, 32        
    if what_do =='0':
        for i in range(len(phrase)):
            if phrase[i].isalpha():
                if phrase[i].isupper():
                    print(alphabet[(alphabet.index(phrase[i]) + int(k)) % n], end = '')
                else:
                    print(alphabet[(alphabet.index(phrase[i]) + int(k)) % n + n], end='')
            else:
                print(phrase[i], end = '')
        
    if what_do =='1':
        for i in range(len(phrase)):
            if phrase[i].isalpha():
                if phrase[i].isupper():
                    print(alphabet[(alphabet.index(phrase[i]) - int(k)) % n], end = '')
                else:
                    print(alphabet[(alphabet.index(phrase[i]) - int(k)) % n + n], end='')
            else:
                print(phrase[i], end = '')

go = True
while go:
    what_do = input('Что нужно сделать? Для шифрования нажмите - 0, для дешифрования - 1 ')
    if what_do.isdigit() != True:
        what_do = input('Я так не понимаю. Для шифрования нажмите - 0, для дешифрования - 1 ')
        continue
    
    lang =  input('Выберите язык. Ru или En ')
    if lang.lower() not in ['en', 'eng', 'ru', 'he', 'англ', 'рус', 'ру', 'ут']:
       lang =  input('Я так не понимаю. Выберите один язык. Ru или En ') 
       continue
    
    if what_do == '0':
        phrase = input('Какую фразу или слово вы хотите зашифровать? ')
        k = input('Какой шаг сдвига сделать? Введите цифру: ')
        if k.isdigit() != True:
            k = input('Я так не понимаю. Для шифрования напишите цифру шага: ')
            continue        
    
    if what_do == '1':
        phrase = input('Какую фразу или слово вы хотите дешифровать?')
        k = input('Какой шаг сдвига попробовать? Введите цифру: ')
        if k.isdigit() != True or k == '0':
            print('Хорошо, подберу шаг сам, вы выберете результат')
            if lang in ['en', 'eng','англ','ут']:
                print('Вот результаты: ')
                for k in range(25):
                    print(caesar_shifr(phrase))
            if lang in ['ru', 'he', 'рус', 'ру']:
                print('Вот результаты: ')
                for k in range(32):
                    print(caesar_shifr(phrase))                    
        else:               
            print(' Вот результат: ')    
            caesar_shifr(phrase)                
    else:               
        print(' Вот результат: ')    
        caesar_shifr(phrase)
        
    go_unsw = input('Хотите зашифровать/дешифровать еще что-нибудь?')
    if go_unsw in ['lf', 'да']:
        go = True
    else:
        go = False
    