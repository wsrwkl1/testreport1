#coding=utf-8 
'''
Created on 2013-10-18

@author: hequn
'''
from django.contrib import admin
from TRR.models import BL_mi2s, BL_mi2a, BL_mi3w,BL_mi3td, Current_mi2s, Current_mi2a, Current_mi3w,Current_mi3td
from TRR.models import CI_mi2s,CI_mi2a,CI_mi3w,CI_mi3td, CC_mi2s,CC_mi2a,CC_mi3w,CC_mi3td

class BL_admin(admin.ModelAdmin):
    list_display = ('Version','Timestamp')
    ordering = ('-Timestamp',)
    
class Current_admin(admin.ModelAdmin):
    list_display = ('Version','Timestamp')
    ordering = ('-Timestamp',)

class CI_admin(admin.ModelAdmin):
    list_display = ('BugID','Title','Timestamp')
    ordering = ('-Timestamp',)

class CC_admin(admin.ModelAdmin):
    list_display = ('CaseName','Result','Timestamp')
    ordering = ('-Timestamp',)
admin.site.register(BL_mi2s,BL_admin)
admin.site.register(BL_mi2a,BL_admin)
admin.site.register(BL_mi3w,BL_admin)
admin.site.register(BL_mi3td,BL_admin)
admin.site.register(Current_mi2s,Current_admin)
admin.site.register(Current_mi2a,Current_admin)
admin.site.register(Current_mi3w,Current_admin)
admin.site.register(Current_mi3td,Current_admin)
admin.site.register(CI_mi2s,CI_admin)
admin.site.register(CI_mi2a,CI_admin)
admin.site.register(CI_mi3w,CI_admin)
admin.site.register(CI_mi3td,CI_admin)
admin.site.register(CC_mi2s,CC_admin)
admin.site.register(CC_mi2a,CC_admin)
admin.site.register(CC_mi3w,CC_admin)
admin.site.register(CC_mi3td,CC_admin)