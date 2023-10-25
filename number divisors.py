number = int(input("Введите число: "))
print ("Ваше число:", number)

divisors = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print("Делители числа", number, ":", divisors)

