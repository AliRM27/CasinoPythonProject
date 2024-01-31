from random import *
from tkinter import *
from tkinter.messagebox import *
from time import sleep


def main():
    global usernameEntry, passwordEntry, menu, title, loginButton, registerButton, Or, labelPassword, labelUsername, infoLabel
    menu = Tk()
    menu.geometry(f"400x400")
    menu.resizable(False, False)
    menu.title("Casino")

    frame = Frame(menu, width=1380, height=730)
    frame.grid(row=0, column=0, padx=10, pady=10)

    title = Label(menu, text="Casino", font=("arial", 45))
    title.place(x=115, y=40)

    loginButton = Button(menu, text="Login", font=(10), width=7, command=login)
    loginButton.place(x=115, y=320)
    Or = Label(menu, text="or", font=(10))
    Or.place(x=200, y=325)
    registerButton = Button(menu, text="Register", font=(10), width=7, command=register)
    registerButton.place(x=230, y=320)

    labelUsername = Label(menu, text="Username", font=(10))
    labelUsername.place(x=170, y=140)
    labelPassword = Label(menu, text="Password", font=(10))
    labelPassword.place(x=170, y=210)

    usernameEntry = Entry(menu, font=("arial", 13))
    usernameEntry.place(x=115, y=170)
    passwordEntry = Entry(menu, font=("arial", 13), show="*")
    passwordEntry.place(x=115, y=240)

    infoLabel = Label(menu, text="", font=("arial", 13),)
    infoLabel.place(x=190, y=280)

    menu.mainloop()


def confirm():
    global UserPassword, passwordLabel
    newPassword = ""
    with open("data.txt", "r") as file:
        data = file.readlines()
        newData = []
        for line in data:
            line = line.strip()
            username, _, score, allTime = line.split(" ")
            if username == name and name != changeEntry.get().strip():
                if changeEntry.get() == "" or " " in changeEntry.get():
                    errorLabel["text"] = "Invalid Password"
                    errorLabel["fg"] = "red"
                    errorLabel.place(x=100, y=140)
                else:
                    line = f"{username} {changeEntry.get().strip()} {score} {allTime}"
                    newPassword = changeEntry.get().strip()
                    UserPassword = newPassword
                    errorLabel["text"] = "New Password is Valid"
                    errorLabel["fg"] = "green"
                    errorLabel.place(x=100, y=140)
            elif username == name and name == changeEntry.get().strip():
                errorLabel["text"] = "Username and password have to be different"
                errorLabel["fg"] = "red"
                errorLabel.place(x=70, y=140)
            newData.append(line)
    with open("data.txt", "w") as file:
        for i, val in enumerate(newData):
            file.write(val)
            if i == len(newData)-1:
                pass
            else:
                file.write("\n")

    passwordLabel["text"] = f"Password: {len(newPassword)*'*'}"
    remove_widgets(changeEntry, confirmButton)
    changeButton.place(x=220, y=180)


def change_password():
    global changeEntry, confirmButton
    errorLabel["text"] = ""
    changeEntry = Entry(acc, font=("arial", 13))
    changeEntry.place(x=105, y=120)
    changeButton.place(x=10000, y=1000)
    confirmButton = Button(acc, text="Confirm", font=(5), command=confirm)
    confirmButton.place(x=220, y=160)


def account():
    global acc, changeButton, passwordLabel, errorLabel, recordLabel
    record = ""
    allTimeWinnings = ""
    switch("disabled", accountButton)
    acc = Tk()
    acc.title("Account")
    acc.geometry("400x400")
    acc.resizable(False, False)

    labelTitle = Label(acc, text="Your account", font=("arial", 20))
    labelTitle.place(x=120, y=20)

    nameLabel = Label(acc, text=f"Username: {name}", font=("arial", 13))
    nameLabel.place(x=20, y=80)
    passwordLabel = Label(acc, text=f"Password: {len(UserPassword)*'*'}", font=("arial", 13))
    passwordLabel.place(x=20, y=120)

    changeButton = Button(acc, text="Change Password", font=(5), width=15, command=change_password)
    changeButton.place(x=220, y=180)

    errorLabel = Label(acc, text="", font=("arial", 13))
    errorLabel.place(x=110, y=150)

    with open("data.txt", "r") as file:
        data = file.readlines()
        for line in data:
            line = line.strip()
            username, _, score, allTime = line.split(" ")
            if username == name:
                record = score
                allTimeWinnings = allTime

    recordLabel = Label(acc, text=f"Record winnings: ${record}", font=("arial", 13))
    recordLabel.place(x=20, y=250)

    allTimeLabel = Label(acc, text=f"All-time winnings: ${allTimeWinnings}", font=("arial", 13))
    allTimeLabel.place(x=20, y=300)

    back = Button(acc, text="Back", font = ("arial", 13), command=lambda:close(acc, accountButton))
    back.place(x=320, y=350)
    acc.mainloop()


def rules():
    global rul
    switch("disabled", rulesButton)
    rul = Tk()
    rul.geometry("500x250")
    rul.resizable(False, False)
    rul.title("Rules")

    txt = Label(rul, text="Rules: In this game you will test your luck! \n You will play games of chance and your goal \n is to win as much money as possible. \n You start with $1,000. But you can only play 10 games.", font=("arial", 13))
    txt.place(x=50, y=50)

    back = Button(rul, text="Back", font=("arial", 13), command=lambda:close(rul, rulesButton))
    back.place(x=420, y=200)

    rul.mainloop()


def draw():
    global points
    card = choice(cards)
    cards.remove(card)
    if card in ["Jack", "Queen", "King"]:
        points += 10
    elif card == "Ace":
        points += 1
    else:
        points += card

    infoCard["text"] = "You drew a card: " + str(card)
    infotxt["text"] = "Points: " + str(points)

    if points > 21:
        infotxt["text"] = "Points: " + str(points) + "\n You have more than 21 points, which means you lost."
        infotxt.place(x=70, y=390)
        Button(bj, text="Leave", font=("arial", 13), command=lambda:close(bj, playBJ, playR, playWOF, accountButton, rulesButton, exitButton)).place(x=420, y=450)
        switch("disabled", stopButton, drawButton)


def stop():
    global money
    score = {21: 1000, 20: 500, 19: 300, 18: 200, 17: 100}
    switch("disabled", stopButton, drawButton)
    Button(bj, text="Leave", font=("arial", 13), command=lambda:close(bj, playBJ, playR, playWOF, accountButton, rulesButton, exitButton)).place(x=420, y=450)
    if points in score:
        infotxt["text"] = f"Points: {points} \n You have won ${score[points]}!"
        money += score[points]
        infotxt.place(x=193, y=390)
        bankLabel["text"] = f"Bank: ${money}"
    else:
        infotxt["text"] = f"Points: {points} \n You have won nothing."
        infotxt.place(x=185, y=390)


def exit_and_save():
    menu.destroy()
    with open("data.txt", "r") as file:
        data = file.readlines()
        newData = []
        for line in data:
            line = line.strip()
            username, password, score, allTime = line.split(" ")
            if username == name:
                if int(score) < money-1000:
                    line = f"{username} {password} {str(money-1000)} {str(int(allTime) + int(money-1000))}"
            newData.append(line)

    with open("data.txt", "w") as file:
        for i, val in enumerate(newData):
            file.write(val)
            if i == len(newData)-1:
                pass
            else:
                file.write("\n")


def black_Jack():
    global cards, bj, infoCard, infotxt, points, stopButton, drawButton, money, tickets
    if money >= 200 and tickets > 0:
        pay(200)
        points = 0
        cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"] * 4
        shuffle(cards)
        switch("disabled", playBJ, playWOF, playR, accountButton, rulesButton, exitButton)
        bj = Tk()
        bj.geometry("500x500")
        bj.title("Black Jack")
        bj.resizable(False, False)
        Label(bj, text="Black Jack", font=("arial", 30)).place(x=160, y=20)
        Label(bj, text="\nYou draw a card from the deck. \nYou count this card as points. \nBut if you have more than 21 points \n then you have lost.", font=('arial', 13)).place(x=130, y=70)
        Label(bj, text="Wnnings: \n21 = $1,000 \n 20 = $500 \n 19 = $300 \n 18 = $200 \n 17 = $100", font=("arial", 13)).place(x=50, y=200)
        Label(bj, text="Ace = 1, faces = 10, \n numbers = their value", font=("arial", 13)).place(x=320, y=200)
        stopButton = Button(bj, text="Stop drawing", font=("arial", 13), command=stop)
        stopButton.place(x=360, y=310)
        drawButton = Button(bj, text="Draw a card", font=("arial", 13), command=draw)
        drawButton.place(x=210, y=310)
        infoCard = Label(bj, text="You drew a card: ", font=("arial", 13))
        infoCard.place(x=200, y=360)
        infotxt = Label(bj, text="Points: ", font=("arial", 13))
        infotxt.place(x=230, y=390)
        bj.mainloop()
    elif money < 200:
        showinfo(title="Not enough Money", message="You don't have enough money.")
    else:
        showinfo(title="Out of tickets", message="You've run out of tickets.")


def turn():
    global money
    nums = {1: 500, 2: 250, 3: 150, 4:100}
    switch("disabled", turnButton)
    num = 0
    t = 0.04
    randNum = randint(1, 10)

    for i in range(randNum + 60):
        num += 1
        if num == 11:
            num = 1
        if i % 10 == 0:
            t += 0.02
        wheel["text"] = f"Wheel: {str(num)}"
        sleep(t)
        wof.update()

    infoNum["text"] = f"You got: {randNum} so you won {f'{str(nums[randNum])}$' if randNum in nums else 'nothing.'}"
    Button(wof, text="Leave", font=(10), command=lambda:close(wof, playBJ, playR, playWOF, accountButton, rulesButton, exitButton)).place(x=320, y=400)
    if randNum in nums:
        money += nums[randNum]
        bankLabel["text"] = f"Bank: ${money}"

def wheel_of_fortune():
    global tickets, money, wof, wheel, turnButton, infoNum
    if money >= 100 and tickets > 0:
        switch("disabled", playBJ, playR, playWOF, accountButton, rulesButton, exitButton)
        pay(100)
        wof = Tk()
        wof.geometry("400x450")
        wof.title("Wheel of fourtune")
        wof.resizable(False, False)
        Label(wof, text="Wheel of Fortune", font=("arial", 30)).place(x=60, y=20)
        Label(wof, text="You turn the wheel that has 10 fields.\n The fields are numbered from 1 to 10.\n On the table you can see what you get.\n 1 = $500 \n 2 = $250 \n 3 = $150 \n 4 = $100 \n rest = $0", font=("arial", 13)).place(x=60, y=100)
        Label(wof, text=f"Chance to win {chance_calculator(4, 10)}", font=("arial", 13)).place(x=10, y=400)
        infoNum = Label(wof, text="", font=("arial", 13))
        infoNum.place(x=100, y=360)
        wheel = Label(wof, text="Wheel: 1", font=("arial", 15))
        wheel.place(x=170, y=270)
        turnButton = Button(wof, text="Turn the wheel", font=(10), command=turn)
        turnButton.place(x=155, y=310)
        wof.mainloop()
    elif money < 100:
        showinfo(title="Not enough Money", message="You don't have enough money.")
    else:
        showinfo(title="Out of tickets", message="You've run out of tickets.")


def check_spin(color: str):
    userColor = listbox.get(listbox.curselection())
    return True if color == userColor else False


def spin():
    global money
    switch("disabled", spinButton)
    listbox["state"] = "disabled"
    colorField = choice(["Black", "Red"])
    num = 0
    t = 0.04
    for i in range(60):
        num += 1
        if num == 11:
            num = 1
        if i % 10 == 0:
            t += 0.02
        labelinfo["text"] = f"Roulette: {'Black' if i%2==0 else 'Red'}"
        sleep(t)
        roulWin.update()
    labelinfo["text"] = f"Roulette: {'Black' if colorField=='Black' else 'Red'} \n The ball is on the {colorField} field \n {'so you $600' if check_spin(colorField) else 'so you won nothing.'}"
    labelinfo.place(x=90, y=420)
    if check_spin(colorField):
        money += 600
        bankLabel["text"] = f"Bank: ${money}"
    Button(roulWin, text="Leave", font=(10), command=lambda:close(roulWin, playBJ, playR, playWOF, accountButton, rulesButton, exitButton)).place(x=320, y=450)


def roulette():
    global labelinfo, roulWin, listbox
    if money >= 300 and tickets > 0:
        def list_selected(event):
            global spinButton
            spinButton = Button(roulWin, text="Spin", font=(10), command=spin)
            spinButton.place(x=170, y= 370)

        switch("disabled", playBJ, playR, playWOF, accountButton, rulesButton, exitButton)
        pay(300)
        roulWin = Tk()
        roulWin.geometry("400x500")
        roulWin.resizable(False, False)
        roulWin.title("Roulutte")

        Label(roulWin, text="Roulette", font=("arial", 30)).place(x=130, y=30)
        Label(roulWin, text="The roulette has 20 fields, of which \n10 are black and 10 are red. \nFirst you say the color the ball will land on,\nthen you spin the roulette and throw the ball in.\n If you said the correct color, you have won.\n \n Winning prize: $600", font=("arial", 13)).place(x=30, y=100)
        Label(roulWin, text="Choose one color",font=("arial", 13)).place(x=130, y=270)
        Label(roulWin, text=f"Chace to win: {chance_calculator(1,2)}", font=("arial", 13)).place(x=240, y=320)

        labelinfo = Label(roulWin, text="Roulette: Black", font=("arial", 13))
        labelinfo.place(x=140, y=420)

        listbox = Listbox(roulWin, height=2, font=("arial", 13), width=7)
        listbox.place(x=160, y=310)
        listbox.insert(1, "Black")
        listbox.insert(2, "Red")
        listbox.bind("<<ListboxSelect>>", list_selected)

        roulWin.mainloop()
    elif money < 300:
        showinfo(title="Not enough Money", message="You don't have enough money.")
    else:
        showinfo(title="Out of tickets", message="You've run out of tickets.")


def create_menu():
    global rulesButton, accountButton, playBJ, playR, playWOF, money, bankLabel, ticketLabel, tickets, exitButton
    money = 1000
    tickets = 10

    menu["bg"] = "grey"

    accountButton = Button(menu, text="Account", font=(10), width=7, command=account)
    accountButton.place(x=1300, y=20)
    rulesButton = Button(menu, text="Rules", font=(10), width=7, command=rules)
    rulesButton.place(x=1300, y=70)
    exitButton = Button(menu, text="Exit and Save", font=(10),width=13, command=exit_and_save)
    exitButton.place(x=1250, y=700)

    bankLabel = Label(menu, text=f"Bank: $1000", font=("arial", 17))
    bankLabel.place(x=50, y=50)
    ticketLabel = Label(menu, text="Tickets: 10", font=("arial", 17))
    ticketLabel.place(x=200, y=50)

    Label(menu, text="Wheel of fortune", font = ("arial", 20)).place(x=320, y=260)
    Label(menu, text="Entrance costs: $100", font=("airial", 13)).place(x=340, y=300)
    Label(menu, text="Black Jack",font = ("arial", 20)).place(x=670, y=260)
    Label(menu, text="Entrance costs: $200", font=("airial", 13)).place(x=660, y=300)
    Label(menu, text="Roulette", font = ("arial", 20)).place(x=970, y=260)
    Label(menu, text="Entrance costs: $300", font=("airial", 13)).place(x=950, y=300)

    playWOF = Button(menu, text="Play", font=("arial", 15), width=7, command=wheel_of_fortune)
    playWOF.place(x=370, y=350)
    playBJ = Button(menu, text="Play", font=("arial", 15), width=7, command=black_Jack)
    playBJ.place(x=690, y=350)
    playR = Button(menu, text="Play", font=("arial", 15), width=7, command=roulette)
    playR.place(x=980, y=350)


def check_login(nameEntry: str, passwEntry: str):
    if nameEntry.strip() == "" or passwEntry.strip() == "":
        return False

    with open("data.txt", "r") as file:
        data = file.readlines()

    for line in data:
        line = line.strip()
        username, password, _, _ = line.split(" ")
        if nameEntry == username and passwEntry == password:
            return True
    return False


def login():
    global name, UserPassword
    if check_login(usernameEntry.get(), passwordEntry.get()):
        name, UserPassword = usernameEntry.get(), passwordEntry.get()
        remove_widgets(passwordEntry, usernameEntry, loginButton, registerButton, Or, labelPassword, labelUsername, infoLabel)
        menu.geometry("1400x750")
        title.place(x=600, y=40)
        title["font"] = ("arial", 60)
        create_menu()
    else:
        usernameEntry.delete(0, END)
        passwordEntry.delete(0, END)
        infoLabel["text"] = "Username or password not found"
        infoLabel["fg"] = "red"
        infoLabel.place(x=90, y=280)


def check_register(nameEntry: str, passwEntry: str):
    global isFirst, isRegistered, isEqual
    isFirst = False
    isRegistered = False
    isEqual = False
    if " " in nameEntry or " " in passwEntry:
        return False

    if nameEntry == "" or passwEntry == "":
        return False

    if nameEntry == passwEntry:
        isEqual = True
        return False

    with open("data.txt", "r") as file:
        data = file.readlines()
        if data == []:
            isFirst = True
            return True

    for line in data:
        line = line.strip()
        username, _, _, _ = line.split(" ")
        if username == nameEntry:
            isRegistered = True
            return False
    return True


def register():
    global isFirst, isRegistered, isEqual
    if check_register(usernameEntry.get(), passwordEntry.get()):
        with open("data.txt", "a") as file:
            if isFirst:
                file.write(f"{usernameEntry.get()} {passwordEntry.get()} 0 0")
                usernameEntry.delete(0, END)
                passwordEntry.delete(0, END)
                isFirst = False
                infoLabel["text"] = "You are registered"
                infoLabel["fg"] = "green"
                infoLabel.place(x=140, y=280)
            else:
                file.write(f"\n{usernameEntry.get()} {passwordEntry.get()} 0 0")
                usernameEntry.delete(0, END)
                passwordEntry.delete(0, END)
                infoLabel["text"] = "You are registered"
                infoLabel["fg"] = "green"
                infoLabel.place(x=140, y=280)
    else:
        usernameEntry.delete(0, END)
        passwordEntry.delete(0, END)
        if isRegistered:
            infoLabel["text"] = "This Username is already registered"
            infoLabel["fg"] = "red"
            infoLabel.place(x=85, y=280)
        elif isEqual:
                isEqual = False
                infoLabel["text"] = "Username and Password have to be different"
                infoLabel["fg"] = "red"
                infoLabel.place(x=50, y=280)
        else:
            infoLabel["text"] = "Invalid Username or Password"
            infoLabel["fg"] = "red"
            infoLabel.place(x=100, y=280)


def chance_calculator(n: int, total: int):
    return f"{round(n / total, 2) * 100}%"


def pay(n: int):
    global tickets, money
    tickets -= 1
    ticketLabel["text"] = f"Tickets: {tickets}"
    money -= n
    bankLabel["text"] = f"Bank: ${money}"


def close(win, *buttons: Button):
    for button in buttons:
        button["state"] = "active"
    win.destroy()


def switch(virsion: str, *buttons: Button):
    for button in buttons:
        button["state"] = virsion


def remove_widgets(*widgets):
    for widget in widgets:
        widget.destroy()


if __name__ == "__main__":
    main()