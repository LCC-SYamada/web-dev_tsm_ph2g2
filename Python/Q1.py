def DictionarySort (*args):
  strNumbers = sorted([str(x) for x in args])
  print(strNumbers)
  for i in strNumbers:
    print(int(i)) 

print(DictionarySort(14, 35, 2, 3, 1, 1000))
