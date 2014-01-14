#coding=utf-8
'''
Created on 2014-1-2

@author: hequn
'''
from database import executsql
import usefull_var
###################################
#统计所有时间相关的方法
#TEST_TYPE_LIST 测试类型列表。current----电流测试。bl-----功耗测试
#TEST_PRODUCT_LIST测试产品的列表。与类型列表共同组成查询所需的表名。current_mi2s,bl_mi2s等
###################################


#1. 所有表中最近更新的表的时间点 alltablelatestupdatetime
def AllTableLatesUpdateTime(self):
    TestTypeList = usefull_var.TestTypeList
    TestProductList = usefull_var.TestProductList
    dtlist = [] #存放每个表的最新更新时间点
    for t in TestTypeList:
        for p in TestProductList:
            sql = 'select Timestamp from ' + t +'_' + p +' order by Timestamp desc limit 1'
            #print sql
            rows = executsql(sql)
            for row in rows:
                dt = row["Timestamp"]
                dtlist.append(dt)
    maxdt = max(dtlist)
    #print maxdt
    newdt = maxdt.strftime("%Y-%m-%d %X") #在dtlist取出最大的时间值，把datetime转为str
    return newdt

def SignalTableLatesUpdateTime(t):
    TestProductList = usefull_var.TestProductList
    dtlist = [] #存放每个表的最新更新时间点
    for p in TestProductList:
        sql = 'select Timestamp from ' + t +'_' + p +' order by Timestamp desc limit 1'
        #print sql
        rows = executsql(sql)
        for row in rows:
            dt = row["Timestamp"]
            dtlist.append(dt)
    maxdt = max(dtlist)
    #print maxdt
    newdt = maxdt.strftime("%Y-%m-%d %X") #在dtlist取出最大的时间值，把datetime转为str
    return newdt