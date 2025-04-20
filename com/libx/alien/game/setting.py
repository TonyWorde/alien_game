
class Setting:
    """
    存储“外星人入侵游戏”的所有设置的类
    """
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (169,169,169)
        self.ship_speed = 1
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,0,0)
        """一个屏幕上子弹的数量"""
        self.bullet_num = 10
        """外星人移动的速度"""
        self.alien_speed = 1
        """外星人到达屏幕边缘后下移的速度"""
        self.fleet_drop_speed = 10
        """外星人移动方向，正代表右移，负代表左移"""
        self.fleet_direction = 1