
#Write a program that prints the integers from 1 to 100. 
#But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
#For numbers which are multiples of both three and five print "FizzBuzz".

mylist=range(1,101)
for item in mylist:
    if item%3 == 0 and item%5 == 0:
        print("%s FizzBuzz" %(item))
    elif item%3 == 0:
        print("%s Fizz" %(item))
    elif item%5 == 0:
        print("%s Buzz" %(item))
    else:
        print(item)

