Ver. 2025.05.10
# 스택 + 큐 == 데크
- 데크: 스택과 큐의 기능을 모두 가진 출입구가 양 끝에 있는 큐.
- 시퀀스의 양 끝으로부터 항목을 추가하거나 삭제할 때 유용하게 쓰인다.
- poplef()함수: 데크로부터 왼쪽 끝의 항목을 제거한 후, 그 항목을 반환한다.
- pop()함수: 오른쪽의 항목을 제거한 후, 그 항목을 반환한다.
- 양쪽 끝에서부터 이 두함수가 중간 지점을 향해서 동작한다.
- 양쪽 문자가 서로 일치한다면 단어 중간에 도달할때까지 데크를 팝한다.
