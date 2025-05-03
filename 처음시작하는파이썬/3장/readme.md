Ver. 2025.05.03

# 리스트의 끝에 항목 추가하기: append()
- append(): 리스트의 긑에 새 항목을 추가한다.
- insert(): 원하는 위치에 항목을 추가한다.

# 값으로 항목 삭제하기: remove()
- marxes=['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
- marxes.remove('Gummo')
- marxes:['Groucho','Chico','Harpo','Zeppo']

+) 만약 append()로 새로운 항목을 끝에 추가한 뒤, pop()으로 다시 마지막 항목을 제거했다면, 여러분은 LIFO(Last in First out:후입선출) 자료구조인 스택(stack)을 구현한 것이다.
