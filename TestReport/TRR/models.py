#coding=utf-8 

from django.db import models
from django.contrib import admin

# 创建登陆用户表
class User(models.Model):
    name = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = 'user'
    def __str__(self):
        return self.name
############################################################################
#创建电池续航测试所需表。Battery Life（BL）
class BL_item(models.Model):
    Game = models.CharField(max_length=10, verbose_name="游戏")
    Music = models.CharField(max_length=10, verbose_name="音乐")
    PlayVideo = models.CharField(max_length=80, verbose_name="播放视频")
    ReadBook = models.CharField(max_length=80, verbose_name="读书")
    WeiBO = models.CharField(max_length=80, verbose_name="微博")
    CallMO = models.CharField(max_length=80, verbose_name="电话呼出")
    Brower = models.CharField(max_length=80, verbose_name="浏览器")
    Camera = models.CharField(max_length=80, verbose_name="相机")
    Remain = models.CharField(max_length=80, verbose_name="剩余")
    Timestamp = models.DateTimeField()
        
    class Meta:
        db_table = 'BL_item' #给表命名为应用名+类名（TRR_BL_item），改为BL_item
        abstract = True
    

class BL_mi2s(BL_item):
    Version = models.CharField(max_length=20, verbose_name="版本", primary_key=True)
    
    class Meta:
        db_table = 'BL_mi2s'
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version

class BL_mi2a(BL_item):
    Version = models.CharField(max_length=20, verbose_name="版本", primary_key=True)
    
    class Meta:
        db_table = 'BL_mi2a'
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version
    
class BL_mi3w(BL_item):
    Version = models.CharField(max_length=20, verbose_name="版本", primary_key=True)
    
    class Meta:
        db_table = 'BL_mi3w'
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version

class BL_mi3td(BL_item):
    Version = models.CharField(max_length=20, verbose_name="版本", primary_key=True)
    
    class Meta:
        db_table = 'BL_mi3td'
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version
############################################################################
#创建电流测试表
class Current_item(models.Model):
    Item1 = models.CharField(max_length=80, verbose_name="2G关屏插耳机打电话5分钟")
    Item2 = models.CharField(max_length=80, verbose_name="3G关屏插耳机打电话5分钟")
    Item3 = models.CharField(max_length=80, verbose_name="飞行模式待机亮屏40分钟")
    Item4 = models.CharField(max_length=80, verbose_name="3G网络关屏待机40分钟")
    Item5 = models.CharField(max_length=80, verbose_name="无SIM卡关屏待机10分钟")
    Item6 = models.CharField(max_length=80, verbose_name="飞行模式关屏待机30分钟")
    Item7 = models.CharField(max_length=80, verbose_name="关屏飞行模式打开WLAN不连接网络30分钟")
    Item8 = models.CharField(max_length=80, verbose_name="关屏飞行模式打开WLAN连接2.4G网络30分钟")
    Item9 = models.CharField(max_length=80, verbose_name="关屏飞行模式打开WLAN连接5G网络30分钟")
    Item10 = models.CharField(max_length=80, verbose_name="关屏飞行模式打开BT不连接设备30分钟")
    Item11 = models.CharField(max_length=80, verbose_name="关屏飞行模式打开BT连接设备30分钟")
    Item12 = models.CharField(max_length=80, verbose_name="飞行模式播放本地视频")
    Item13 = models.CharField(max_length=80, verbose_name="飞行模式玩游戏（切水果或者其它）5分钟")
    Item14 = models.CharField(max_length=80, verbose_name="飞行模式滑动主屏10分钟")
    Item15 = models.CharField(max_length=80, verbose_name="飞行模式滑动联系人10分钟")
    Item16 = models.CharField(max_length=80, verbose_name="飞行模式连接wifi滑动浏览器10分钟")
    Item17 = models.CharField(max_length=80, verbose_name="飞行模式开启防抖录制视频5分钟")
    Item18 = models.CharField(max_length=80, verbose_name="飞行模式关闭防抖录制视频5分钟")
    Item19 = models.CharField(max_length=80, verbose_name="飞行模式播放视频5分钟")
    Item20 = models.CharField(max_length=80, verbose_name="关屏插耳机飞行模式播放音乐10分钟")
    Item21 = models.CharField(max_length=80, verbose_name="关屏飞行模式录音10分钟")
    Timestamp = models.DateTimeField()
        
    class Meta:
        db_table = 'Current_item' #给表命名为应用名+类名（TRR_BL_item），改为BL_item
        abstract = True


class Current_mi2s(Current_item):
    Version = models.CharField(max_length=20, verbose_name="版本", primary_key=True)
    
    class Meta:
        db_table = 'Current_mi2s'
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version

class Current_mi2a(Current_item):
    Version = models.CharField(max_length=20, verbose_name="版本", primary_key=True)
    
    class Meta:
        db_table = 'Current_mi2a'
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version
    
class Current_mi3w(Current_item):
    Version = models.CharField(max_length=20, verbose_name="版本", primary_key=True)
    
    class Meta:
        db_table = 'Current_mi3w'
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version
    
class Current_mi3td(Current_item):
    Version = models.CharField(max_length=20, verbose_name="版本", primary_key=True)
    
    class Meta:
        db_table = 'Current_mi3td'
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version