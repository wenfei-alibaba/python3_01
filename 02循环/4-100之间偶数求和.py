result = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
        result += i
    i += 1
print("1~100之间偶数和是=%d " % result)
