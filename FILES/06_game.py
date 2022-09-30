def game():
    return 4809
score=game()
with open('highscore.txt','r') as g:
    highscore=int(g.read())
    

if highscore<score:

    with open('highscore.txt','w') as g:
        g.write(str(score))


