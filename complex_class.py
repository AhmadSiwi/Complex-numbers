import math
class Complex():
	def __init__(self, m, n, type):
		self.x = 0
		self.y = 0
		self.r = 0
		self.theta = 0
		if type == 0:
			self.x = m
			self.y = n
			self.r = math.sqrt(m**2+n**2)
			self.theta = math.atan2(n, m)
		else:
			self.r = m
			self.theta = n
			self.x = m*math.cos(n)
			self.y = m*math.sin(n)
	def add(self, other_complex):
		x = self.x + other_complex.x
		y = self.y + other_complex.y
		return Complex(x, y, 0)
	def sub(self, other_complex):
		x = self.x - other_complex.x
		y = self.y - other_complex.y
		return Complex(x, y, 0)
	def mul(self, other_complex):
		r = self.r * other_complex.r
		theta = self.theta + other_complex.theta
		return Complex(r, theta, 1)
	def div(self, other_complex):
		
		r = self.r / other_complex.r
		theta = self.theta - other_complex.theta
		return Complex(r, theta, 1)
	def show_complex_cartesian(self):
		if self.y == 0:
			print('result =',self.x)
		elif self.y == 1:
			if self.x == 0:
				print('result =','i')
			else:
				print('result =',str(self.x)+'+'+'i')
		elif self.y > 1:
			if self.x == 0:
				print('result =',str(self.y)+'i')
			else:
				print('result =',str(self.x)+'+'+str(self.y)+'i')
		elif self.y == -1:
			if self.x == 0:
				print('result =','-i')
			else:
				print('result =',str(self.x)+'-i')
		elif self.y < -1:
			if self.x == 0:
				print('result =',str(self.y)+'i')
			else:
				print('result =',str(self.x)+str(self.y)+'i')
	def show_complex_polar(self):
		print('result =',self.r, 'cis', self.theta)