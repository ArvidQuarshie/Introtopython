Python 2.7.10 (default, Oct 14 2015, 16:09:02) 
[GCC 5.2.1 20151010] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> the_count=[1,2,3,4,5]
>>> fruit=['apples','oranges','pears','apricots']
>>> for fruit in fruits:
	print "A fruit of type %s is:" %fruit


Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    for fruit in fruits:
NameError: name 'fruits' is not defined
>>> fruits=['apples','oranges','pears','apricots']
>>> for fruit in fruits:
	print " A fruit of tyoe %s is:"%fruit

	
 A fruit of tyoe apples is:
 A fruit of tyoe oranges is:
 A fruit of tyoe pears is:
 A fruit of tyoe apricots is:
>>> change=[1,'pennies',2,'dimes',3,'quarters']
>>> for i in change:
	print "i got %r" %i

	
i got 1
i got 'pennies'
i got 2
i got 'dimes'
i got 3
i got 'quarters'
>>> the_count=[1,2,3,4,5]
>>> for number in the_count:
	print "the count is %s" %number

	
the count is 1
the count is 2
the count is 3
the count is 4
the count is 5
>>> elements=[]
>>> for i in range(0,6)
SyntaxError: invalid syntax
>>> for i in range(0,6):
	print "adding %d to the list."%i
	elements.append(i)

	
adding 0 to the list.
adding 1 to the list.
adding 2 to the list.
adding 3 to the list.
adding 4 to the list.
adding 5 to the list.
>>> for i in elements:
	print "elememt was %d" %i

	
elememt was 0
elememt was 1
elememt was 2
elememt was 3
elememt was 4
elememt was 5
>>> 
