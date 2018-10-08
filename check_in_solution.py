#this imports numpy
import numpy as np

#this step creates a function called main
def main():
	i = 0     #sets a variable i equal to 0
	x = 119.  # sets a variable x equal to 119 and the decimal makes it a float (do you need the 0?)

	for i in range(120):          #starting at i, add one everytime the program gets to the end of the for loop
		if (i%2) == 0:        #if the value of i divided by 2 is exactly 0, then do the below part
			x += 3.0      #resets the variable x to 3 more than it was before

		else:                   # if the above condition is not true, do what is below
			x -= 5.0        #resets the variable x to 5 less than it was before

	s = "%3.2e" % x          #puts it in sci notation (need help with why)

	print(s)           #prints the above string s


if __name__ == "__main__":
	main()


