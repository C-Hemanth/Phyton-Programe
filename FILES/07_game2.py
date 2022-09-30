def game():
    return 563

score = game()                                                                      # read the given score
with open("highscore.txt") as h:
    highscore=h.read()
   
if highscore=='':                                  # if highscore is blank then we get the value what we have given in the score
    with open("highscore.txt", "w") as h:
        h.write(str(score))

elif int(highscore)<score :                # or if no blank is there then it checks the condition and print it in the highscore.txt
    with open("highscore.txt", "w") as h:
        h.write(str(score))        
       
    

