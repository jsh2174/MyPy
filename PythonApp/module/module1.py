import calculator               # 전체 포함 

from calculator import plus     # 특정 함수만 포함 

from calculator import plus, minus # 여러개의 함수 포함 

from calculator import *  # 와일드 카드 사용 
#===================================================================================================
# 모듈 파일을 찾는 순서 
#  1) 파이썬 인터프리터 내장 모듈 
#  2) sys.path에 정의 되어 있는 디렉토리 탐색  
#===================================================================================================
import sys 
# 1. 내장 모듈 출력 
print(sys.builtin_module_names)  
# 2. sys.path에 설정된 모듈  

for path in sys.path :
    print(path)


# print( plus(10,20))





