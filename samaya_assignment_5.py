#Challenge 1
print(f"=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number:"))
step_count = 0
print(" Sequence:", end=" ")
while (current_number != 1):
    print( current_number, end=" ")
    if current_number % 2 == 0:
        current_number//=2
    elif current_number % 2 != 0:
        current_number = (current_number * 3) +1
    step_count += 1
print("1")
print(f"Steps: {step_count}")
print()

# Challenge 2
print("=== Challenge 2: Prime Number Checker ===")
current_number = int(input())
print(f"Enter a number: Testing divisors from 2 to {current_number-1}...")
is_prime = True
for divisor in range(2, current_number):
    if current_number % divisor == 0:
        is_prime = False
        break
if is_prime:
    print(f"{current_number} is prime!")
else:
    for divisor in range(2, current_number):
        if current_number % divisor == 0:
            divisible_by = divisor
            print(f"{current_number} is not prime! (divisible by {divisible_by})")
print()

