#var 2
s = input()
k = 0
while ":" in s:
	s = s.replace(':', '%', 1)
	k += 1
print(k)
