for i in range(100):
    if i%3 and i%5 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("buzz")
    elif i%3 == 0:
        print("fizz")
    else:
        print(i)

