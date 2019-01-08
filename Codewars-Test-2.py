# 09.01.2019

def iq_test(numbers):
    lnumbers = numbers.split(" ")
    numodd = numeven = odd = even = 0
    odd = [int(x) for x in lnumbers if int(x) % 2 != 0]
    even = [int(x) for x in lnumbers if int(x) % 2 == 0]
    print("Нечётные числа: " + str(odd))
    print("Чётные числа: " + str(even))
    for n in lnumbers:
        if int(n) % 2 != 0:
            numodd += 1
            odd = n
        if (int(n) % 2) == 0:
            numeven += 1
            even = n
    return (lnumbers.index(odd) + 1) * (numodd == 1) + (lnumbers.index(even) + 1) * (numeven == 1)

print("Позиция нечётного числа: " + str(iq_test("2 4 7 8 10")))
print("Позиция нечётного числа: " + str(iq_test("1 2 2")))
print("Позиция нечётного числа: " + str(iq_test("2 5 4 6 8")))