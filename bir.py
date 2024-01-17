N = int(input("N = "))

lst = [i for i in range(N)]

for i in range(N):
    print(lst)
    lst = lst[:i] + lst[i::][::-1]

print(lst)

k = int(input("(1 dan N-1) gacha oraliqda son kiriting: "))

print(f"{k} - tartibdagi son: {lst.index(k)}")