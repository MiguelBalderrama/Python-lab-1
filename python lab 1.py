print "hello"
print ""
print "what is your name?"

name = raw_input()
print""
print "hello " 
print name
print ""
print "can you give me a number?"
number1 = raw_input()
print ""
print "how about another?"
number2 = raw_input() 
print ""
print "do you want to add or subtract these numbers? (1=+) (2=-)"
answer = raw_input()
if int(answer) == 2:
   print int(number1) - int(number2)
else:
   print int(number1) + int(number2)
