import random

import pygame
import pygame.freetype

from Map import Map

MaxBlockSize = 50
MaxWindowHeight = 720
MaxWindowWidth = 1280
COLOR_ALIVE = (228, 186, 186)
COLOR_DEAD = (158, 158, 158)
COLOR_BG = (255, 255, 255)

class UI:
    def __init__(self, _map: Map, _title, _blocksize=100):

        self.isPause = False
        self.CurMap = _map
        self.TextWidth = 160
        temp_size = min((MaxWindowWidth - self.TextWidth) / self.CurMap.width, MaxWindowHeight / self.CurMap.height)
        self.BlockSize = int(min(temp_size, MaxBlockSize))
        self.WindowWidth = self.BlockSize * self.CurMap.width + self.TextWidth
        self.WindowHeight = self.BlockSize * self.CurMap.height
        pygame.init()
        self.screen = pygame.display.set_mode((self.WindowWidth, self.WindowHeight))
        self.screen.fill(COLOR_BG)
        pygame.display.set_caption(_title)
        self.IsPlaying = True
        self._10timesFPS = 16
        self.Clock = pygame.time.Clock()
        self.font = pygame.freetype.SysFont('microsoft Yahei', 15)

    def updateText(self):
        self.screen.fill(COLOR_BG, (self.WindowWidth - self.TextWidth, 0, self.TextWidth, self.WindowHeight))
        pygame.display.flip()
        text_fps = self.font.render('当前FPS: ' + str(self._10timesFPS/10), (25, 25, 25))[0]
        text_key_j = self.font.render('J:减速', (25, 25, 25))[0]
        text_key_k = self.font.render('K:加速', (25, 25, 25))[0]
        text_key_s = self.font.render('S:暂停' if not self.isPause else 'S:运行', (25, 25, 25))[0]
        text_key_d = self.font.render('D:下一帧',(25,25,25))[0]
        text_key_r = self.font.render('R:重新随机生成',(25,25,25))[0]

        textlist = [text_fps, text_key_j, text_key_k, text_key_s,text_key_r]

        if self.isPause:
            textlist.append(text_key_d)

        [self.screen.blit(text, (25 + self.WindowWidth - self.TextWidth, 25 + index * 40)) for index, text in
         enumerate(textlist)]

    def play(self):
        count = 0
        self.updateText()
        while self.IsPlaying:
            # 计数器实现游戏速度调整
            count += 1
            if count >= 512 / self._10timesFPS and not self.isPause:
                count = 0
                self.CurMap.Update()

            for i in range(0, self.CurMap.height):
                for j in range(0, self.CurMap.width):
                    pygame.draw.rect(self.screen,
                                     COLOR_ALIVE if self.CurMap.table[i + 1][j + 1] == 1 else COLOR_DEAD,
                                     (j * self.BlockSize, i * self.BlockSize, self.BlockSize, self.BlockSize),
                                     border_radius = 2)

            self.Clock.tick(51.2)
            pygame.display.update()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.IsPlaying = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j and self._10timesFPS > 1:
                        self._10timesFPS = round(self._10timesFPS / 2)
                    if event.key == pygame.K_k and self._10timesFPS < 512:
                        self._10timesFPS = round(self._10timesFPS * 2)
                    if event.key == pygame.K_s:
                        self.isPause = not self.isPause
                    if event.key == pygame.K_d and self.isPause:
                        self.CurMap.Update()
                    if event.key == pygame.K_r:
                        self.CurMap.reset(0.5)

                    self.updateText()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] <= self.CurMap.width * self.BlockSize \
                            and pos[1] <= self.CurMap.height * self.BlockSize:
                        column = int(pos[0] / self.BlockSize)
                        row = int(pos[1] / self.BlockSize)
                        self.CurMap.flip_cell(row, column)
