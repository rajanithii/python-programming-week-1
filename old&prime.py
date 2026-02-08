def is_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Input
num = int(input("Enter a number: "))

# Even / Odd check
print("The number is:", is_even_odd(num))

# Prime check
if is_prime(num):
    print("The number is Prime")
else:
    print("The number is Not Prime")
