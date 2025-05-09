Ver. 2025.05.05
# 4장 파이 크러스트: 코드 구조

# 코멘트 달기: #
- 프로그램에서 코멘트는 인터프리터에 의해 무시되는 텍스트의 한 부분이다.
- 코드를 설명하거나 나중에 어떤 문제를 고치기 위해 표시를 하는 등 다양한 목적으로 코멘트를 사용할 수 있다.

# for: 순회하기
- 파이썬에서 이터레이터(iterator)란, 요소를 하나씩 순서대로 꺼낼 수 있는 객체.

# 컴프리헨션: Comprehension
- 컴프리헨션은 하나 이상의 이터레이터로부터 파이썬의 자료구조를 만드는 콤팩트한 방법.
- 리스트 컴프리헨션
- [표현식 for 항목 in 순회 가능한 객체]
- 리스트 컴프리헨션은 대괄호 안에 루프가 있다.
ex) number for number in range(1,6)

# 이터레이터
- number_list=[]
- for number in range(1,6):
-   number_list.append(number)

  
- range(1,6): 이터러블(iterable) 객체.
- 이터러블: _iter_() 메서드를 가지고 있는 객체이며, 이터레이터를 생성할 수 있습니다.
- for문은 내부적으로 다음 과정을 자동으로 수행합니다.
1) iter(range(1,6))을 호출하여 이터레이터(iterator)를 생성합니다.
2) 이 이터레이터는 _next_() 메서드를 통해 값을 하나씩 꺼냅니다.
3) 더 이상 꺼낼 값이 없으면 stopiteration 예외가 발생하고 반복이 종료됩니다.

# 함수
- 파이썬 함수를 정의하기 위해서는 def와 함수 이름, 괄호를 입력한다.
- 괄호 안에는 옵션으로 매개변수를 입력할 수 있다. 그리고 마지막으로 콜론(:)을 붙인다.
- 함수로 전달한 값을 인자(argument)라고 부른다. 인자와 함수를 호출하면 인자의 값은 함수내에서 해당하는 매개변수에 복사된다.

- ex) echo('Rumplestiltskin')
- echo: 함수, 'Rumplestiltskin': 인자

# 에러 처리하기: try, except
- try 블록 안의 코드를 실행할 때 에러가 있다면 예외가 발생하고 except 블록 내의 코드가 실행된다.
- 만약 try 블록 안에 에러가 없다면 except 블록을 건너뛴다.
- except 예외 타입 as 이름: IndexError = 시퀀스에서 잘못된 위치를 입력할 때 발생하는 예외타입.

ex)
- try:
- except IndexError as err:
- except Exception as other: #other 변수에 다른 기타 예외를 저장.
