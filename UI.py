import pygame

from Map import Map


class UI:
    def __init__(self,_map:Map,_title,_blocksize = 100):
        self.BlockSize = _blocksize
        self.WindowHeight = _blocksize * _map.Height
        self.WindowWidth = _blocksize * _map.Width
        self.CurMap = _map
        pygame.init()
        self.screen = pygame.display.set_mode((self.WindowWidth,self.WindowHeight))
        pygame.display.set_caption(_title)
        self.IsPlaying = True
        self.FPS = 1
        self.Clock = pygame.time.Clock()

    def play(self):
        while self.IsPlaying:
            for i in range(0,self.CurMap.Height):
                for j in range(0,self.CurMap.Width):
                    pygame.draw.rect(self.screen,(255,255,255) if self.CurMap.table[i+1][j+1] == 1 else (0,0,0),
                                 (j*self.BlockSize,i*self.BlockSize,self.BlockSize,self.BlockSize))
            self.CurMap.Update()
            self.Clock.tick(self.FPS)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.IsPlaying = False

map = Map([
    [0,0,0,0,0],
    [1,1,1,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [0,0,0,1,0],
    [0,0,0,1,0]
    ],6,5)
Test = UI(map,"TEST")
Test.play()