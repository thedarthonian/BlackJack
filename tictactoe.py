from tkinter import *
tk=Tk()
tk.title("Tic Tac Toe")
r=1
s1="null"
s2="null"
s3="null"
s4="null"
s5="null"
s6="null"
s7="null"
s8="null"
s9="null"
chosen = []
def winCheck(button,num):
    global r
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    if s1 == "X" and s2 == "X" and s3 == "X" or s4 == "X" and s5 == "X" and s6 == "X" or s7 == "X" and s8 == "X" and s9 == "X" or s1 == "X" and s4 == "X" and s7 == "X" or s2 == "X" and s5 == "X" and s8 == "X" or s3 == "X" and s6 == "X" and s9 == "X" or s1 == "X" and s5 == "X" and s9 == "X" or s3 == "X" and s5 == "X" and s7 == "X":
        button["text"] = "X WINS"
        tk.title("X WINS!")
        r=99
        return 1
    if s1 == "O" and s2 == "O" and s3 == "O" or s4 == "O" and s5 == "O" and s6 == "O" or s7 == "O" and s8 == "O" and s9 == "O" or s1 == "O" and s4 == "O" and s7 == "O" or s2 == "O" and s5 == "O" and s8 == "O" or s3 == "O" and s6 == "O" and s9 == "O" or s1 == "O" and s5 == "O" and s9 == "O" or s3 == "O" and s5 == "O" and s7 == "O":
        button["text"] = "O WINS"
        tk.title("O WINS!")
        r=99
        return 1
    return 0
def onClick(button,num):
    global r
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    global chosen
    if r > 9:
        return
    if button in chosen:
        return
    if winCheck(button,num) == 0:
        if r % 2 == 0:
            player = "O"
        else:
            player = "X"
        button["text"] = player
        if num == 1:
            s1=player
        if num == 2:
            s2=player
        if num == 3:
            s3=player
        if num == 4:
            s4=player
        if num == 5:
            s5=player
        if num == 6:
            s6=player
        if num == 7:
            s7=player
        if num == 8:
            s8=player
        if num == 9:
            s9=player
        winCheck(button,num)
        chosen.append(button)
        r=r+1
buttons=StringVar()
button1 = Button(tk,text=" ",font=('Helvetica 20'),bg='darkred',fg='white',height=4,width=9,command=lambda:onClick(button1,1))
button1.grid(row=1,column=0)
button2 = Button(tk,text=' ',font=('Helvetica 20'),bg='black',fg='white',height=4,width=10,command=lambda:onClick(button2,2))
button2.grid(row=1,column=1)
button3 = Button(tk,text=' ',font=('Helvetica 20'),bg='darkred',fg='white',height=4,width=9,command=lambda:onClick(button3,3))
button3.grid(row=1,column=2)
button4 = Button(tk,text=' ',font=('Helvetica 20'),bg='black',fg='white',height=4,width=9,command=lambda:onClick(button4,4))
button4.grid(row=2,column=0)
button5 = Button(tk,text=' ',font=('Helvetica 20'),bg='darkred',fg='white',height=4,width=10,command=lambda:onClick(button5,5))
button5.grid(row=2,column=1)
button6 = Button(tk,text=' ',font=('Helvetica 20'),bg='black',fg='white',height=4,width=9,command=lambda:onClick(button6,6))
button6.grid(row=2,column=2)
button7 = Button(tk,text=' ',font=('Helvetica 20'),bg='darkred',fg='white',height=4,width=9,command=lambda:onClick(button7,7))
button7.grid(row=3,column=0)
button8 = Button(tk,text=' ',font=('Helvetica 20'),bg='black',fg='white',height=4,width=10,command=lambda:onClick(button8,8))
button8.grid(row=3,column=1)
button9 = Button(tk,text=' ',font=('Helvetica 20'),bg='darkred',fg='white',height=4,width=9,command=lambda:onClick(button9,9))
button9.grid(row=3,column=2)

tk.mainloop()
