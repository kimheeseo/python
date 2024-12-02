a = int(input())
min_surface_area = float('inf')  # 최소 표면적
best_dimensions = (0, 0, 0)

# 모든 약수 i에 대해
for i in range(1, int(a ** (1/3)) + 2):  # +2로 범위를 안전하게 설정
    if a % i == 0:
        for j in range(i, int((a // i) ** 0.5) + 1):  # +2로 범위 조정
            if (a // i) % j == 0:
                k = (a // i) // j
                if k > 0:  # k가 유효한 값인지 확인
                    # 현재 표면적 계산
                    current_surface_area = 2 * (i * j + j * k + k * i)
                    # 최소 표면적 갱신
                    if current_surface_area < min_surface_area:
                        min_surface_area = current_surface_area
                        best_dimensions = (i, j, k)

# 결과 출력
print(*best_dimensions)