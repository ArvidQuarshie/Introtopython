Python 2.7.10 (default, Oct 14 2015, 16:09:02) 
[GCC 5.2.1 20151010] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 1,2,3,4
(1, 2, 3, 4)
>>> ['bob','sue','john']
['bob', 'sue', 'john']
>>> a=[1,2,3,4]
>>> names=["bob" "sue" "john"]
>>> a[0]
1
>>> names[0]
'bobsuejohn'
>>> a.append (8)
>>> a
[1, 2, 3, 4, 8]
>>> range(4,11)
[4, 5, 6, 7, 8, 9, 10]
>>> [range (1,11)]
[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
>>> [x*2 for x in range(1,11)]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> list(range(2,21))
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> [x for x in range(2,21) if x%2==0]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> //filters out the uneven numbers
