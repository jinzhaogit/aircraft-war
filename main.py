#-*- coding:utf-8 -*-

#引入包使用其方法开发
import pygame
#引入包里面的键盘事件检测
from pygame.locals import *
#引入时间做sleep睡眠进行数据节流
import time

#通过面向对象创建类
class HeroPlane(object):
    #初始化英雄飞机函数
    def __init__(self,screen_temp):
        #定义自己的英雄飞机图片运动坐标
        self.x=200
        self.y=500
        #接收定义的画布
        self.screen=screen_temp
        #创建一个自己的英雄飞机图片
        self.image=pygame.image.load('./feiji/hero1.png')
        #存储发射出去的子弹对象引用
        self.bullet_list=[] 
    #利用画笔把英雄飞机画出来
    def display(self):
        #显示飞机
        self.screen.blit(self.image,(self.x,self.y))
        #飞机发射子弹
        for bullet in self.bullet_list:
            bullet.display()
            #让子弹向上移动
            bullet.move()
    #英雄飞机左移动
    def move_left(self):
        self.x -=5
    #英雄飞机右移动
    def move_right(self):
        self.x +=5
    #英雄飞机发射子弹
    def fire(self):
        #将创建的子弹添加列表中
        self.bullet_list.append(Bullet(self.screen,self.x,self.y)) 

class Bullet(object):
    #初始化英雄飞机子弹
    def __init__(self,screen_temp,x,y):
        #定义自己的英雄飞机子弹图片运动坐标
        self.x=x+40
        self.y=y-20
        #接收定义的画布
        self.screen=screen_temp
        #创建一个自己的英雄飞机图片
        self.image=pygame.image.load('./feiji/bullet.png')
    #利用画笔把英雄飞机子弹画出来
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    #让子弹位置向上移动
    def move(self):
        self.y-=12
#定义一个键盘检测事件函数
def key_control(hero_temp):
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
                hero_temp.move_left()
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()

#定义主函数进行执行
def main():
    #创建一个窗口(画布)
    screen=pygame.display.set_mode((488,640))
    #创建一个背景图片
    background=pygame.image.load('./feiji/background.png')
    #利用类创建一个自己的英雄飞机
    hero=HeroPlane(screen)

    #通过不听循环执行让页面存在
    while True:
        #将背景图片传输到屏幕上(画笔)
        screen.blit(background,(0,0))
        #将自己的英雄飞机图片传输到屏幕上
        hero.display()
        #更新屏幕的部分用于显示
        pygame.display.update()
        #获取事件，比如按键
        key_control(hero)
        #延迟更新，沉睡一会，减少CPU压力
        time.sleep(0.2)

# 执行函数
if __name__ == "__main__":
    main()