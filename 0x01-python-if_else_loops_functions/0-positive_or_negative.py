#!/usr/bin/python3
import random
number = random.randint(-10, 10)
<<<<<<< HEAD
if (number == 0):
    print("{} is zero".format(number))
elif (number < 0):
    print("{} is negative".format(number))
elif (number > 0):
    print("{} is positve".format(number))
=======
if (number > 0):
	print("{} is positve".format(number))
elif (number == 0):
	print("{} is zero".format(number))
else:
	print("{} is negative".format(number))
>>>>>>> e0b59f467a1641222fee959ec415fe278d997454
