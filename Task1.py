# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = 100
sum = 0

while number > 0:
    digit = number % 10
    sum += digit
    number //= 10
print ("Сумма цифр числа: ", sum)