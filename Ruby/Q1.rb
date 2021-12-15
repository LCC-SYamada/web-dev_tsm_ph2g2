def sortDictionary(*numList) 
  return numList.map(&:to_s).sort.map(&:to_i)
end

print(sortDictionary(1,25,35,3,5,100,20))