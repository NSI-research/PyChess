# -------------------
#
#   Date : 2024-03-12
#   Auteur : Lodjo28
#   Nom du fichier : main
#   Version : 0.2
#
# -------------------

from tkinter import *

Matrice = [[3, 5, 7, 9, 11, 7, 5, 3], 
           [1, 1, 1, 1, 1, 1, 1, 1], 
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [2, 2, 2, 2, 2, 2, 2, 2],
           [4, 6, 8, 10, 12, 8, 6, 4]]


#################
# Le Jeu
#################

for i in Matrice:
    print(i)


Tour = False

def Play(row, colomn, rowD, colomnD, tt):
        # row = int(input("Donnez une ligne : ")) - 1
        # colomn = int(input("Donnez une colonne : ")) - 1

        # rowD = int(input("Donnez une ligne : ")) - 1
        # colomnD = int(input("Donnez une colonne : ")) - 1

    if tt:
        Peut_manger = 0
        Peut_pas_manger = 1
        Pion = 1
        Tours = 3
        Cavalier = 5
        Fou = 7
        Reine = 9
        Roi = 11
    else:
        Peut_manger = 1
        Peut_pas_manger = 0
        Pion = 2
        Tours = 4
        Cavalier = 6
        Fou = 8
        Reine = 10
        Roi = 12
        



        
    if Matrice[row][colomn] == Pion:
        if abs(rowD - row) <= 2 and colomn == colomnD and (row == 6 or row == 1):
            if Matrice[rowD][colomnD] == 0:
                if tt:
                    if Matrice[rowD][colomnD] == 0 and row < rowD:
                        Matrice[rowD][colomnD] = Matrice[row][colomn]
                        Matrice[row][colomn] = 0
                        return True
                else:
                    if Matrice[rowD][colomnD] == 0 and row > rowD:
                        Matrice[rowD][colomnD] = Matrice[row][colomn]
                        Matrice[row][colomn] = 0
                        return True
        elif abs(rowD - row) == 1 and colomn == colomnD:
            if tt:
                if Matrice[rowD][colomnD] == 0 and row < rowD:
                    Matrice[rowD][colomnD] = Matrice[row][colomn]
                    Matrice[row][colomn] = 0
                    return True
            else:
                if Matrice[rowD][colomnD] == 0 and row > rowD:
                    Matrice[rowD][colomnD] = Matrice[row][colomn]
                    Matrice[row][colomn] = 0
                    return True
        elif abs(rowD - row) == 1 and abs(colomn - colomnD) == 1 and (Matrice[rowD][colomnD] % 2 == Peut_manger and Matrice[rowD][colomnD] != 0):
            Matrice[rowD][colomnD] = Matrice[row][colomn]
            Matrice[row][colomn] = 0
            return True
        else:
            return False
    elif Matrice[row][colomn] == Tours:
        if row != rowD and colomn == colomnD:
            ecart = abs(row - rowD)

            Okay = True
            if row > rowD:
                for i in range(ecart):
                    if Matrice[row - (i + 1)][colomn] != 0 and Matrice[row - (i + 1)][colomn] % 2 == Peut_pas_manger:
                        Okay = False
                if Okay:
                    Matrice[rowD][colomnD] = Matrice[row][colomn]
                    Matrice[row][colomn] = 0
                    return True
            elif row < rowD:
                for i in range(ecart):
                    if Matrice[row + (i + 1)][colomn] != 0 and Matrice[row + (i + 1)][colomn] % 2 == Peut_pas_manger:
                        Okay = False
                if Okay:
                    Matrice[rowD][colomnD] = Matrice[row][colomn]
                    Matrice[row][colomn] = 0
                    return True
                        
        elif row == rowD and colomn != colomnD:
            ecart = abs(colomn - colomnD)

            Okay = True
            if colomn > colomnD:
                for i in range(ecart):
                    if Matrice[row][colomn - (i + 1)] != 0 and Matrice[row][colomn - (i + 1)] % 2 == Peut_pas_manger:
                        Okay = False
                if Okay:
                    Matrice[rowD][colomnD] = Matrice[row][colomn]
                    Matrice[row][colomn] = 0
                    return True
            elif colomn < colomnD:
                for i in range(ecart):
                    if Matrice[row][colomn + (i + 1)] != 0 and Matrice[row][colomn + (i + 1)] % 2 == Peut_pas_manger:
                        Okay = False
                if Okay:
                    Matrice[rowD][colomnD] = Matrice[row][colomn]
                    Matrice[row][colomn] = 0
                    return True
        else:
            return False
    elif Matrice[row][colomn] == Cavalier:
            if row != rowD and colomn != colomnD:
                if (rowD == (row + 1) or rowD == (row - 1)) and (colomnD == (colomn + 2) or colomnD == (colomn - 2)) and (Matrice[rowD][colomnD] == 0 or Matrice[rowD][colomnD] % 2 == Peut_manger):
                    Matrice[rowD][colomnD] = Matrice[row][colomn]
                    Matrice[row][colomn] = 0
                    return True

                elif (rowD == (row + 2) or rowD == (row - 2)) and (colomnD == (colomn + 1) or colomnD == (colomn - 1)) and (Matrice[rowD][colomnD] == 0 or Matrice[rowD][colomnD] % 2 == Peut_manger):
                    Matrice[rowD][colomnD] = Matrice[row][colomn]
                    Matrice[row][colomn] = 0
                    return True
            else:
                return False
    elif Matrice[row][colomn] == Fou:
        if row != rowD and colomn != colomnD:
            ecartrow = abs(row - rowD)
            ecartcolomn = abs(colomn - colomnD)

            Okay = True
            if ecartrow == ecartcolomn:
                if row > rowD and colomn > colomnD:
                    for i in range(ecartcolomn):
                        if Matrice[row - (i + 1)][colomn - (i + 1)] != 0 and Matrice[row - (i + 1)][colomn - (i + 1)] % 2 == Peut_pas_manger:
                            Okay = False
                    if Okay:
                        Matrice[rowD][colomnD] = Matrice[row][colomn]
                        Matrice[row][colomn] = 0
                        return True
                elif row < rowD and colomn > colomnD:
                    for i in range(ecartcolomn):
                        if Matrice[row + (i + 1)][colomn - (i + 1)] != 0 and Matrice[row + (i + 1)][colomn - (i + 1)] % 2 == Peut_pas_manger:
                            Okay = False
                    if Okay:
                        Matrice[rowD][colomnD] = Matrice[row][colomn]
                        Matrice[row][colomn] = 0
                        return True
                elif row > rowD and colomn < colomnD:
                    for i in range(ecartcolomn):
                        if Matrice[row - (i + 1)][colomn + (i + 1)] != 0 and Matrice[row - (i + 1)][colomn + (i + 1)] % 2 == Peut_pas_manger:
                            Okay = False
                    if Okay:
                        Matrice[rowD][colomnD] = Matrice[row][colomn]
                        Matrice[row][colomn] = 0
                        return True
                elif row < rowD and colomn < colomnD:
                    for i in range(ecartcolomn):
                        if Matrice[row + (i + 1)][colomn + (i + 1)] != 0 and Matrice[row + (i + 1)][colomn + (i + 1)] % 2 == Peut_pas_manger:
                            Okay = False
                    if Okay:
                        Matrice[rowD][colomnD] = Matrice[row][colomn]
                        Matrice[row][colomn] = 0
                        return True
        else:
            return False

    elif Matrice[row][colomn] == Reine:
        if row != rowD and colomn == colomnD:
            ecart = abs(row - rowD)

            Okay = True
            if row > rowD:
                for i in range(ecart):
                    if Matrice[row - (i + 1)][colomn] != 0 and Matrice[row - (i + 1)][colomn] % 2 == Peut_pas_manger:
                        Okay = False
                if Okay:
                    Matrice[rowD][colomnD] = Matrice[row][colomn]
                    Matrice[row][colomn] = 0
                    return True
            elif row < rowD:
                for i in range(ecart):
                    if Matrice[row + (i + 1)][colomn] != 0 and Matrice[row + (i + 1)][colomn] % 2 == Peut_pas_manger:
                        Okay = False
                if Okay:
                    Matrice[rowD][colomnD] = Matrice[row][colomn]
                    Matrice[row][colomn] = 0
                    return True
                        
        elif row == rowD and colomn != colomnD:
            ecart = abs(colomn - colomnD)

            Okay = True
            if colomn > colomnD:
                for i in range(ecart):
                    if Matrice[row][colomn - (i + 1)] != 0 and Matrice[row][colomn - (i + 1)] % 2 == Peut_pas_manger:
                        Okay = False
                if Okay:
                    Matrice[rowD][colomnD] = Matrice[row][colomn]
                    Matrice[row][colomn] = 0
                    return True
            elif colomn < colomnD:
                for i in range(ecart):
                    if Matrice[row][colomn + (i + 1)] != 0 and Matrice[row][colomn + (i + 1)] % 2 == Peut_pas_manger:
                        Okay = False
                if Okay:
                    Matrice[rowD][colomnD] = Matrice[row][colomn]
                    Matrice[row][colomn] = 0
                    return True

        elif row != rowD and colomn != colomnD:
            ecartrow = abs(row - rowD)
            ecartcolomn = abs(colomn - colomnD)

            Okay = True
            if ecartrow == ecartcolomn:
                if row > rowD and colomn > colomnD:
                    for i in range(ecartcolomn):
                        if Matrice[row - (i + 1)][colomn - (i + 1)] != 0 and Matrice[row - (i + 1)][colomn - (i + 1)] % 2 == Peut_pas_manger:
                            Okay = False
                    if Okay:
                        Matrice[rowD][colomnD] = Matrice[row][colomn]
                        Matrice[row][colomn] = 0
                        return True
                elif row < rowD and colomn > colomnD:
                    for i in range(ecartcolomn):
                        if Matrice[row + (i + 1)][colomn - (i + 1)] != 0 and Matrice[row + (i + 1)][colomn - (i + 1)] % 2 == Peut_pas_manger:
                            Okay = False
                    if Okay:
                        Matrice[rowD][colomnD] = Matrice[row][colomn]
                        Matrice[row][colomn] = 0
                        return True
                elif row > rowD and colomn < colomnD:
                    for i in range(ecartcolomn):
                        if Matrice[row - (i + 1)][colomn + (i + 1)] != 0 and Matrice[row - (i + 1)][colomn + (i + 1)] % 2 == Peut_pas_manger:
                            Okay = False
                    if Okay:
                        Matrice[rowD][colomnD] = Matrice[row][colomn]
                        Matrice[row][colomn] = 0
                        return True
                elif row < rowD and colomn < colomnD:
                    for i in range(ecartcolomn):
                        if Matrice[row + (i + 1)][colomn + (i + 1)] != 0 and Matrice[row + (i + 1)][colomn + (i + 1)] % 2 == Peut_pas_manger:
                            Okay = False
                    if Okay:
                        Matrice[rowD][colomnD] = Matrice[row][colomn]
                        Matrice[row][colomn] = 0
                        return True

    elif Matrice[row][colomn] == Roi:
        ecartrow = abs(row - rowD)
        ecartcolomn = abs(colomn - colomnD)

        if ecartrow <= 1 and ecartcolomn <= 1 and (Matrice[rowD][colomnD] == 0 or Matrice[rowD][colomnD] % 2 == Peut_manger):
            Matrice[rowD][colomnD] = Matrice[row][colomn]
            Matrice[row][colomn] = 0
            return True

    for i in Matrice:
        print(i)

    return False


SwitchG = []
    
root = Tk()
root.geometry("1180x1070")
root.minsize(1180, 1070)
root.maxsize(1180, 1070)
root.title("PragChess")
root.iconbitmap("jeu-dechecs.ico")

piece_images = {
    0: PhotoImage(file='PNG2\\VideIntersideral.png'),
    1: PhotoImage(file='PNG2\\PionNoir.png'),
    2: PhotoImage(file='PNG2\\PionBlanc.png'),
    3: PhotoImage(file='PNG2\\TourNoire.png'),
    4: PhotoImage(file='PNG2\\TourBlanche.png'),
    5: PhotoImage(file='PNG2\\ChevalierNoir.png'),
    6: PhotoImage(file='PNG2\\ChevalierBlanc.png'),
    7: PhotoImage(file='PNG2\\FouNoir.png'),
    8: PhotoImage(file='PNG2\\FouBlanc.png'),
    9: PhotoImage(file='PNG2\\ReineNoire.png'),
    10: PhotoImage(file='PNG2\\ReineBlanche.png'),
    11: PhotoImage(file='PNG2\\RoiNoir.png'),
    12: PhotoImage(file='PNG2\\RoiBlanc.png')
}






def on_button_click(row, col):
    global SwitchG
    global Tour


    print(f"Clic sur la case: {row}, {col}")

    if len(SwitchG) == 0:
        SwitchG.append([row, col])

        Butt = buttons[row][col]

        Butt.config(bg="#F7FF46")


    elif len(SwitchG) == 1:

        Butt = buttons[SwitchG[0][0]][SwitchG[0][1]]

        Butt.config(bg="#DCDCDC")

        if Tour:
            var = Play(SwitchG[0][0], SwitchG[0][1], row, col, True)
            SwitchG = []
            if not var:
                return
        else:
            var = Play(SwitchG[0][0], SwitchG[0][1], row, col, False)
            SwitchG = []
            if not var:
                return

            

        Tour = not Tour
        if Tour:
            Text_variable.set("Tour des noirs")
        else:
            Text_variable.set("Tour des blancs")

        for i in range(8):
            for j in range(8):
                text = Matrice[i][j]
                button = buttons[i][j]
                if text in piece_images:

                    button.config(image=piece_images[text])
                else:
                    button.config(image='', text=' ', compound="center")


buttons = [[None for _ in range(8)] for _ in range(8)]

for i in range(8):
    for j in range(8):
        
        buttons[i][j] = Button(root, text=Matrice[i][j], command=lambda i=i, j=j: on_button_click(i, j), bg="#DCDCDC")
        buttons[i][j].grid(row=i, column=j, sticky=N+E+S+W)


for i in range(8):
    for j in range(8):
        text = Matrice[i][j]
        button = buttons[i][j]
        if text in piece_images:

            button.config(image=piece_images[text])
        else:
            button.config(image='', text=' ', compound="center")

Text_variable = StringVar(root, value="Tour des Blancs")
LabelTour = Label(root, textvariable=Text_variable)
LabelTour.grid(row=0, column=8)

root.mainloop()