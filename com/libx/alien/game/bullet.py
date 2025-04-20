import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """子弹类"""
    def __init__(self, ai_game):
        """初始化子弹"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.setting
        """先在原点初始化子弹位置，这是在pygame上绘制一个游戏元素，可以理解为改变原来位置的元素颜色，和飞船图片是不同的"""
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        self.color = self.setting.bullet_color
        """再把子弹设置从飞船顶部开始"""
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """更新子弹位置"""
        self.y -= self.setting.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)