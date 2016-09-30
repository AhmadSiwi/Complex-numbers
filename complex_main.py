from complex_class import Complex
print('\nWelcome to our simple calculator for complex numbers!')
while True:
	x = int(input("\nPlease enter '0' for cartesian or '1' for polar or '2' to exit:\n"))
	if x == 0:
		print('\nEnter your first number:')
		r1 = float(input('real = '))
		i1 = float(input('imaginary = '))
		op = input('\nChoose an operator(+,-,*,/): ')
		print('\nEnter your second number:')
		r2 = float(input('real = '))
		i2 = float(input('imaginary = '))
		first_num  = Complex(r1, i1, 0)
		second_num = Complex(r2, i2, 0)
		if op == '+':
			result = first_num.add(second_num)
			result.show_complex_cartesian()
		elif op =='-':
			result = first_num.sub(second_num)
			result.show_complex_cartesian()
		elif op == '*':
			result = first_num.mul(second_num)
			result.show_complex_cartesian()
		elif op == '/':
			result = first_num.div(second_num)
			result.show_complex_cartesian()
		else:
			print('\nWrong operation!')
	elif x == 1:
		print('\nEnter your first number:')
		r1 = float(input('magnitude = '))
		theta1 = float(input('theta in rad = '))
		op = input('\nChoose an operator(+,-,*,/): ')
		print('\nEnter your second number:')
		r2 = float(input('magnitude = '))
		theta2 = float(input('theta in rad = '))
		first_num  = Complex(r1, theta1, 1)
		second_num = Complex(r2, theta2, 1)
		if op == '+':
			result = first_num.add(second_num)
			result.show_complex_polar()
		elif op =='-':
			result = first_num.sub(second_num)
			result.show_complex_polar()
		elif op == '*':
			result = first_num.mul(second_num)
			result.show_complex_polar()
		elif op == '/':
			result = first_num.div(second_num)
			result.show_complex_polar()
		else:
			print('\nWrong operation!')
	elif x == 2:
		print('\nThanks for using our simple calculator for complex numbers!')
		print('\nGoodBye!\n')
		break