import random

import pygame
import pygame.freetype

from Map import Map

WIDTH = 800
HEIGHT = 600
COLOR_ALIVE = (228, 186, 186)
COLOR_DEAD = (158, 158, 158)
COLOR_BG = (255, 255, 255)


class UI:
    def __init__(self, _map: Map, _title, _blocksize=100):
        self.BlockSize = HEIGHT / _map.Height
        self.WindowHeight = HEIGHT
        self.WindowWidth = WIDTH
        self.CurMap = _map
        pygame.init()
        self.screen = pygame.display.set_mode((self.WindowWidth, self.WindowHeight))
        self.screen.fill(COLOR_BG)
        pygame.display.set_caption(_title)
        self.IsPlaying = True
        self.FPS = 1
        self.Clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('microsoft Yahei', 15)
        self.font = pygame.freetype.SysFont('microsoft Yahei', 15)

    def updateText(self):
        self.screen.fill(COLOR_BG, (HEIGHT, 0, WIDTH - HEIGHT, HEIGHT))
        pygame.display.flip()
        text_fps, __ = self.font.render('当前FPS: ' + str(self.FPS), (25, 25, 25))
        text_help, __ = self.font.render('j:减速, k:加速, s:暂停', (25, 25, 25))
        [self.screen.blit(text, (25 + HEIGHT, 25 + index * 40)) for (index, text) in
         enumerate([text_fps, text_help])]

    def play(self):
        count = 0
        pause_flg = False
        self.updateText()
        while self.IsPlaying:
            # 计数器实现游戏速度调整
            count += 1
            if count >= 120 / self.FPS and not pause_flg:
                count = 0
                self.CurMap.Update()
            for i in range(0, self.CurMap.Height):
                for j in range(0, self.CurMap.Width):
                    pygame.draw.rect(self.screen,
                                     COLOR_ALIVE if self.CurMap.table[i + 1][j + 1] == 1 else COLOR_DEAD,
                                     (j * self.BlockSize, i * self.BlockSize, self.BlockSize, self.BlockSize),
                                     border_radius=2)

            self.Clock.tick(120)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.IsPlaying = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:
                        if 0.3 < self.FPS <= 2:
                            self.FPS = round(self.FPS - 0.2, 2)
                        elif self.FPS > 2:
                            self.FPS = round(self.FPS - 1, 2)
                    if event.key == pygame.K_k:
                        if 0.2 <= self.FPS < 2:
                            self.FPS = round(self.FPS + 0.2, 2)
                        elif 2 <= self.FPS < 120:
                            self.FPS = round(self.FPS + 1, 2)
                    self.updateText()
                    if event.key == pygame.K_s:
                        pause_flg = not pause_flg
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] <= 600:
                        column = int(pos[0] / self.BlockSize)
                        row = int(pos[1] / self.BlockSize)
                        self.CurMap.flip_cell(row, column)


game_map = Map([[random.choice([0, 1]) for i in range(30)] for j in range(30)])
GameUI = UI(game_map, "Game Of Life")
GameUI.play()
