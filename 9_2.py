def f(max, max2):
    num = int(input())
    
    if num == 0:
        if max2 == float('-inf'):
            print('Нет 2-го по величине элемента')
        else:
            print(max2)
        return

    if num > max:
        max2 = max
        max = num
    elif num > max2 and num != max:
        max2 = num

    f(max, max2)
f(float('-inf'), float('-inf'))