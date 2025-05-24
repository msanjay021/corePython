# word = 'Python'

# def my_func(n):
#     for i in range(1, n):
#         print(i*"*")

#     for i in reversed(range(1, n)):
#         print(i*"*")

# inp_character = int(input("enter a number:"))

# my_func(inp_character)


# Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# print(users)
# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
# print(users)

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
# print(users)

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):


# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

# match status:
#     case 400:
#         "Bad request"
#     case 404:
#         "Not found"
#     case 418:
#         "I'm a teapot"
#     case _:
#         "Something's wrong with the internet"

# def fib(n):    # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# # Now call the function we just defined:
# fib(2000)

# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])


# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")


squares = []
for i in range(10):
    squares.append(i**2)

print(squares)
