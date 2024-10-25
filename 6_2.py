# var 2
a = [1, 2, 3, 4, 15, 28, -100, -11, 0, -13]
b = []
c = []
for i in a:
	if i > 0:
		b.append(i)
	else:
		c.append(i)
print(a, b, c)
