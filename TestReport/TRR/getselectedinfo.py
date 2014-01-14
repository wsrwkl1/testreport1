#coding=utf-8
'''
Created on 2014-1-9

@author: hequn
'''
from database import executsql, QueryVersionAllTable,QueryVersionSignalTable
from datetime import AllTableLatesUpdateTime, SignalTableLatesUpdateTime
import usefull_var

######################################
#GetLatestInfoAllTable 获取所有表中最新更新内容
######################################
def GetLatestInfoAllTable(self):
    newdt = AllTableLatesUpdateTime(self)
    #print newdt
    TestTypeList = usefull_var.TestTypeList
    TestProductList = usefull_var.TestProductList
    for t in TestTypeList:
        for p in TestProductList:
            newsql = 'select * from ' + t + '_' + p + ' where Timestamp = "%s"' %(newdt)
            rows = executsql(newsql)
            if len(rows) == 1:
                variety = t
                product = p
                if variety == "bl":
                    selecttemp = "BatteryLife"
                    for row in rows:
                        Version = row["Version"]
                        Game = row["Game"]
                        Music = row["Music"]
                        PlayVideo = row["PlayVideo"]
                        ReadBook = row["ReadBook"]
                        WeiBO = row["WeiBO"]
                        CallMO = row["CallMO"]
                        Brower = row["Brower"]
                        Camera = row["Camera"]
                        Remain = row["Remain"]
                        #print Version,Game,Music,PlayVideo,ReadBook,WeiBO,CallMO,Brower,Camera,Remain
                        dic = {'Version':Version,'Game':Game,'Music':Music,'PlayVideo':PlayVideo,'ReadBook':ReadBook,'WeiBO':WeiBO,'CallMO':CallMO,'Brower':Brower,'Camera':Camera,'Remain':Remain}
                elif variety == "current":
                    for row in rows:
                        selecttemp = "Current"
                        Version = row["Version"]
                        Item1 = row["Item1"]
                        Item2 = row["Item2"]
                        Item3 = row["Item3"]
                        Item4 = row["Item4"]
                        Item5 = row["Item5"]
                        Item6 = row["Item6"]
                        Item7 = row["Item7"]
                        Item8 = row["Item8"]
                        Item9 = row["Item9"]
                        Item10 = row["Item10"]
                        Item11 = row["Item11"]
                        Item12 = row["Item12"]
                        Item13 = row["Item13"]
                        Item14 = row["Item14"]
                        Item15 = row["Item15"]
                        Item16 = row["Item16"]
                        Item17 = row["Item17"]
                        Item18 = row["Item18"] 
                        Item19 = row["Item19"]
                        Item20 = row["Item20"]
                        Item21 = row["Item21"]
                        dic = {'Version':Version,'Item1': Item1, 'Item2': Item2,'Item3': Item3,'Item4': Item4,'Item5': Item5,'Item6': Item6,'Item7': Item7,'Item8': Item8, 'Item9': Item9,'Item10': Item10,
                               'Item11': Item11,'Item12': Item12,'Item13': Item13,'Item14': Item14,'Item15': Item15,'Item16': Item16,'Item17': Item17,'Item18': Item18,'Item19':Item19,'Item20':Item20,'Item21':Item21}
    verison = QueryVersionSignalTable(t,p)
    other_dic = {'variety':variety,'product':product,'verison':verison,'selecttemp':selecttemp}
    dic = dict(dic, **other_dic)
    return dic

##########################################
#GetLatestInfoSignalTable 获取指定表中最新更新内容
#不指定参数P查询的是t种测试所有表中最新的更新内容
#指定p则查询指定测试种类和产品的表的最新更新内容
##########################################
def GetLatestInfoSignalTable(t):
    TestProductList = usefull_var.TestProductList
    for p in TestProductList:
        newdt = SignalTableLatesUpdateTime(t)
        newsql = 'select * from ' + t + '_' + p + ' where Timestamp = "%s"' %(newdt)
        rows = executsql(newsql)
        if len(rows) == 1:
            p = p
            newsql = 'select * from ' + t + '_' + p + ' where Timestamp = "%s"' %(newdt)
            rows = executsql(newsql)
            #print rows
            if t == "bl":
                for row in rows:
                    Version = row["Version"]
                    Game = row["Game"]
                    Music = row["Music"]
                    PlayVideo = row["PlayVideo"]
                    ReadBook = row["ReadBook"]
                    WeiBO = row["WeiBO"]
                    CallMO = row["CallMO"]
                    Brower = row["Brower"]
                    Camera = row["Camera"]
                    Remain = row["Remain"]
                    #print Version,Game,Music,PlayVideo,ReadBook,WeiBO,CallMO,Brower,Camera,Remain
                    tem_dic = {'Version':Version,'Game':Game,'Music':Music,'PlayVideo':PlayVideo,'ReadBook':ReadBook,'WeiBO':WeiBO,'CallMO':CallMO,'Brower':Brower,'Camera':Camera,'Remain':Remain}
                    #print tem_dic
            elif t == "current":
                for row in rows:
                    Version = row["Version"]
                    Item1 = row["Item1"]
                    Item2 = row["Item2"]
                    Item3 = row["Item3"]
                    Item4 = row["Item4"]
                    Item5 = row["Item5"]
                    Item6 = row["Item6"]
                    Item7 = row["Item7"]
                    Item8 = row["Item8"]
                    Item9 = row["Item9"]
                    Item10 = row["Item10"]
                    Item11 = row["Item11"]
                    Item12 = row["Item12"]
                    Item13 = row["Item13"]
                    Item14 = row["Item14"]
                    Item15 = row["Item15"]
                    Item16 = row["Item16"]
                    Item17 = row["Item17"]
                    Item18 = row["Item18"] 
                    Item19 = row["Item19"]
                    Item20 = row["Item20"]
                    Item21 = row["Item21"]
                    tem_dic = {'Version':Version,'Item1': Item1, 'Item2': Item2,'Item3': Item3,'Item4': Item4,'Item5': Item5,'Item6': Item6,'Item7': Item7,'Item8': Item8, 'Item9': Item9,'Item10': Item10,
                           'Item11': Item11,'Item12': Item12,'Item13': Item13,'Item14': Item14,'Item15': Item15,'Item16': Item16,'Item17': Item17,'Item18': Item18,'Item19':Item19,'Item20':Item20,'Item21':Item21}
                    #print tem_dic
    other_dic = {'p':p}
    dic = dict(tem_dic, **other_dic)
    #print dic
    return dic

def getcompareinfo(request,t):
    com_ver_list = []
    result_list = []
    tname_list = []
    
    error = False
    info = ''
    #获取template中selecte中name为product0的值。
    product0 = request.GET.getlist('product0')
    pro0 = str(''.join(product0) )#将list转为str
    p0 = str(pro0.split('/',1)[0]) #取/前的部分
    print p0,type(p0)
    #获取template中selecte中name为product1的值。
    product1 = request.GET.getlist('product1')
    pro1 = str(''.join(product1) )#将list转为str
    p1 = str(pro1.split('/',1)[0]) #取/前的部分
    print p1,type(p1)
    version0 = request.GET.get('version0')
    com_ver_list.append(version0)
    version1 = request.GET.get('version1')
    com_ver_list.append(version1)
    #com_ver_list_l = len(com_ver_list)
    print com_ver_list
    tname0 = t + '_' + p0
    tname1 = t + '_' + p1
    if tname0 == tname1:
        tname_list.append(tname0)
    else:
        tname_list.append(tname0)
        tname_list.append(tname1)
    #print tname_list
    if p0 == "0" or p1 == "0":
        #print p0,p1
        error = True
        info = "请选择所要搜索的产品"
    elif version0 == "0" or version1 =="0":
        #print version0,version1
        error = True
        info = "请选择所要对比的版本"
    elif p0 == p1 and version0 == version1:
        error =True
        info = "请选择不同版本进行对比"
    #print len(p)
    elif p0 == "mi2s" and p1 != "mi2s":
        error = True
        info = "请选择同一型号进行对比"
    
    elif p0 == "mi2a" and p1 != "mi2a":
        error = True
        info = "请选择同一型号进行对比"
        
    else:
        for com_ver in com_ver_list:
            for tname in tname_list:
                com_sql = 'select * from %s where version = "%s" order by Timestamp desc' % (tname,com_ver)
                #print com_sql
                rows = executsql(com_sql)
                #L = len(rows)
                for row in rows:
                    if len(row) > 0:
                        result_list.append(row)
    dic = {'result_list':result_list}
    other_dic = {'product0':p0,'product1':p1,'version0':version0,'version1':version1}
    error_dic = {'error':error,'info':info}
    temp_dic = dict(dic,**other_dic)
    info_dic = dict(temp_dic,**error_dic)
    return info_dic
        
    