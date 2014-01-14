#coding=utf-8 
from TRR import models
from django.contrib import admin
'''
Created on 2013-10-18

@author: hequn
'''
from django.contrib import admin
from TRR.models import BL_mi2s, BL_mi2a, BL_mi3w,BL_mi3td, Current_mi2s, Current_mi2a, Current_mi3w,Current_mi3td

class BL_mi2s_admin(admin.ModelAdmin):
    list_display = ('Version','Timestamp')
    ordering = ('-Timestamp',)


class BL_mi2a_admin(admin.ModelAdmin):
    list_display = ('Version','Timestamp')
    ordering = ('-Timestamp',)
    
class BL_mi3_admin(admin.ModelAdmin):
    list_display = ('Version','Timestamp')
    ordering = ('-Timestamp',)
    
class Current_mi2s_admin(admin.ModelAdmin):
    list_display = ('Version','Timestamp')
    ordering = ('-Timestamp',)
    
class Current_mi2a_admin(admin.ModelAdmin):
    list_display = ('Version','Timestamp')
    ordering = ('-Timestamp',)
    
class Current_mi3_admin(admin.ModelAdmin):
    list_display = ('Version','Timestamp')
    ordering = ('-Timestamp',)
    
admin.site.register(BL_mi2s,BL_mi2s_admin)
admin.site.register(BL_mi2a,BL_mi2a_admin)
admin.site.register(BL_mi3w,BL_mi3_admin)
admin.site.register(BL_mi3td,BL_mi3_admin)
admin.site.register(Current_mi2s,Current_mi2s_admin)
admin.site.register(Current_mi2a,Current_mi2a_admin)
admin.site.register(Current_mi3w,Current_mi3_admin)
admin.site.register(Current_mi3td,Current_mi3_admin)