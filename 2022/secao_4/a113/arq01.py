def Mult(*args):
	tot = 1
	for n in args:
		tot *= n
	return tot


def ParOuImpar(n): 
	if n % 2 == 0:
		return 'Par'
	return 'Ímpar'	


num = Mult(3, 7)
print(num, ParOuImpar(num))