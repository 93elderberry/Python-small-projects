def konverter_to_ten(num,num_base):
    if num_base != 16:
        return sum([int(num[-1 - i]) * num_base**i for i in range(len(num))])
    else:
        s = list()
        for i in range(len(num)):
            if num[-1 - i] not in ['A', 'B', 'C', 'D', 'E', 'F']:
                s.append(int(num[-1 - i]) * num_base**i)
            else:
                s.append((ord(num[-1 - i]) - 55) * num_base**i)
        return sum(s)        

print('Добро пожаловать в конвертер! Я переведу число из любых систем счисления в десятичную систему!')    
go_konverter = True    
while go_konverter:
    num = input('Введите число без основания: ')
    num_base = int(input('Введите основание числа: '))
    print('Число в десятичной системе:')
    print(konverter_to_ten(num,num_base))
    output = input('Желаете конвертировать снова? Введите ДА/НЕТ ')
    if output in ['lf', 'да']:
        go_konverter = True 
    else:
        print('Буду ждать! Возвращайтесь!')
        go_konverter = False 