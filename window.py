#-*- coding:utf-8 -*-

#引入包使用其方法开发
import pygame
#引入包里面的键盘事件检测
from pygame.locals import *
#引入时间做sleep睡眠进行数据节流
import time

#定义主函数进行执行
def main():
    #创建一个窗口(画布)
    screen=pygame.display.set_mode((488,640))
    #创建一个背景图片
    background=pygame.image.load('./feiji/background.png')
    #创建一个自己的英雄飞机图片
    hero=pygame.image.load('./feiji/hero1.png')
    #定义自己的英雄飞机图片运动坐标
    x=200
    y=500

    #通过不听循环执行让页面存在
    while True:
        #将背景图片传输到屏幕上(画笔)
        screen.blit(background,(0,0))
        #将自己的英雄飞机图片传输到屏幕上
        screen.blit(hero,(x,y))
        #更新屏幕的部分用于显示
        pygame.display.update()
        
        #获取事件，比如按键等，收集之前按下的所有操作循环执行，控制自己的英雄飞机图片左右移动
        for event in pygame.event.get():
            #判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            #判断是否是按下了键
            elif event.type == KEYDOWN:
                #检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    x-=5
                #检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    x+=5
                #检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')

        #延迟更新，沉睡一会，减少CPU压力
        time.sleep(0.1)

# 执行函数
if __name__ == "__main__":
    main()