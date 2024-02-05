x = input('list all of your grades ')

print(x)

grades = x.split(",")
for i in range(len(grades)):
    grades[i] = int(grades[i])

print(grades)