for i in range(2, 21):
    with open('multipli.txt','w') as h:
    # with open(f"tables/multipli_tables_of_{i}.txt",'w') as h:  # or we can create folder to keep and 'F' is used to print directly the output
        for j in range (1,11):
            h.write(f"{i}*{j}={i*j}")
            if j!=10:
                h.write('\n')
               





g=563
with open('multiplication.txt','w') as h:
    for i in range(1,11):
        h.write(f"{g}*{i}={g*i}\n")                                             # we use'F' it is also called as f strings
        # h.write(str(g) + "X" + str(i) + "=" + str(g*i))           # because if we dont use 'F'we should type in a big statement
        # if i !=10:
            # h.write('\n')