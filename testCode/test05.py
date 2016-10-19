#coding:utf-8

a = 'aaaaaaa'

print a

a += 'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'

print a

b = 'b'

while b in 'bbbbbbbbbbbbbbbbb':
    print 'c'
    b += '{}'.format('b')
    print b

print 'd'