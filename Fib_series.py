n = int(input("Enter the nth number: "))

zeroth_num = 0
first_num = 1

count =0

# while count <=n:
#     next_num = zeroth_num + first_num 
#     zeroth_num = first_num 
#     first_num = next_num
#     count = count +1

for i in range(0,n):
    next_num = zeroth_num + first_num
    zeroth_num = first_num
    first_num = next_num
    print(zeroth_num)


print(zeroth_num)

# def fibonacci(n):
#     if n < 0:
#         return "Invalid input"
    
#     a, b = 0, 1
#     count = 0
    
#     while count < n:
#         a, b = b, a + b
#         count += 1
    
#     return a

# # Input from the user
# n = int(input("Enter the value of n: "))
# print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
