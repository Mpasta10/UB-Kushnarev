#2 var
k = int(input())
f = int(input())
if f < 5 or k > 2:
	r = f + k -1
elif k < 2:
	r = k**2
elif k == 2:
	r = 1
print(r)
