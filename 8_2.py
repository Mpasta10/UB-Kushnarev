n = int(input())
a = []
for i in range (n):
	b = []
	for j in range(n):
		b.append(int(input()))
	a.append(b)
print(a)
for i in range(n):
	x = a[i][0]
	a[i][0] = a[i][n-1]
	a[i][n-1] = x
print(a)