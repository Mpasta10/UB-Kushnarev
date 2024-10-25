#var 4
s = input()
k = 0
while "a" in s:
	s = s.replace('a', 'o', 1)
	k += 1
print(k, len(s))
