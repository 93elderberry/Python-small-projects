def konverter_to_any(num,num_base):
    s = ''
    ABC = 'ABCDEF'
    while num > 0:
        if num % num_base > 9:
            s += ABC[(num % num_base) % 10]
        else:
            s += str(num % num_base)
        num = num // num_base
    return(s[::-1])

print('Добро пожаловать в конвертер! Я переведу число из десятичной системы счисления в любую другую!')    
go_konverter = True    
while go_konverter:
    num = int(input('Введите число в десятичной системе: '))
    num_base = int(input('Введите новое основание числа: '))
    print('Число =')
    print(konverter_to_any(num,num_base))
    output = input('Желаете конвертировать снова? Введите ДА/НЕТ ')
    if output in ['lf', 'да']:
        go_konverter = True 
    else:
        print('Буду ждать! Возвращайтесь!')
        go_konverter = False 