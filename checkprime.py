
# coding: utf-8

# In[1]:


#creating a function to check if a number is prime
#2, 3, 5, 7, 11, 13
def checkprime(num):
    '''
    input a number to check whether it's a prime number
    '''
    
    for item in range(2, num):
        if num % item == 0:
            return False
    else: #else aligned to for: exhaust all possibilities in the range before returning True
        return True

