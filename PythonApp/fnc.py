def my_abs( arg ):
    if arg < 0 :
         arg =  arg * -1
    return  arg;

def hello() : 
    print("hello")

def print_string(txt = "기본 문자열",  cnt  = 1) : 
    for i in range(cnt) :
        print(txt)

def var_arg( *str ) : 
    for s in str : 
           print(s)

# 파라미터 맵 자동 변환 !! 
def player_info ( **player ): 
    for info in player : 
        print(info)


def team_player( teamname,  *player ) :
    print( teamname )
    for p  in player : 
        print(p)

def print_argv( * argv ,  argc = 4) : 
       for i in range(argc) : 
           print(argv[i])



def multiply(a,b) : 
    return a* b 

result = multiply(10,10)
print( result ) 






























   
#for ar in argv : 
#     print(ar)
#print_argv( 'aaa','bbb','ccc',3)
#team_player( teamname = 1234 , '이승엽', '이동국', '정현')
#var_arg( 'AAA','BBB', 'CCC', 'DDD', 'EEE' )
#print_string(cnt = 5)
#hello()
#print( abs( ))

