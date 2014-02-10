#coding=utf-8 

from django.db import models
from django.contrib import admin

# 创建登陆用户表
'''class User(models.Model):
    name = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = 'user'
    def __str__(self):
        return self.name'''
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
        verbose_name="功耗测试MI2s"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version

class BL_mi2a(BL_item):
    Version = models.CharField(max_length=20, verbose_name="版本", primary_key=True)
    
    class Meta:
        db_table = 'BL_mi2a'
        verbose_name="功耗测试MI2a"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version
    
class BL_mi3w(BL_item):
    Version = models.CharField(max_length=20, verbose_name="版本", primary_key=True)
    
    class Meta:
        db_table = 'BL_mi3w'
        verbose_name="功耗测试MI3w"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version

class BL_mi3td(BL_item):
    Version = models.CharField(max_length=20, verbose_name="版本", primary_key=True)
    
    class Meta:
        db_table = 'BL_mi3td'
        verbose_name="功耗测试MI3td"
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
        verbose_name="电流测试MI2s"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version

class Current_mi2a(Current_item):
    Version = models.CharField(max_length=20, verbose_name="版本", primary_key=True)
    
    class Meta:
        db_table = 'Current_mi2a'
        verbose_name="电流测试MI2a"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version
    
class Current_mi3w(Current_item):
    Version = models.CharField(max_length=20, verbose_name="版本", primary_key=True)
    
    class Meta:
        db_table = 'Current_mi3w'
        verbose_name="电流测试MI3w"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version
    
class Current_mi3td(Current_item):
    Version = models.CharField(max_length=20, verbose_name="版本", primary_key=True)
    
    class Meta:
        db_table = 'Current_mi3td'
        verbose_name="电流测试MI3td"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Version
    
############################################################################
#创建Critical Issue
class critical_issue(models.Model):
    BugID = models.CharField(max_length=10, verbose_name="JiraID")
    Title = models.CharField(max_length=50, verbose_name="描述")
    priority = models.CharField(max_length=10, verbose_name="优先级")
    status = models.CharField(max_length=10, verbose_name="状态")
    openversion =  models.CharField(max_length=10, verbose_name="发现版本")
    fixversion = models.CharField(max_length=10, verbose_name="关闭版本")
    link = models.CharField(max_length=50, verbose_name="链接")
    Timestamp = models.DateTimeField()
    
    class Meta:
        db_table = 'critical_issue' #给表命名为应用名+类名（TRR_critical_issue），改为critical_issue
        abstract = True
    
class CI_mi2s(critical_issue):
    class Meta:
        db_table = 'CI_mi2s'
        verbose_name="问题列表MI2s"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Title
    
class CI_mi2a(critical_issue):
    class Meta:
        db_table = 'CI_mi2a'
        verbose_name="问题列表MI2a"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Title
    
class CI_mi3w(critical_issue):
    class Meta:
        db_table = 'CI_mi3w'
        verbose_name="问题列表MI3w"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Title

class CI_mi3td(critical_issue):
    class Meta:
        db_table = 'CI_mi3td'
        verbose_name="问题列表MI3td"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Title

############################################################################
#camera cts
class camera_cts(models.Model):
    CaseName = models.CharField(max_length=50, verbose_name="case名称")
    Result = models.CharField(max_length=10, verbose_name="结果")
    Reason = models.CharField(max_length=30, verbose_name="失败原因")
    Capacity = models.CharField(max_length=5,verbose_name="当前电量")
    Trace = models.CharField(max_length=1000, verbose_name="Trace路径")
    Bugreport = models.CharField(max_length=100, verbose_name="Bureport路径")
    ScreenShot = models.CharField(max_length=100, verbose_name="截图路径")
    Version = models.CharField(max_length=20, verbose_name="版本")
    Timestamp = models.DateTimeField()
    
    class Meta:
        db_table = 'camera_cts' 
        abstract = True

class CC_mi2s(camera_cts):
    class Meta:
        db_table = 'CC_mi2s'
        verbose_name="相机测试MI2s"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.CaseName, self.Result
    
class CC_mi2a(camera_cts):
    class Meta:
        db_table = 'CC_mi2a'
        verbose_name="相机测试MI2a"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.CaseName, self.Result
    
class CC_mi3w(camera_cts):
    class Meta:
        db_table = 'CC_mi3w'
        verbose_name="相机测试MI3w"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.CaseName, self.Result

class CC_mi3td(camera_cts):
    class Meta:
        db_table = 'CC_mi3td'
        verbose_name="相机测试MI3td"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.CaseName, self.Result
    
############################################################################
#test table
class test_table(models.Model):
    title = models.CharField(max_length=50, verbose_name="title")
    Timestamp = models.DateTimeField()
    Version = models.CharField(max_length=20, verbose_name="版本")
    class Meta:
        db_table = 'test' 
        abstract = True

class test_tb1(test_table):
    class Meta:
        db_table = 'test_tb1'
        verbose_name="测试表"
        ordering = ('-Timestamp',)
    def __unicode__(self):
        return self.Title
    