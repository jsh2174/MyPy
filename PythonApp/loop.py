print('input ') 
# 파이썬은 무조건 문자열 입력  (캐스팅 필요) 
'''
dic = {'애플': 'www.apple.com',
       '파이썬': 'www.python.org',
       '마이크로소프트': 'www.microsoft.com'}


for key, value in dic.items() :
    print( ' {0} : {1} '.format(key,value))
''' 

'''
for i in range(0,5) :
    for j in range(0,i):
        print('*', end = "",)
    print('')
for i in range(0,5) :
    for j in range(i,5):
        print('*', end = "",)
    print('')
for i in range(0,5) :
    for j in range(0,i):
        print('*', end = "",)
    print('')
for i in range(0,5) :
    for j in range(i,5):
        print('*', end = "",)
    print('')
'''

'''
for i in range(1,9): 
    for j in range(1, 9):
        print('{0} x {1} = {2}'.format( i , j , i * j) )
'''
'''
for i in range(5):
    print(i)
'''
'''
for i in range(0,10,2): 
    print(i)
'''
'''
for i in range(0,10,1): 
    print(i)
'''


'''
for s in ['뇌를', '자극하는', '파이썬']:
    print(s) 

for s in ['뇌를', '자극하는', '파이썬']:
    print(s) 
'''



'''
for s in ['aaa','bbb','ccc'] :
    print(s)
'''
'''
for i in (1,2,3): 
    print( i )
'''







# 무한 루프 
'''
while True: 
    limit = int(input())

    if limit == 0 :
        break;
'''
'''
while limit > 0 : 
    print('{0} turn ...'.format(limit))
    limit -=1
'''    

  





'''
if a < 10 : 
    if a > 5 : 
        print(' range : 5 ~10 ')
'''

'''
if a == 1 : 
    print(a)
elif a==2: 
    print(a)
elif a==3:
    print(a)
elif a==4 :
    print(a)
else :
    print('out of range ~~')
'''


'''
if a != 0 : 
    a /= 2 
else  : 
    print('0 나누기 불가')

print ( a )
'''

"""
if a % 2 == 0 :
    print('짝수') 
else : 
    print('홀수') 
"""
