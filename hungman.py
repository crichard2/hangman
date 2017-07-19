#Hungman!

def hangman():
    lista = ["manzana","paralelepipedo","zopenco","tangananica","tanganana","oso"]
    import random
    word = lista[random.randint(0,5)]
    wrong = 0
    stages = ["",
              "________          ",
              "|       |         ",
              "|       |         ",
              "|       0         ",
              "|      /|\        ",
              "|      / \        ",
              "|                 "
              ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print ("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] =  char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(("").join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
              print("You win! It was {}".format(word))
              print("".join(board).upper()+"!!!!!")
              win = True
              break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}".format(word))
        
hangman()

              
