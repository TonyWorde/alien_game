import pygame
"""
rect方法是获取矩形元素的方法
pygame之所以会高效是因为它将游戏元素分为每个rect对象(矩形元素)，矩形简单容易操作，哪怕有时候它们的形状并非矩形
操作游戏元素实际上就是在操作矩形元素

在pygame中，原点(0,0)是在左上角，元素往右下角移动时，x值和y值会变大，即；
________ x
|
|
y
blit方法是pygame绘制方法
操作rect对象时，可以使用矩形的四个角和中心的x、y轴坐标来控制矩形位置，或者使用特定方法
居中：center、centerx、centery，后两个时居中wy居中
与屏幕边缘的各种对齐：left、right、bottom、top
结合，例如底部居中midbottom、右居中midright、左居中midleft、顶部居中midtop

"""
class Ship:
    """
    外星飞船类
    """
    def __init__(self, ai_game):
        """初始化游戏窗口整体并获取位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        """初始化飞船图片并获取矩形"""
        self.image = pygame.image.load('../resources/外星飞船.jpg')
        self.rect = self.image.get_rect()

        """设置飞船在游戏窗口的位置"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.setting = ai_game.setting
        self.x = float(self.rect.x)
        # self.y = float(self.rect.y)

        """设置飞船上下左右移动的标志"""
        self.left_move = False
        self.right_move = False
        # self.up_move = False
        # self.down_move = False

    def update(self):
        """判断，不让飞船飞出游戏窗口"""
        if self.left_move and self.rect.left > self.screen_rect.left:
            self.x -= self.setting.ship_speed
        if self.right_move and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        # if self.up_move and self.rect.top > self.screen_rect.top:
        #     self.y -= self.setting.ship_speed
        # if self.down_move and self.rect.bottom < self.screen_rect.bottom:
        #     self.y += self.setting.ship_speed
        self.rect.x = self.x
        # self.rect.y = self.y

    def resize(self, width, height):
        """控制飞船图片大小"""
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(midbottom = self.rect.midbottom)

    def blitem(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
