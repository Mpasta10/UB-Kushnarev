n = int(input())
a = []
c = True 
for i in range (n):
	b = []
	for j in range(n):
		b.append(int(input()))
	a.append(b)
k = sum(a[0])

for i in range(n):
	if sum(a[i]) != k:
		c = False

for e in range(n):
	g = 0
	for j in range(n):
		g += a[j][e]
	if g != k:
		c = False


if c == True:
	print('Является магическим квадратом')
else:
	print('Не является магическим квадратом')
		
		
		
		
