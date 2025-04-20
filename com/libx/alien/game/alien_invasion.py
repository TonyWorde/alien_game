import sys
import pygame
from setting import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """ 管理游戏资源与行为的类 """
    def __init__(self):
        """ 初始化游戏并创建游戏资源 """
        pygame.init()
        # 初始化时钟属性，使用pygame获取Clock类
        self.clock = pygame.time.Clock()
        self.setting = Setting()
        # 初始化窗口属性，使用pygame提供的方法绘制显示窗口的宽度和高度
        self.screen = pygame.display.set_mode((
            self.setting.screen_width, self.setting.screen_height
        ))
        # 使用pygame提供的方法设置窗口标题
        pygame.display.set_caption("外星人入侵")
        # 获取飞船
        self.ship = Ship(self)
        self.ship.resize(50, 50)
        """Group是sprite的功能，类似一个数组，用于额外功能开发"""
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """ 开始游戏的主循环 """
        while True:
            self._check_events()
            self.ship.update()
            """更新子弹"""
            self._update_bullets()
            """更新外星人"""
            self._update_alien()
            self._update_screen()
            #在循环里面设置帧率
            self.clock.tick(30)

    def _check_events(self):
        # 侦听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_down_event(event)
            elif event.type == pygame.KEYUP:
                self._check_up_event(event)

    def _check_down_event(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.down_move = True
        elif event.key == pygame.K_UP:
            self.ship.up_move = True
        elif event.key == pygame.K_LEFT:
            self.ship.left_move = True
        elif event.key == pygame.K_RIGHT:
            self.ship.right_move = True
        elif event.key == pygame.K_SPACE:
            """空格，创建一个新的子弹并且加入group数组"""
            if len(self.bullets) < self.setting.bullet_num:
                self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_up_event(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.down_move = False
        elif event.key == pygame.K_UP:
            self.ship.up_move = False
        elif event.key == pygame.K_LEFT:
            self.ship.left_move = False
        elif event.key == pygame.K_RIGHT:
            self.ship.right_move = False
    def _update_screen(self):
        # 重绘窗口背景颜色
        self.screen.fill(self.setting.bg_color)
        """绘制飞船"""
        self.ship.blitem()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        """绘制外星人"""
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _fire_bullet(self):
        """开火，绘制一枚新的子弹"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹"""
        self.bullets.update()
        """
        防止group数组里面的bullet过多而导致内存溢出，在此处要做删除，
        但是由于不允许在循环中删除数组，所以用一个副本做判断，再删除正本
        """
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """创建外星人舰队"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        """让每个外星人间隔一个外星人宽度，直到超出窗口，再换下一行"""
        while current_y < (self.setting.screen_height - 15 * alien_height):
            while current_x < (self.setting.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            """重置x，并且加y"""
            current_x = alien_width
            current_y += 3 * alien_height

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = new_alien.x
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_alien(self):
        """检查外星人是否到达屏幕边缘，若是，则改变"""
        self._check_fleet_edges()
        """更新外星人位置"""
        self.aliens.update()

    def _check_fleet_edges(self):
        """判断外星人是否到达屏幕边缘"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """让机器人下移并改变它们的左右移动方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1

if __name__ == '__main__':
    # 创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()