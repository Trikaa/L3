def matrix_generator(n):
    x = 0
    matrix = []
    for j in range(n):
        lst = list(range(n, x, -1))
        matrix.append(lst)
        print(lst)
        x += 1
matrix_generator(7)
