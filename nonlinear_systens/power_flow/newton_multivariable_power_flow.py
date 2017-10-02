import numpy as np
from math import cos,sin

dim = int(input())
error = float(input())
PR = np.array(list(map(int,input().split())))-1
QR = np.array(list(map(int,input().split())))-1
P_real = np.array(list(map(float,input().split())))
Q_real = np.array(list(map(float,input().split())))
v = np.array(list(map(float,input().split())))
t = np.array(list(map(float,input().split())))

G = np.zeros([dim,dim])
B = np.zeros([dim,dim])
for i in range(dim):
	G[i] = np.array(list(map(float,input().split())))
for i in range(dim):
	B[i] = np.array(list(map(float,input().split())))

H = np.array(len(PR)*[len(PR)*[0.0]])
N = np.array(len(PR)*[len(QR)*[0.0]])
J = np.array(len(QR)*[len(PR)*[0.0]])
L = np.array(len(QR)*[len(QR)*[0.0]])

JAC = np.zeros([len(PR)+len(QR),len(PR)+len(QR)])


P_est = np.array(dim*[0.0])
Q_est = np.array(dim*[0.0])

delta_P = np.array(len(PR)*[0.0])
delta_Q = np.array(len(QR)*[0.0])
delta = np.array((len(PR)+len(QR))*[0.0])


while True:
	P_est = np.array(dim*[0.0])
	Q_est = np.array(dim*[0.0])
	for i in range(dim):
		for j in range(dim):
			P_est[i] = P_est[i] + v[i]*v[j]*(G[i][j]*cos(t[j] - t[i]) - B[i][j]*sin(t[j] - t[i]))
			Q_est[i] = Q_est[i] - v[i]*v[j]*(B[i][j]*cos(t[j] - t[i]) + G[i][j]*sin(t[j] - t[i]))
	k = 0
	for i in PR:
		delta_P[k] = P_real[k] - P_est[i]
		k = k + 1
	k = 0
	for i in QR:
		delta_Q[k] = Q_real[k] - Q_est[i]
		k = k + 1
	delta[0:len(PR)] = delta_P
	delta[len(PR):len(PR)+len(QR)] = delta_Q

	if(max(abs(delta_P)) < error and max(abs(delta_Q)) < error):
		break
		
	ind_i = 0
	for i in PR:
		ind_j = 0
		for j in PR:
			if i == j:
				H[ind_i][ind_j] = -Q_est[i] - (v[i]**2)*B[i][j]
			else:
				H[ind_i][ind_j] = -v[i]*v[j]*(B[i][j]*cos(t[j] - t[i]) + G[i][j]*sin(t[j] - t[i]))
			ind_j = ind_j + 1
		ind_i = ind_i + 1

	ind_i= 0
	for i in PR:
		ind_j = 0
		for j in QR:
			if i == j:
				N[ind_i][ind_j] = (P_est[i] + (v[i]**2)*G[i][j])
			else:
				N[ind_i][ind_j] = v[i]*v[j]*(G[i][j]*cos(t[j]-t[i]) - B[i][j]*sin(t[j]-t[i]))
			ind_j = ind_j + 1
		ind_i = ind_i + 1

	ind_i = 0
	for i in QR:
		ind_j = 0
		for j in PR:
			if i == j:
				J[ind_i][ind_j] = P_est[i] - (v[i]**2)*G[i][j]
			else:
				J[ind_i][ind_j] = v[i]*v[j]*(B[i][j]*sin(t[j]-t[i]) - G[i][j]*cos(t[j]-t[i]))
			ind_j = ind_j + 1
		ind_i = ind_i + 1

	ind_i = 0
	for i in QR:
		ind_j = 0
		for j in QR:
			if i == j:
				L[ind_i][ind_j] = Q_est[i] - (v[i]**2)*B[i][j]
			else:
				L[ind_i][ind_j] = -v[i]*v[j]*(B[i][j]*cos(t[j]-t[i]) + G[i][j]*sin(t[j] - t[i]))
			ind_j = ind_j  + 1
		ind_i = ind_i + 1

	JAC[0:len(PR),0:len(PR)] = H
	JAC[0:len(PR),len(PR):len(PR)+len(QR)] = N
	JAC[len(PR):len(PR)+len(QR),0:len(PR)] = J
	JAC[len(PR):len(PR)+len(QR),len(PR):len(PR)+len(QR)] = L

	delta_x = np.linalg.inv(JAC).dot(delta)

	k = 0
	for i in PR:
		t[i] = t[i] + delta_x[k]
		k = k + 1

	k = len(PR)
	for i in QR:
		v[i] = v[i]/(1 - delta_x[k])
		k = k + 1
print('V = ',v)
print('Theta = ',t)
	


