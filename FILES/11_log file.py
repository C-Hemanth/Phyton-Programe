with open ('log.txt')as g:
    h=g.read()                                # by  taking the log file from internet copy and create txt filke in this and there we cvan use lower()
    # h=g.read().lower()       # by  taking the log file from internet copy and create txt filke in this and there we cvan use lower()

if 'JOHNNY DEPP' in h:
    print('yes')
else:
    print('no')