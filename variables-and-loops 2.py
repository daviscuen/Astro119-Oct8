import numpy as np
def main():
	i = 0
	n = 10
	x = 119.0
	
	y = np.zeros(n,dtype=float)     #declares an array of 10 zeros as floats
	#we can use for loops to iterate through a variable
	
	for i in range(n):          #for i in range (0,n-1)
		y[i] = 2.0 * float(i) + 1.0    #this sets y = 2i+1
		
		#we can iterate through the elements one by one 
	for y_element in y:
		print(y_element)
		
if __name__ == "__main__":
	main()
	