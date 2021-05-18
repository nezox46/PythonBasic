duration = int(input())
days, hour, minute, second = duration // 86400 % 3600, duration // 3600 % 24, duration // 60 % 60, duration % 60
print(f'{days} дней {hour} часов {minute} минут {second} секунд')

