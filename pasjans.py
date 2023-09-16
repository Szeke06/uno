import random

#P stand for power of  card if bigger then card is stronger
figury = [
{'P':5,'F': 'ace'},
{'P':4, 'F': 'king'},
{'P':3,'F': 'quen'},
{'P':2,'F': 'jopek'},
{'P':1,'F' :'10'},
{'P':0,'F': '9'}]
colory=['serce','karo','pik','trefl']

kreska='=============================================================================================='

title1='PLAYER ONE CARDS: \n'
title2='PLAYER TWO HAVE CARDS :'
title3='IN PAIL IS :'
cards=[ ]
pail =[ ]


# Preparing  play cards
for color in colory:
    for f in figury:
        c=f.copy()
        c['C']= color
        cards.append(c)

random.shuffle(cards)

player1=[]
player2=[]
playersee=[ ]

while len(cards)>0:
    player1.append(cards.pop())
    player2.append(cards.pop())



nrPail=str(len(pail))
copy_pail=0


# Function display number of play cards of  player 2 and stack of rejected card

def display1 (player2, pail):
    nrP2=str(len(player2))
    nrPail=str(len(pail))
    if len(pail)>0:
        pail.reverse()
        a=pail[0]
        pail.reverse()
        b=a['F']
        c=a['C']
        txt="Top card : %s %s" % (b,c)
    else:
        txt="No cards in Pail"
    print(kreska)
    print(title2.center(100))
    print(nrP2.center(100))
    print('\n')
    print(title3.center(100))
    print(nrPail.center(100),"\n",txt.center(100).upper())
    print('\n')
    print(title1.center(100))
    return

player1cards=player1.copy()


# Function sort and display all cards of player 1 in rows

def display2(player1):
    player1=player1cards.copy()
    z=0
    while len(player1)>0:
        player= player1.copy()
        for card in player:
            if card['P']==z:
                card_copy= card.copy()
                playersee.append(card_copy)
                player1.remove(card)
        z+=1
        if z ==6:
            z = 0

    player1=playersee.copy()      
      
    while len(playersee)>0:
        player=playersee.copy()
        line= []
        line1 =''
        none1=' '
        none='%10s\t' % (none1)
        d=0
        for cd in player:
            if cd['P']==d:
                copy_cd=cd.copy()
                x=copy_cd['F']
                y=copy_cd['C']
                card1= "%5s %5s\t" % ( x,y) #Changing dictionary on string will provide better look of tally
                line.append(card1)
                line1 += card1
                playersee.remove(cd)
                d+= 1
            elif cd['P']<d:
                continue
            
            elif cd['P'] >d:
                brak= cd['P']- d
                for i in range(brak):
                    line.append(none)
                    line1 += none
                copy_cd=cd.copy()
                x=copy_cd['F']
                y=copy_cd['C']
                card1='%5s %5s\t' % (x,y)
                line1 += card1
                line.append(card1)
                playersee.remove(cd)
                d=cd['P']
                d+=1
                
        if len(line)<6:
            brak=6-len(line)
            for i in range(brak):
                    line.append(none)
                    line1 += none
        print(line1)
    return



#Game function wins player who will first get out of his cards

def gra():
    warunek= True
    choose=input('\nchoose POWER of card you whant to place(from 0 to 5 where: 0 is NINE and 5 is ACE):  ')
    while warunek:
            copy_pail= pail.copy()
            if choose =='p': # Player can allways take card from top of rejected cards and add it to his play cards
                if len(copy_pail)==0:
                    choose=input("There's nothing to pull from pail! its empty! choose another option:  ")
                else:
                    pail.reverse()
                    x=pail[0]
                    player1cards.append(x)
                    pail.remove(x)
                    pail.reverse()
                    warunek=False
            elif choose.isdigit() and int(choose) in range(0,6):
                    for card in player1cards:
                        if choose.isdigit() and card['P']== int(choose):
                            pail.reverse()
                            if len(pail) == 0:
                                pail.append(card)
                                player1cards.remove(card)
                                warunek =False
                                break
                            elif len(pail)>0 and pail[0].get('P') <= int(choose):
                                pail.reverse()
                                pail.append(card)
                                player1cards.remove(card)
                                warunek=False
                                break    
                    if len(pail)== len(copy_pail):
                            choose=input('Wrong option try again or press "p" to pull cards rom Pail:')
                    else:
                            warunek=False
                            
            else:
                    choose= input('choose wrong option please try again:')
                    
    pail.reverse()
    if len(pail)>0:
        topCard=pail[0].get('P')
        x=pail[0]
    else:
        topCard=0
    pail.reverse()  
    warunek= True
    while warunek: # Player2( computer) round
            copy_pail= pail.copy()
            for card in player2:
                    if card['P']== topCard:
                            pail.append(card)
                            player2.remove(card)
                            warunek = False
                            break
            if len(pail)>len(copy_pail):
                    warunek = False
            elif len(pail)==len(copy_pail):
                    for card in player2:
                            if card['P']>topCard:
                                    pail.append(card)
                                    player2.remove(card)
                                    warunek=False
                                    break
                    if len(pail)==len(copy_pail):
                        if len(pail)>1:
                            player2.append(x)
                            pail.remove(x)
                            warunek=False
                        else:
                            warunek=False


while len(player1)>0 or len(player2)>0:  #final loop to sortout who will win :)                           
    display1 (player2, pail)
    display2(player1)
    gra()
    player1=player1cards.copy()
    if len(player1)==0:
        print("\nEND GAME ! PLAYER 1 WINS !!!".center(100))
        break
    elif len(player2)==0:
        print("\nEND GAME! PALYER 2 WINS !!!".center(100))
        break
        



