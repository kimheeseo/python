def solution(n):
    if 620 <= n <= 780:
        return 'Red'
    elif 590 <= n < 620:
        return 'Orange'
    elif 570 <= n < 590:
        return 'Yellow'
    elif 495 <= n < 570:
        return 'Green'
    elif 450 <= n < 495:
        return 'Blue'
    elif 425 <= n < 450:
        return 'Indigo'
    elif 380 <= n < 425:
        return 'Violet'
 
 
if __name__ == '__main__':
    n = int(input())
    result = solution(n)
    print(result)