h=5
# i=1                                                     # for normal order of multiplication
i=10                                                  # for reverse order of multiplication
while i>0:
    print(f"{h}*{i}={h*i}")
    # i=i+1                                               # for normal order of multiplcation
    i=i-1                                                # for reverse order of multiplication
    # if i==11:
    if i==0:
        break