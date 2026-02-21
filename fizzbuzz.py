import sys

if len(sys.argv) < 2: # Pārbauda, vai ir norādīts skaitlis N kā komandrindas arguments
    print("Norādi skaitli N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N jābūt skaitlim")
    sys.exit(1)

for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print("FizzBuzzJazz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 7 == 0:
        print("Jazz")
    else:
        print(i)
