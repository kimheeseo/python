def classify_mail(dimensions):
    length, height, thickness = sorted(dimensions, reverse=True)
    
    # 편지 조건
    if (125 <= length <= 290 and
        90 <= height <= 155 and
        0.25 <= thickness <= 7):
        return "letter"
    
    # 소포 조건
    elif (length <= 380 and height <= 300 and thickness <= 50 and
          length >= 125 and height >= 90 and thickness >= 0.25 and
          (length > 290 or height > 155 or thickness > 7)):
        return "packet"
    
    # 소화물 조건
    elif (length >= 125 and height >= 90 and thickness >= 0.25 and
          (length > 380 or height > 300 or thickness > 50) and
          (length + 2*(height + thickness) <= 2100)):
        return "parcel"
    
    else:
        return "not mailable"

while True:
    dimensions = list(map(float, input().split()))
    if dimensions == [0, 0, 0]:
        break
    print(classify_mail(dimensions))