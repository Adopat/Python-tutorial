# 利用Pygame 实现贪吃蛇
# -*- coding: utf-8 -*-
import pygame
import random
caption_width = 500 # 画布宽度
caption_heigth = 500 # 画布高度
white_color = (255,255,255) # 白色蛇
black_color = (0,0,0)
game_title = "贪吃蛇"
cell = 10
snake_init_pos = [[250,250],[240,250],[230,250],[220,250]] # 蛇的初始位置
food_pos = [random.randrange(1,50)*10,random.randrange(1,50)*10] # 食物初始随机位置
head_pos = [250,250] # 定义蛇头的位置
#初始化
pygame.init()
# 关闭刷新
clock = pygame.time.Clock()
# 设置窗口大小
caption = pygame.display.set_mode((caption_width,caption_heigth))
# 设置窗口标题
pygame.display.set_caption(game_title)
# while True:
#     # 初始化
#     pygame.init()
#     # 关闭刷新
#     clock = pygame.time.Clock()
#     # 设置窗口大小
#     caption = pygame.display.set_mode((caption_width,caption_heigth))
#     # 设置窗口标题
#     pygame.display.set_caption(game_title)
#     white = (255,255,255)
#     pygame.draw.rect(caption,white,pygame.Rect(250,250,10,10))
#     pygame.draw.rect(caption,white,pygame.Rect(240,250,10,10))
#     pygame.draw.rect(caption,white,pygame.Rect(230,250,10,10))
#     pygame.draw.rect(caption,white,pygame.Rect(220,250,10,10))
#     pygame.display.update()
#pygame.Rect(left,top,width,heigth)
def draw_rect(color,position):
    pygame.draw.rect(caption,color,pygame.Rect(position[0],position[1],cell,cell))
def hit_the_self():
    if snake_init_pos[0] in snake_init_pos[1:]:
        return True
    else:
        return False
def hit_the_wall(head_pos):
    if head_pos[0]>=caption_width or head_pos[0]<0 or head_pos[1]>=caption_heigth or head_pos[1]<0:
        return True
    else:
        return False
def change_direction(head_pos):
    global food_pos
    snake_init_pos.insert(0,list(head_pos))
    if head_pos != food_pos:
        snake_init_pos.pop()
    else:
        food_pos = [random.randrange(1,50)*10,random.randrange(1,50)*10]
    if hit_the_self() or hit_the_wall(head_pos):
        pygame.quit()
def main():
    for pos in snake_init_pos:
        draw_rect(white_color,pos)
    draw_rect(white_color,food_pos)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    head_pos[0] -= cell
                    change_direction(head_pos)
                elif event.key == pygame.K_RIGHT:
                    head_pos[0] +=cell
                    change_direction(head_pos)
                elif event.key == pygame.K_UP:
                    head_pos[1] -=cell
                    change_direction(head_pos)
                elif event.key == pygame.K_DOWN:
                    head_pos[1] +=cell
                    change_direction(head_pos)
        caption.fill(black_color)
        draw_rect(white_color,food_pos)
        for pos in snake_init_pos:
            draw_rect(white_color,pos)
        pygame.display.update()
        clock.tick(10)
if __name__ =='__main__':
    main()



