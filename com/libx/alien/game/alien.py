import pygame.image
from pygame.sprite import Sprite


class Alien(Sprite):
    """外星人类"""

    def __init__(self, ai_game):
        """初始化"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.image = pygame.image.load('../resources/外星人.jpg')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        """把外星人的位置设置为图片的宽度和高度，处于左上角"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """判断外星人是否到达屏幕边缘"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right > screen_rect.right) or (self.rect.left < 0)

    def update(self):
        """移动外星人，左移或者右移"""
        self.x += self.setting.fleet_direction * self.setting.alien_speed
        self.rect.x = self.x
