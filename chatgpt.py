# from fractions import Fraction as F
#
# def power(a,b) :
# 	if a==0: return 1
# 	return a ** b
#
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# #         result += factorial(n) / (factorial(k) * factorial(n - k)) * k ** (n - k)
#
# def bernoulli_numbers(n):
# 	result = 0
# 	for k in range(n + 1):
# 		täljare = factorial(n)
# 		nämnare = factorial(k) * factorial(n - k) * power(k, n - k)
# 		result += F(täljare, nämnare)
# 	return F(result, n + 1)
#
# for num in range(2,10):  # Change this to compute different Bernoulli numbers
# 	print(f"Bernoulli number B({num}) = {bernoulli_numbers(num)}")
#
