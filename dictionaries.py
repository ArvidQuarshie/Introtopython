Python 2.7.10 (default, Oct 14 2015, 16:09:02) 
[GCC 5.2.1 20151010] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> stuff={'name':'Arvid','age':'34','height':'5 inches'}

>>> print stuff['name']
Arvid
>>> print['age']
['age']
>>> print stuff ['age']
34
>>> print stuff ['height']
5 inches
>>> stuff[1]="wat"
>>> print stuff['name']
Arvid
>>> print stuff[1]
wat
>>> del stuff[]
SyntaxError: invalid syntax
>>> del stuff ['name']
>>> print stuff['name']

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print stuff['name']
KeyError: 'name'
>>> 
moringa={'name':'moringaschool'}
print moringa['name']
if moringa.has_key(name)=True:
    moringa['name']=school

    print moringa['name']
print moringa['name']


moringa={'name':'moringaschool'}
print moringa['name']
if moringa.has_key(name)=True:
    moringa['name']=school
    
