#16. Check if a number is perfect.
def is_perfect(num):
    if num < 1:
        return False
    return sum(i for i in range(1, num) if num % i == 0) == num


print(is_perfect(28))  
print(is_perfect(10))  
