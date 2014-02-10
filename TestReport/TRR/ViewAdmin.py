#coding=utf-8 
'''
Created on 2014-2-10

@author: hequn
'''
from TRR.models import CC_mi2s

CaseName=''
Result=''
Reason=''
Capacity=''
Trace=''
Bugreport=''
ScreenShot=''
Version=''
Timestamp=''

cc_mi2s = CC_mi2s(CaseName="%s",Result="%s",Reason="%s",Capacity="%s",Trace="%s",Bugreport="%s",ScreenShot="%s",Version="%s",Timestamp="%s") % (CaseName,Result,Reason,Capacity,Trace,Bugreport,ScreenShot,Version,Timestamp)
