def checkFizz(num)
  reg = Regexp.new(/\A[0-9]{1}\z/)
  loop do
    list = num.to_s.chars.map(&:to_i)
    num = list.sum
    if reg.match(num.to_s)
      break
    end
  end
  case num
  when 3,6,9 then
    return true
  end   
end

def checkBuzz(num)
  reg = Regexp.new(/[0-9]$/)

  case (reg.match(num.to_s)).to_s
  when  "0","5" then
    return true
  end
end

def checkNum(num)
  boolFizz = checkFizz(num)
  boolBuzz = checkBuzz(num)

  if boolBuzz && boolFizz
    return "FizzBuzz"
  elsif boolFizz
    return "Fizz"
  elsif boolBuzz
    return "Buzz"
  else
    return num
  end
end

(1..100).each{|num|
  puts checkNum(num)
}