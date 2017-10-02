import numpy as np
from math import *
number_of_equations = int(input())
number_of_variables = int(input())
error = float(input())
variables = input().split()
x = np.array(list(map(float,input().split())))
precision = int(round(-log(error)/log(10))) + 1
print(precision)
equations = [input().replace('^','**') for equation in range(number_of_equations)]
jacobian =  [input().replace('^','**').split() for equation in range(number_of_equations)]

F = np.array(number_of_equations*[0.0])
J = np.array(number_of_equations*[[0.0]*number_of_variables])

[equations.__setitem__(i,equations[i].replace(variables[j],'(x['+str(j)+'])'))
 for i in range(len(equations)) for j in range(len(variables))]
[jacobian[i].__setitem__(j,jacobian[i][j].replace(variables[k],'(x['+str(k)+'])')) 
 for i in range(len(jacobian)) for j in range(len(jacobian[i])) for k in range(len(variables))]

while(True):
	[F.__setitem__(i,round(eval(equations[i]),precision)) for i in range(len(equations))]
	[J[i].__setitem__(j,round(eval(jacobian[i][j]),precision)) for i in range(len(jacobian)) 
	for j in range(len(jacobian[i]))]
	print('x =',x,'F(x) = ',F)
	x = x - np.linalg.inv(J).dot(F)
	[x.__setitem__(i,round(x[i],precision)) for i in range(len(x))]
	if(error > max(abs(F))):
		break
print('\nsolution:',x,'with minimal:',F)


