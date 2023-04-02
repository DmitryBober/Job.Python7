#Задача 34

def rifma(words):
    return sum(1 for i in words if i in 'аеёиоуыэюя')
    
c = "Хорошо-живет-на-свете-Винни-Пух! Оттого-поет-он-эти-Песни-вслух!"
st = c.lower().split()
t = rifma(st[0])
if all([rifma(i) == t for i in st]):
    print('Парам пам-пам')
else:
    print('Пам парам')

#Задача 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])


print_operation_table(lambda x, y: x * y)