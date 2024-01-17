son = int(input("Son kiriting: "))

lst = []
i = 0
while son:
    s = son % 10
    lst.append(str(s * 10**i)) if s != 0 else lst
    son //= 10
    i += 1

print(" + ".join(lst[::-1]))