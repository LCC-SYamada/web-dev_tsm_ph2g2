import math

def FizzBuzz(limit):
  d = {3: "Fizz", 5: "Buzz", 15: "FizzBuzz"}
  for i in range(1, limit + 1):
    # 1. 最大公約数を求める(math.gcd)
    # 2. 最大公約数が 3/5/15 だったら辞書から値を引っ張る
    # 3. 最大公約数が 3/5/15 以外の数値が返ってきたらgetの処理によりデフォルト値iを返す
    print(d.get(math.gcd(i, 15), i))

FizzBuzz(20)
