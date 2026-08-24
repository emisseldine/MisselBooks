square = lambda x : x**2

print(square(5))   

def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (uses default exponent = 2)
print(power(5, 3))   # 125

def greet(name):
    print("Hello,", name)

greet("Alice")   # prints "Hello, Alice"
