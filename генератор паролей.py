import random
digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
xz = 'il1Lo0O'

def generate_password():
    for i in range(int(counter)):
        password = ''
        for i in range(int(length)):
            password += random.choice(chars)
        print(password)
        
        
    

gen = True    
while gen:
    counter = input('Сколько паролей сгенерировать? Введите цифру: ')
    if counter.isdigit() == False:
        counter = input('Не понимаю, нужно ввести цифру: ')
        continue
    
    length =  input('Какой длины должен быть пароль? Введите цифру: ')
    if length.isdigit() == False:
        length = input('Не понимаю, нужно ввести цифру: ')
        continue    
    
    digits_answer = input('Включать ли цифры в пароль? ДА/НЕТ ')
    if digits_answer.lower() in ['lf','да', 'yes', 'вф', 'da']:
        chars += digits  
    
    lowercase_letters_answer = input('Включать ли строчные буквы в пароль? ДА/НЕТ ')
    if lowercase_letters_answer.lower() in ['lf','да', 'yes', 'вф', 'da']:
        chars += lowercase_letters     
    
    uppercase_letters_answer = input('Включать ли прописные буквы в пароль? ДА/НЕТ ')
    if uppercase_letters_answer.lower() in ['lf','да', 'yes', 'вф', 'da']:
        chars += uppercase_letters    
    
    punctuation_answer = input('Включать ли символы в пароль? ДА/НЕТ ')
    if punctuation_answer.lower() in ['lf','да', 'yes', 'вф', 'da']:
        chars += punctuation     
    
    xz_answer = input('Включать ли неоднозначные символы (il1Lo0O) в пароль? ДА/НЕТ ')
    if xz_answer.lower() in ['lf','да', 'yes', 'вф', 'da']:
        chars  += xz

    generate_password()  
    print()    
    
    gen_answer = input('Желаете сгенирировать еще пароли? ДА/НЕТ ')
    if gen_answer in ['lf', 'да', 'yes', 'вф', 'da']:
        gen = True
    else:
        gen = False        



            
    
    
    
    