# Write a Python program that prints the numbers from 1 to 100. 

for i in range(1,101):
# Check if divisable by 3 and 5       
      if i%3 == 0 and i%5 == 0:    
          print ("FizzBuzz")
# if both are not divisible check to see 
# if divisable by 3 
      elif i%3 == 0:
      	print ("Fizz")
# if divisable by 3      
      elif i%5 == 0:
      	print ("Buzz")
# if not divisable by 3 or 5 output number of iteration      
      else:
      	print (i)
    
