lst = [3332, 10, 710238, 674, 7723, 420, 1030, 60001, 2324, 1964]
i = 1
summa = 0
while i != len(lst) - 1:
    if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
        summa += 1
        i += 1
    else:
        i += 1
        continue
print(summa)