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


grid = np.zeros([3,3])
datajoueurs = {"0":{"value":"4","sym":"o","color":"lightblue"},"1":{"value":"1","sym":"x","color":"red"}}
rang = [0,1,2]
g=globals()
player=np.random.randint(0,2)
tour=0
TITLE="Joueur qui commence: "+ datajoueurs[str(player)]["sym"]

def is_won():
    global res
    d1=np.sum(grid.diagonal())
    d2=np.sum(np.fliplr(grid).diagonal())
    res=[d1,d2]
    for i in rang:
        g[f"l{i}"]=np.sum(grid[i])
        g[f"c{i}"]=np.sum(grid.T[i])
        res.append(g[f"l{i}"])
        res.append(g[f"c{i}"])

   
    if len([i for i in res if i==12])!=0:
        winner=0
        return True, winner
    elif len([i for i in res if i==3])!=0:
        winner=1
        return True, winner
    else:
        return False
    
def draw():
    screen.draw.line((WIDTH/3,0),(WIDTH/3,HEIGHT),"white")
    screen.draw.line((2*WIDTH/3,0),(2*WIDTH/3,HEIGHT),"white")
    screen.draw.line((0,HEIGHT/3),(WIDTH,HEIGHT/3),"white")
    screen.draw.line((0,2*HEIGHT/3),(WIDTH,2*HEIGHT/3),"white")


def on_mouse_down(pos):
    global grid
    global tour
    global player
    position=[pos[0],pos[1]]
    posgrid=[int(np.floor(position[i]/300)) for i in [1,0]]

    if grid[posgrid[0]][posgrid[1]]==0:
        tour+=1
        grid[posgrid[0]][posgrid[1]]=datajoueurs[str(player)]["value"]
        screen.draw.text(datajoueurs[str(player)]["sym"],center=(posgrid[1]*300+150,posgrid[0]*300+150),color=datajoueurs[str(player)]["color"],fontsize=300)
        player^=1
        if is_won():
            if eg.boolbox(msg=f"Victoire du joueur {is_won()[1]+1} ({datajoueurs[str(is_won()[1])]['sym']}) \n Rejouer ?",choices=["Oui","Non"]):
                screen.clear()
                grid=np.zeros([3,3])
                tour=0
            else:
                sys.exit()
        elif not(is_won()) and tour==9:
            if eg.boolbox(msg="Égalité ! \n Rejouer ?",choices=["Oui","Non"]):
                screen.clear()
                grid=np.zeros([3,3])
                tour=0
            else:
                sys.exit()
    
