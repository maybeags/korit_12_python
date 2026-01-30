'''
1. while 반복문
    while 다음에 나오는 조건식이 참이라면 이하의 실행문이 반복 실행됨(조건이
    False가 될 때까지)
형식 :
while 조건식1:
    반복실행문1

당연히 특정 시점에 while 반복문이 종료될 수 있도록 지정해주셔야 합니다.
중첩 while문 당연히 가능.

기본 예제
1부터 10까지 출력하기
'''
n = 1
while n < 11:
    print(n, end=' / ')
    n += 1          # python에는 ++가 없습니다...
'''
기본 예제 # 2
10부터 1까지 역순으로 출력하시오.
'''
print()
n2 = 10
while n2 > 0:
    print(n2, end=' / ')
    n2 -= 1
'''
중첩 while 문 (while문 뿐만 아니라 내부에 if를 쓸 수도 있겠습니다)
중첩 while 및 f-string을 활용하여
기본 예제

구구단 2단부터 9단까지 출력하는 프로그램을 작성하시오.(while문 사용할 것)
변수명은 dan / number로 하겠습니다.
실행 예
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
...
9 x 8 = 72
9 x 9 = 81
'''
dan = 2
while dan < 10:                                     # 조건문1
    number = 1                                      # 반복실행문1-a
    while number < 10:                              # 조건문2
        print(f'{dan} x {number} = {dan*number}')   # 반복실행문2
        number += 1
    dan += 1                                        # 반복실행문1-b
    print()


print(number)       # 전역 / 지역 변수의 개념이 java와는 다릅니다.