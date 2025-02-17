#19. Calculate the sum of the digits of a number.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))


print(sum_of_digits(1234))  
print(sum_of_digits(-567))  

