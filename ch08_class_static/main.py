'''
1. 클래스 변수 vs. 인스턴스 변수
    인스턴스 변수 : 인스턴스 마다 서로 다른 값
    클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수

    인스턴스 변수 접근 방식 - 인스턴스 접근(o) / 클래스 접근(x)
    클래스 변수 접근 방식 - 인스턴스 접근(o) / 클래스 접근(o)
'''
# 클래스 변수 예시
class Korean:
    country = '한국'                   # 클래스 변수 # 1
    def __init__(self, name, age, address):
        self.name = name            # 인스턴스 변수 # 1
        self.age = age              # 인스턴스 변수 # 2
        self.address = address      # 인스턴스 변수 # 3
# 객체 생성
korean = Korean('김일', 21, '서울특별시 마포구')
print(korean.name)      # 인스턴스 변수 참조
# 클래스 변수 참조
print(korean.country)   # 객체명.클래스변수명 으로 접근 가능
print(Korean.country)   # 클래스명.클래스변수명 으로 접근 가능

'''
객체명.클래스변수명을 통해서 클래스 변수에 접근이 가능하긴 한데, 클래스 내부 코드를 보기 전까지는 country라는 변수가 인스턴스 변수인지 클래스 변수인지 알 방법이 없습니다.

이상을 이유로 클래스 변수를 확인하고자 할 때는 객체명.클래스변수명 보다는
클래스명.클래스변수명을 통해서 참조하는 것이 권장됩니다.

2. 클래스 메서드
'''
class Korean2:
    country = '대한민국'        # 클래스 변수의 선언 및 초기화
    # 클래스 메서드의 정의 방법
    @classmethod                # @ decorator를 달면 됩니다.
    def trip(cls, travelling_site):
        if cls.country == travelling_site:
            print('국내 여행입니다.')
        else:
            print('해외 여행입니다.')
# 클래스 메서드 호출
Korean2.trip('대한민국')
Korean2.trip('미국')
# 객체 생성
person2 = Korean2()
person2.trip('일본')      # 객체명.클래스메서드() 호출도 가능하긴 합니다. 근데 마찬가지로 권장되지 않습니다.

'''
3. 정적 메서드(static method)




'''