# Algorithm in python to print all prime numbers below a certain number given it is a smaller number


def SieveOfEratosthenes(n):
    # create a list init
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            print(i)
            for x in range(i*i, n+1, i):
                prime_list.append(x)
print(SieveOfEratosthenes(35));

print("break")

# Dynamic fibonacci sequence solving algorithm for position
array = [0, 1] 

def Dynamic_Fibonacci(n): 
    if (n < 0): 
        return 0
    elif (n <= len(array)): 
        return array[n-1] 
    else: 
        dyno_fib = Dynamic_Fibonacci(n-1)+Dynamic_Fibonacci(n-2) 
        array.append(dyno_fib) 
        return dyno_fib 

# Call a position w function
print(Dynamic_Fibonacci(11)) 