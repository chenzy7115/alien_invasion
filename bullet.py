import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()  # 继承Sprite类的属性和方法
        self.screen = ai_game.screen  # 屏幕对象
        self.settings = ai_game.settings  # 设置对象
        self.color = self.settings.bullet_color  # 子弹颜色

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)  # 创建子弹矩形对象
        self.rect.midtop = ai_game.ship.rect.midtop  # 设置子弹的位置,这里是飞船的顶部中心

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)  # 存储子弹的y坐标,这里是小数

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed  # 更新子弹的y坐标,向上移动
        # Update the rect position.
        self.rect.y = self.y  # 更新子弹的矩形位置

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)  # 绘制子弹矩形对象到屏幕上,颜色为self.color   
        