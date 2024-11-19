a = []
max = float('-inf')
def f():
     global max
     global a
     x = int(input())
     if x == 0:
          return
     else:
          if x > max:
               max = x
     a.append(max)
     f()
     if len(a) >= 2:
          return a[-2]
     else:
          return 'Необходимо два элемента'
print(f())