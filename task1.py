# Напишите функцию для транспонирования матрицы


# def matrix_transporation(table):
#     table2 = []
#
#     for i in range(len(table[0])):
#         table2.append(list())
#         for j in range(len(table)):
#             table2[i].append(table[j][i])
#     return table2
#
# matrix = [[1, 2, 3], [4, 5, 6]]
# print(matrix)
# matrix2 = matrix_transporation(matrix)
# print(matrix2)

def matrix_transporation(*a_list: list[[int]]) -> list[()] | str:
    moving = True
    col = len(a_list[0])
    for a in list(a_list):
        if len(a) != col:
            moving = False
    if moving:
        return list(zip(*a_list))
    else:
        return 'Матрицу нельзя транспорировать'


print(matrix_transporation([1, 3, 5], [2, 4, 6]))

