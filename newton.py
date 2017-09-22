from math import *
function = input().replace('^','**')
derivative = input().replace('^','**')
x = float(input())
error = float(input())
x_ant = x + 999999999
while True:
	x_ant = x
	x = x - eval(function)/eval(derivative)
	if abs(x - x_ant) <= error:
		break
print('Function:',function.replace('**','^')),print('Solution:',x),print('Final Error:',x-x_ant)