#Resolvendo equação de segundo grau
from math import sqrt

text = input("Insira os valores de a, b e c da equacao separados por virgula: ")
try:
	a, b, c = tuple(int(value) for value in text.split(","))
except ValueError:
	print("Os valores das variaveis nao sao compativeis")

def solucao_eq_segundo_grau(a, b, c):
	delta = b**2 - 4*a*c
	
	if(delta < 0):
		raise ValueError("Nao ha solucao real")
	
	x_1 = (-b+sqrt(delta))/(2*a)
	x_2 = (-b-sqrt(delta))/(2*a) 

	return x_1, x_2

try:
	x_1, x_2 = solucao_eq_segundo_grau(a,b,c)
	print(f"As solucoes desta equacao sao x_1 = {x_1:.2f} e x_2 = {x_2:.2f}")
except ValueError as error:
	print(error)
except NameError as nerror:
	print(nerror)	
