# 해당 문제는 부동소수점 오차 보정 관련 문제가 중요한 개념.
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D+', 'D0', 'D-', 'F']
score = [4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]

total_score = 0  # 총 점수의 합
total_credits = 0  # 총 학점 수
n = int(input())  # 수강 과목 수

for _ in range(n):
    a = input().split()  # 과목명, 학점, 성적
    credits = int(a[1])  # 학점
    grade_index = grade.index(a[2])  # 성적 인덱스
    total_score += credits * score[grade_index]
    total_credits += credits

# 평균 학점 계산 및 소수점 출력
gpa = total_score / total_credits
print(format(round(gpa + 1e-9, 2), ".2f"))  # 부동소수점 오차 보정
