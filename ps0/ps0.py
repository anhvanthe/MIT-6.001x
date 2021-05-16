import numpy
import math

num_x = int(input("Enter number x:  "))
num_y = int(input("Enter number y:  "))

X = num_x ** num_y

print('x**y = ' + str(X))

log = numpy.log2(num_x)

print('log(x) = ' + str(log))