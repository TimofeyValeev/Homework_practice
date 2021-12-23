N = int(input("Введите количество счетов компании: "))
M = int(input("Введите количество сотрудников компании: "))
print("Введите суммы")
fond_all = []
fond_sum = 0
for i in range(N):
    user_sum = int(input())
    fond_all.append(user_sum)
    fond_sum += user_sum
try:
    if fond_sum < M:
        print(0)
    elif fond_sum // M == 1:
        print(1)
    else:
        grant_found = 0
        max_grant = fond_sum // M

        while True:
            check = 0
            for i in fond_all:
                check += i // max_grant
            if check >= M:
                grant_found = 1
                max_grant += 1

            else:
                if not grant_found:
                    max_grant -= 1
                else:
                    print(max_grant - 1)
                    break

except ZeroDivisionError:
    print("Вы ввели количество сотрудников, равное нулю.")
