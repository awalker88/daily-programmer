seed = 20 #int(input("Enter a number: "))

digits = 1

for num in str(seed ** 2):
    digits += 1


current = 1

for i in range(seed):
    line = ""
    for j in range(seed):
        line = line + (" " * (digits - len(str(current)))) + str(current)
        current += 1

    print(line)



