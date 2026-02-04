'''
상속

형식 :
class 슈퍼클래스:
    본문

class 서브클래스(슈퍼클래스)
    본문
'''
class Person:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name}이(가) {food}을(를) 먹습니다.')

    def drink(self, drink_name):
        print(f'{self.name}이(가) {drink_name}을(를) 먹습니다.')

person1 = Person('김영')
person1.eat('감자')

# 서브 클래스의 정의
class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def study(self):
        print(f'{self.name}은(는) {self.school}에서 공부를 합니다.')

    def drink(self, drink_name):
        print(f'{self.school}에서', end=' ')
        super().drink(drink_name)

# 서브 클래스의 객체 생성
potter = Student(name='해리포터', school='호그와트')
potter.study()
potter.eat('라멘')   # 부모의 메서드를 정의하는 일 없이 그대로 쓸 수 있음
potter.drink('투샷아이스아메리카노')      # overriding된 메서드를 호출
'''
1. 서브 클래스의 __init__()
    Java와 마찬가지로 서브 클래스는 슈퍼 클래스가 없으면 존재할 수 없습니다. 그래서 서브 클래스의 생성자를 구현할 때는 '반드시 슈퍼 클래스의 생성자를 먼저 호출'하는 코드를 작성하셔야 합니다.
    
    super()는 잘 생각해보시면 슈퍼 클래스의 생성자라고 해석할 수 있을 겁니다. potter = Student()에서 보면 알 수 있듯이. 그러면 슈퍼 클래스의 객체가 .__init__(name)이라는 메서드를 호출했다고 해석할 수 있겠네요. 즉, 이상의 코드에서 Student 생성자의 호출이 완벽하게 마무리 되려면 super().__init__(name)에 의해서 슈퍼 클래스인 Person의 생성자가 먼저 호출이 완료되고 -> Person클래스의 인스턴스가 생성됩니다. 이후에 슈퍼 클래스의 인스턴스 변수인 name이 서브 클래스로 전달되고, 그 다음 서브 클래스에서 school 인스턴스 변수를 선언 및 초기화하여 서브 클래스의 인스턴스가 생성완료됩니다.
    
    : 생성자를 호출했다면 -> 객체가 생성되었다고 볼 수 있는데 -> 그렇다면 부모 클래스의 인스턴스와 자식 클래스의 인스턴스가 있는거 아니냐 -> 맞긴한데 그러면 별개의 인스턴스라고 봐야 하냐면 그게 또 좀 애매합니다.
    
    Java에서는 super() -> 얘는 생성자 / super.메서드명() 으로 super 자체가 객체인 경우가 있었지만 python에서는 super()로 일원화되어있습니다. 

2. 서브 클래스의 인스턴스 자료형
    슈퍼 클래스의 객체는 슈퍼 클래스의 인스턴스
    서브 클래스의 인스턴스는 서브 클래스의 인스턴스이면서 동시에 슈퍼 클래스의 인스턴스(부모 생성자 호출 했으니까요)
    Student 클래스의 객체는 Student의 인스턴스이면서 Person의 인스턴스.
    
    Java를 기준으로 instanceof 연산자 역할을 하는 것이 JS에서는 typeof 연산자가 있었는데, python에서는 isinstance() 함수가 있습니다. -> 다 소문자입니다.

형식 :
isinstance(객체명, 클래스명) -> boolean
'''
print(isinstance(potter, Student))  # 결과값 : True
print(isinstance(potter, Person))   # 결과값 : True
print(isinstance(person1, Student)) # 결과값 : False
print(isinstance(person1, Person))  # 결과값 : True
print(issubclass(Student, Person))  # 결과값 : True 객체 안만들고 클래스 간의 위계만 확인하고 싶으면 쓸 수 있겠습니다.

'''
3. 다음 지시 사항을 읽고 Hybrid 클래스를 구현하시오.

지시 사항
1. 다음과 같은 슈퍼 클래스 Car를 가지고 있는 Hybrid 클래스를 구현하시오.
2. 서브 클래스 Hybrid는 다음과 같은 특징을 지니고 있습니다.
    1) 최대 배터리 충전량은 30
    2) 배터리를 충전하는 charge() 메서드가 존재합니다. 최대 충전량을 초과할 수 없고,
        0보다 작은 값으로 충전할 수 없습니다.
    3) 현재 주유량과 충전량을 모두 확인할 수 있는 hybrid_info() 메서드가 있습니다.
    
3. 다음과 같은 방식으로 전체 동작을 확인할 수 있습니다.
car = Hybrid(oil= 0, amount= 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

실행 예

하이브리드 차량이 생산되었습니다.
기름을 50 주유 했습니다.
전기를 30 충전 했습니다.
현재 주유 상태 : 50
현재 충전 상태 : 30

'''
