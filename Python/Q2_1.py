def FizzBuzz(limit):
  fizz = [i for i in range(0, limit + 1, 3)]
  buzz = [i for i in range(0, limit + 1, 5)]
  
  for i in range(1, limit + 1):
    if i in fizz and i in buzz:
      print('FizzBuzz')
    elif i in fizz:
      print('Fizz')
    elif i in buzz:
      print('Buzz')
    else:
      print(i)

FizzBuzz(20)
