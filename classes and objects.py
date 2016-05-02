Python 2.7.10 (default, Oct 14 2015, 16:09:02) 
[GCC 5.2.1 20151010] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> class Enemy:
	life=3
	def attack(self):
	    print("ouch")
	    self.life -= 1
	def checklife(self):
	    if self.life <=0:
	        print ("I am dead")
	    else:
		print(str(self.life)+"life left")
enemy1=enemy()
SyntaxError: invalid syntax
>>> enemy1=Enemy()

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    enemy1=Enemy()
NameError: name 'Enemy' is not defined
>>> enemy1 = Enemy()

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    enemy1 = Enemy()
NameError: name 'Enemy' is not defined
>>> 
