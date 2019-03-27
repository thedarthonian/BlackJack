import random
import time
userscore = 0
compscore = 0
while True:
    print("\n")
    print("CURRENT SCORE\nYou "+str(userscore)+" :: "+str(compscore)+" Computer\n")
    total = 0
    def newCard():
        card = random.choice(["Hearts", "Spades", "Diamonds", "Clubs"])
        num = random.randint(1, 14)
        if num <= 10:
            dnum = num
        if num == 11:
            dnum = "Jack"
            num=10
        if num == 12:
            dnum = "King"
            num=10
        if num == 13:
            dnum = "Queen"
            num=10
        if num == 14:
            dnum = "Ace"
            while num != 11 and num != 1:
                try:
                    num=int(input("You scored an Ace! Would you like it to act as 11 or 1?: "))
                except ValueError:
                    x=0
        #print("[DEBUG]"+str(num))
        return str(dnum)+" of "+card, int(num)
    c1=newCard()
    print("Card: "+str(c1[0]))
    total=total+c1[1]

    c2=newCard()
    print("Card: "+str(c2[0]))
    total=total+c2[1]

    playing = True
    while playing == True:
        print("Current Total: ["+str(total)+"]")
        if total > 21:
            print ("BUST - YOU LOSE!")
            compscore=compscore+1
            playing = False
        if playing == False:
            break
        cont=input("Call or Hold?: ")
        if "c" in cont.lower():
            c=newCard()
            print("Card: "+str(c[0]))
            total=total+c[1]
        elif "h" in cont.lower() or total == 21:
            print("Computer Playing...")
            time.sleep(random.randint(1,2))
            cscore = random.randint(total - 2, total + 3)
            print("Computer Score: "+str(cscore))
            if total > cscore and cscore <= 21 or cscore > 21:
                print("YOU WIN!")
                userscore=userscore+1
                break
            if total < cscore:
                print("YOU LOSE!")
                compscore=compscore+1
                break
            if total == cscore:
                print("DRAW!")
                break
        else:
            print("Not recognised... CALL or HOLD")
        print("\n")
