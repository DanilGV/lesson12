def get_matrix (n , m , value):
    matrix = []
    for i in range(n):
        a = []
        for j in range(m):
            a.append(value)
        matrix.append(a)
    return matrix
print(get_matrix(2, 2, 10))
print(get_matrix(5, 4, 8))
print(get_matrix(0, 7, 6))