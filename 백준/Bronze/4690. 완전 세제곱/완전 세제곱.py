for a in range(2,101):
  for i in range(2,101):
    for j in range(i+1,101):
      for k in range(j+1, 101):
        if (i**3 + j**3 + k**3) == a**3:
            print("Cube = {}, Triple = ({},{},{})".format(a,i,j,k))
        if (i**3 + j**3 + k**3) > a**3:
            break