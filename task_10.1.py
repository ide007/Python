class Matrix:
    def __init__(self, list_of_lists):
        self.list = list_of_lists

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.list]))

    def __add__(self, other):
        for i in range(len(self.list)):
            for j in range(len(other.list[i])):
                self.list[i][j] = self.list[i][j] + other.list[i][j]
        return Matrix.__str__(self)


matrix_1 = Matrix([[2, 14, 7, 3], [-2, 8, 14, -6], [12, 23, 6, 2], [84, 3, 36, 74]])
matrix_2 = Matrix([[9, 4, 17, 10], [-4, 7, 6, -3], [9, 7, 15, 43], [1, 54, 3, 3]])

print(matrix_2.__add__(matrix_1))
print(matrix_1)

# class Matrix:
#     def __init__(self, list_of_lists):
#         self.list = list_of_lists
#
#     def __str__(self):
#         return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.list]))
#
#     def __add__(self, other):
#         for i in range(len(self.list)):
#             row = []
#             for j in range(len(other.list[i])):
#                 row.append(self.list[i][j] + other.list[i][j])
#             print(row)
#         return Matrix.__str__(self)
#
#
# matrix_1 = Matrix([[2, 14, 7, 3], [-2, 8, 14, -6], [12, 23, 6, 2], [84, 3, 36, 74]])
# matrix_2 = Matrix([[9, 4, 17, 10], [-4, 7, 6, -3], [9, 7, 15, 43], [1, 54, 3, 3]])
#
# print(matrix_1.__add__(matrix_2))
# print()
# print(matrix_1)
