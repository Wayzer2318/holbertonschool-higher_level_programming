#!/usr/bin/python3
#!/

def square_matrix_simple(matrix=[]):
    nm = []
    for i in range(len(matrix)):
        nm.append(list(map((lambda x: x ** 2), matrix[i])))
    return nm
