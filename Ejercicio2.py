def max_de_tres(a, b, c):
   if (a>b) and (a>c):
           return a
   elif (b>c) and (b>c):
           return b
   else:
           return c

assert max_de_tres(1, 9, 8)==9
assert max_de_tres(1, 9, 18)==9

