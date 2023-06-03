import random
from Map import Map
from UI import UI

game_map = Map([[random.choice([0, 1]) for i in range(30)] for j in range(30)])
GameUI = UI(game_map, "Game Of Life")
GameUI.play()
