# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 17:55:25 2020

@author: William
"""

import numpy as np
import pgzrun
import easygui as eg
import sys

WIDTH = 900
HEIGHT = 900


grid = np.zeros([3,3]) #initialize with an empty grid
datajoueurs = {"0":{"value":"4","sym":"o","color":"lightblue"},
               "1":{"value":"1","sym":"x","color":"red"}} # x value is 1, o value is 4 !!
rang = [0,1,2]
g=globals()
player=np.random.randint(0,2) #starting player = random
tour=0
TITLE="Joueur qui commence: "+ datajoueurs[str(player)]["sym"]
mirror = lambda x: (HEIGHT/3)*x + (HEIGHT/6)

def is_won(): #check the sum of every row/column/diagonal of the matrix
    global res
    d1=np.sum(grid.diagonal())
    d2=np.sum(np.fliplr(grid).diagonal())
    res=[d1,d2]
    for i in rang: 
        g[f"l{i}"]=np.sum(grid[i])
        g[f"c{i}"]=np.sum(grid.T[i])
        res.append(g[f"l{i}"])
        res.append(g[f"c{i}"])

   
    if len([i for i in res if i==12]): #filter the results and look for the value 12 (3*4). If this list is not empty, declare a win for player 0
        winner=0
        return True, winner
    elif len([i for i in res if i==3]): #same but for the value 3 (3*1)
        winner=1
        return True, winner
    else:
        return False
    
def draw(): #draw the game grid
    screen.draw.line((WIDTH/3,0),(WIDTH/3,HEIGHT),"white")
    screen.draw.line((2*WIDTH/3,0),(2*WIDTH/3,HEIGHT),"white")
    screen.draw.line((0,HEIGHT/3),(WIDTH,HEIGHT/3),"white")
    screen.draw.line((0,2*HEIGHT/3),(WIDTH,2*HEIGHT/3),"white")


def on_mouse_down(pos):
    global grid
    global tour
    global player
    position=[pos[0],pos[1]] #translate the tuple "pos" to a list
    posgrid=[int(np.floor(position[i]/300)) for i in [1,0]] #mirror the click's coords to the equivalent position in the matrix

    if grid[posgrid[0]][posgrid[1]]==0: #cannot click if the spot is already taken
        tour+=1
        grid[posgrid[0]][posgrid[1]]=datajoueurs[str(player)]["value"] #add the corresponding value of the click (1 or 4) to the matrix
        screen.draw.text(datajoueurs[str(player)]["sym"],center=(mirror(posgrid[1]),mirror(posgrid[0])),color=datajoueurs[str(player)]["color"],fontsize=300) #draw the player's symbol in the middle of its square no matter where he clicked
        player^=1 #switch players
        if is_won(): #check for a win
            if eg.boolbox(msg=f"Victoire du joueur {is_won()[1]+1} ({datajoueurs[str(is_won()[1])]['sym']}) \n Rejouer ?",choices=["Oui","Non"]):
                screen.clear() #reset the game
                grid=np.zeros([3,3])
                tour=0
            else:
                sys.exit() 
        elif not(is_won()) and tour==9: # if there are no winners and all 9 squares have been filled, declare a tie
            if eg.boolbox(msg="Égalité ! \n Rejouer ?",choices=["Oui","Non"]): 
                screen.clear() #reset the game
                grid=np.zeros([3,3])
                tour=0
            else:
                sys.exit()
    
pgzrun.go()
