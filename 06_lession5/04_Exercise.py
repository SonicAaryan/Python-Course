# Q. What will be the length of following set s.
'''
s = set()
s.add(20)
s.add(20.0)
20 == 20.0 (Is true bcz == check values and datatype dosn't matter (Numerically equal asel tar true yael.))
s.add('20')
'''

s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(len(s))