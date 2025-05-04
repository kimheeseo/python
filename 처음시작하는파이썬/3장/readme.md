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

- ex)
- marx_tuple=('Groucho','Chico','Harpo')
- a,b,c=marx_tuple
- a: 'Groucho'
- b: 'Chico'
- c: 'Harpo'
