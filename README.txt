----------------------------------------------------------------------------------------------
#gauss.py
----------------------------------------------------------------------------------------------
A ENTRADA DEVE SER DA SEGUINTE FORMA
----------------------------------------------------------------------------------------------
3			# NUMERO DE VARIAVEIS
2 1 -3 -1	# PRIMEIRA LINHA DA MATRIZ EXTENDIDA COM NUMEROS SEPARADOS POR ESPAÇOS
-1 3 2 12	# ---
3 1 -3 0	# ENÉSIMA LINHA DA MATRIZ EXTENDIDA COM NUMEROS SEPARADOS POR ESPAÇOS

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
#jordan.py
----------------------------------------------------------------------------------------------
A ENTRADA DEVE SER DA SEGUINTE FORMA
----------------------------------------------------------------------------------------------
3			# NUMERO DE VARIAVEIS
2 1 -3 -1	# PRIMEIRA LINHA DA MATRIZ EXTENDIDA COM NUMEROS SEPARADOS POR ESPAÇOS
-1 3 2 12	# ---
3 1 -3 0	# ENÉSIMA LINHA DA MATRIZ EXTENDIDA COM NUMEROS SEPARADOS POR ESPAÇOS

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
#newton.py
----------------------------------------------------------------------------------------------
A ENTRADA DEVE SER DA SEGUINTE FORMA
----------------------------------------------------------------------------------------------
x^2-2		# FUNÇÃO A SER MINIMIZADA (VARIÁVEL DEVE SER SEMPRE REPRESENTADA POR x)
2*x			# DERIVADA DA FUNÇÃO A SER MIMIZADA (VARIÁVEL DEVE SER SEMPRE REPRESENTADA POR x)
5.0			# CHUTE INICIAL PARA O VALOR x
1e-7		# ERRO UTILIZADO PARA CRITÉRIO DE PARADA ENTRE AS INTERAÇÕES DE x
----------------------------------------------------------------------------------------------
#newton_multivariable.py
----------------------------------------------------------------------------------------------
A ENTRADA DEVE SER DA SEGUINTE FORMA
-------------------------------------------------------------------------------------------------------
3					#number of equations/functions
3					#number of variables
1e-7					#error for stop the method
x1 x2 x3				#the variables
20 20 20				#initial value for the variables
x1^2 -2*x1 + x2^2 -x3 + 1		#equation(1)/function(1)
x1*x2^2 -x1 -3*x2 + x2*x3 + 2		#equation(2)/function(2)
x1*x3^2 - 3*x3 + x2*x3^2 + x1*x2	#equation(3)/function(3)
2*x1-2 2*x2 -1				#line(1) of jacobian
x2^2-1 2*x1*x2-3+x3 x2			#line(2) of jacobian
x3^2+x2 x3^2+x1 2*x1*x3-3+2*x2*x3	#line(3) of jacobian
---------------------------------------------------------------------------------------------------------------------
#newton_multivariable_power_flow.py
---------------------------------------------------------------------------------------------------------------------
A ENTRADA DEVE SER DA SEGUINTE FORMA
----------------------------------------------------------------------------------------------------------------------
2		#quantidade de barras
1e-10		#erro utilizado para parada
2		#local das barras com potencia ativa conhecida
2		#local das barras com potencia reativa conhecida
0.25		#valor da potencia ativa para barra n conhecida
0.0		#valor da potencia reativa para barra n conhecida
1.0 1.0		#estimação inicial dos valores de modulo de tensao (V)
0.0 0.0		#estimação inicial dos alores de fase de tensao (Theta)
0.0 0.0		#primeira linha da matriz de condutancia
0.0 0.0		#enesima linha da matriz de condutancia
-10.0 10.0	#primeira linha da matriz de susceptancia
10.0 -12.0	#enesima linha da matriz de susceptancia

