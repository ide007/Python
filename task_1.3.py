procent = int(input('Введите проценты, значение от 0 до 20: '))
text = ["процент", "процента", "процентов"]

while procent not in range(0, 21):
    procent = int(input('Значение % должно быть в пределах от 0 до 20: '))

if procent == 0 or procent in range(5, 21):
    print(procent, text[2])
elif procent in range(2, 5):
    print(procent, text[1])
else:
    print(procent, text[0])

for i in range(0, 21):
    if i == 0 or i in range(5, 21):
        print(i, text[2])
    elif i in range(2, 5):
        print(i, text[1])
    else:
        print(i, text[0])
