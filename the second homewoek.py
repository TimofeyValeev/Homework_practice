
def get_col(matrix, ind): # получение столбца матрицы
    col = []
    for row in matrix:
        col.append(row[ind])
    return col


def row_X_col(row, col): #перемножение строки на столбец
    s = 0
    for i in range(len(row)):
        s = s + row[i] * col[i]
    return s

def beautiful_print(matrix):# печатать в красивом виде
    col_number = len(matrix[0])
    len_box = []
    for i in range(col_number):
        max_len = 0
        col = get_col(matrix, i)
        for j in col:
            if max_len < len(str(j)):
                max_len = len(str(j))
        len_box.append(max_len)
    for row in matrix:
        row_str = ""
        for elem in row:
            row_str = row_str + str(elem).rjust(len_box[row.index(elem)]) + " "
        print(row_str)

def matrix_mult(A, B):
    C = []
    col_number = len(B[0])
    for row in A:
        C_row = []
        for i in range(col_number):
            col = get_col(B, i)
            C_row.append(row_X_col(row, col))
        C.append(C_row)
    beautiful_print(C)


A = [[1, 2], [3, 4], [5, 6]]
B = [[1, 2, 3, 4], [5, 6, 7, 8]]
error = 0

for i in range(1, len(A)):
    if len(A[i]) != len(A[i - 1]):
        error = 1

if error == 0:
    for i in range(1, len(B)):
        if len(B[i]) != len(B[i - 1]):
            error = 1

if error == 0:
    if len(A[0]) == len(B):
        C = matrix_mult(A, B)

    else:
        print("Матрицы нельзя перемножить")
else:
    print("Мартицы заданы неправильно, попробуйте еще ")
