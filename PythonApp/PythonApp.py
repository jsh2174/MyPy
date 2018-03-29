


def add (list):
    data = input()
    list.append(data);

def show(list) : 
    print("---- list ---- ")
    for val in list :
        print(var)

def remove(list) :
    key = input()
    if( list.index(key)) :
        list.remove()
        show(list)
    else : 
        print("none data!!")

if __name__ == '__main__':

    list = []
    
while True : 
       print( '1. insert ') 
       print( '2. remove ') 
       print( '3. show  ') 
       print( '0. exit' ) 
       key = int(input())

       if( key == 1) :
           add(list)
       elif(key == 2) :
           remove(list)
       elif(key == 3) :
           show(list)
       elif(key == 0) :
           exit(0)
