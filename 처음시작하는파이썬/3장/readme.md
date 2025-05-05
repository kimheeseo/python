Ver. 2025.05.03

# 리스트의 끝에 항목 추가하기: append()
- append(): 리스트의 긑에 새 항목을 추가한다.
- insert(): 원하는 위치에 항목을 추가한다.

# 값으로 항목 삭제하기: remove()
- marxes=['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
- marxes.remove('Gummo')
- marxes:['Groucho','Chico','Harpo','Zeppo']

+) 만약 append()로 새로운 항목을 끝에 추가한 뒤, pop()으로 다시 마지막 항목을 제거했다면, 여러분은 LIFO(Last in First out:후입선출) 자료구조인 스택(stack)을 구현한 것이다.

# 값으로 항목 오프셋 찾기: index()
- 항목 값의 리스트 오프셋을 알고 싶다면 index()를 사용하면된다.
- marxes.index('Chico') -> output: 1

# 튜플
- 튜플은 불변하다.: 튜플을 정의한 후에는 추가, 삭제, 수정을 할 수 없다.

ex)
- marx_tuple=('Groucho','Chico','Harpo')
- a,b,c=marx_tuple
- a: 'Groucho'
- b: 'Chico'
- c: 'Harpo'

- 튜플은 더 적은 공간을 사용한다.
- 실수로 튜플의 항목이 손상될 염려가 없다.
- 튜플을 딕셔너리 키로 사용할 수 있다.

# 딕셔너리
- 딕셔너리는 변경 가능하므로 키-값 요소를 추가, 삭제, 수정할 수 있다.
- 값에 상응하는 고유한 키(key)를 지정한다.

- 딕셔너리 생성하기: {}
- 딕셔너리를 생성하기 위해서는 중괄호 안에 콤마로 구분된 키:값 쌍을 지정한다.

ex)
- bierce={'m':'a', 'n':'b'}
- dict()함수를 사용해서 두 값으로 이루어진 시퀀스를 딕셔너리로 변환할 수 있다.

- 모든 항목 삭제하기: clear()
- 딕셔너리에 있는 키와 값을 모두 삭제하기 위해서는 clear()를 사용하거나, 빈 딕셔너리를 이름에 할당한다.

# Proper Subset
- 'A' is a proper subset of 'B' if and only if every element in 'A' is also in 'B', and there exist at least one element in 'B' that is not in 'A'.
- A]={1,2,3}, B={1,2,3,4}: 'A' is a proper subset of 'B'.
