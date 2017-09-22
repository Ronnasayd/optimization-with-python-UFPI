import numpy as np
number_variables = int(input())
ext_matrix = np.array([list(map(float,input().split())) for linha in range(number_variables)])
solution = np.zeros(number_variables)
# for coluna in range(number_variables):
# 	for linha in range(number_variables):
# 		if linha != coluna:
# 			ext_matrix[linha] = ext_matrix[linha]-(ext_matrix[linha,coluna]/ext_matrix[coluna,coluna])*ext_matrix[coluna]
[ext_matrix.__setitem__(linha,(ext_matrix[linha]-(ext_matrix[linha,coluna]/ext_matrix[coluna,coluna])*ext_matrix[coluna]))
 for coluna in range(number_variables) for linha in range(number_variables) if linha != coluna]
# for linha in range(number_variables):
# 	solution[linha] = ext_matrix[linha,-1]/ext_matrix[linha,linha]
[solution.__setitem__(linha,(ext_matrix[linha,-1]/ext_matrix[linha,linha])) for linha in range(number_variables)]
print('Reduced Matrix:'),print(ext_matrix),print('Solution:'),print(solution)