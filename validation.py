number =None

while number==None:
     try:
         number=int(raw_input("give me a number:"))
     except ValueError:
         print "sorry invalid input"
print "the number you have given me was %d" %(number)

