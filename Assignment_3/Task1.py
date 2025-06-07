def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num-1)
    
def fact_using_for(num):
    fact = 1
    if num == 0:
        return 1
    for x in range (num,1,-1):
        fact = fact * x
    print(f'Factorial of {num} is {fact}')


num = int(input("Enter a number: "))
fact = factorial(num)
print(f'Factorial of {num} is {fact}')
fact_using_for(num)