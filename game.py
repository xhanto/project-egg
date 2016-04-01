from __future__ import print_function
from map import Map
from square import Square
from player import Player
import random as rd

class Game(object):

    def __init__(self,n_players,m_size):
        self.map = Map(m_size)
        self.start_pts = []
        self.players = []
        for i in range(n_players):
            posx = rd.randint(1,m_size-2)
            posy = rd.randint(1,m_size-2)
            while [posx,posy] in self.start_pts:
                posx = rd.randint(1,m_size-2)
                posy = rd.randint(1,m_size-2)
            self.start_pts.append([posx,posy])
            player = Player(i+1,[posx,posy])
            self.players.append(player)
            self.map.grid[posx][posy] = player

    def display_grid(self):
        for i in self.map.grid:
            for j in i:
                print(j,end="")
            print("")
