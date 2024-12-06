with open('Кушнарев Алексей Валерьевич_УБ-41_vvod.txt') as file:
    a = []
    for line in file:
        a.append([int(x) for x in line.strip().split()])

for i in range(len(a[0])):
	x = a[i][0]
	a[i][0] = a[i][len(a[0]) - 1]
	a[i][len(a[0]) - 1] = x
with open('Кушнарев Алексей Валерьевич_УБ-41_vivod.txt', 'r+') as file2:
    for i in range(len(a)):
        file2.write(f'{a[i]}')
        file2.write('\n')