import sys
for i in sys.stdin:
    print(["N","Y"][int(i)%6==0])