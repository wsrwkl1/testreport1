#coding=utf-8 
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.views import login
from TRR.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.views import redirect_to_login
#from powertest.models import User
import MySQLdb
#import time,datetime

blsea_dic = {}
currsea_dic = {}
currtag_dic = {}
v_dic = {}


@login_required(login_url='/accounts/login')
def home(self):
    dtlist = [] #存放每个表的最新更新时间
    #variety = '电流测试'
    var_list = ['current','bl'] 
    p_list = ['mi2s','mi2a','mi3w','mi3td']
    #delta = datetime.timedelta(hours = 8) #东八区时差8小时
    for var in var_list:
        for p in p_list:
            sql = 'select Timestamp from ' + var +'_' + p +' order by Timestamp desc limit 1'
            #print sql
            rows = executsql(sql)
            for row in rows:
                dt = row["Timestamp"]
                dtlist.append(dt)
    maxdt = max(dtlist)
    #print maxdt
    newdt = maxdt.strftime("%Y-%m-%d %X") #在dtlist取出最大的时间值，把datetime转为str
    for var in var_list:
        for p in p_list:
            newsql = 'select * from ' + var + '_' + p + ' where Timestamp = "%s"' %(newdt)
            rows = executsql(newsql)
            if len(rows) == 1:
                variety = var
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
    a_dic = {'product':product,'variety':variety,'selecttemp':selecttemp}
    s_dic =dict(dic, **a_dic) 
    return render_to_response('index.html',s_dic)

@login_required(login_url='/accounts/login') 
def blinfo(self):
    global v_dic
    t = 'bl'
    blcompare(t)
    dtlist = []
    variety = '续航测试'
    p_list = ['mi2s','mi2a','mi3w','mi3td']
    #delta = datetime.timedelta(hours = 8) #东八区时差8小时
    for p in p_list:
        sql = 'select Timestamp from bl_' + p + ' order by Timestamp desc limit 1'
        rows = executsql(sql)
        for row in rows:
            dt = row["Timestamp"]
            dtlist.append(dt)
    maxdt = max(dtlist)        
    newdt = maxdt.strftime("%Y-%m-%d %X") #在dtlist取出最大的时间值，把datetime转为str
    #print newdt
    for p in p_list:
        newsql = 'select * from bl_' + p + ' where Timestamp = "%s"' %(newdt)
        rows = executsql(newsql)
        #print len(rows)
        if len(rows) == 1:
            product = p
            #print rows
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
    a_dic = {'product':product,'variety':variety}
    temp_dic = dict(v_dic,**a_dic)
    s_dic =dict(dic, **temp_dic) 
    return render_to_response('blinfo.html',s_dic)

@login_required(login_url='/accounts/login/')
def blsearch(request):
    global blsea_dic
    global v_dic
    variety = '电池续航测试'
    error = False
    t = 'bl'
    blcompare(t)
    #print v_dic
    product = request.GET.getlist('product')
    pro = str(''.join(product) )#将list转为str
    p = str(pro.split('/',1)[0]) #取/前的部分
    #print p
    if not p:
        error = True
        info = "请在左侧单选列表中选择所要查询的产品"
    #print len(p)
    else:
        s_dic = {'product':p,'variety':variety}
        blamcharts(request)
        
        #合并两个字典
        temp_dic = dict(v_dic,**s_dic)
        dic = dict(blsea_dic, **temp_dic)
        #print dic
        return render_to_response('blsearch.html',dic)
    return render_to_response('blinfo.html', {'error': error,'info':info})

def blcompare(t):
    global v_dic
    mi2slist = []
    mi2alist = []
    mi3wlist = []
    mi3tdlist = []
        
    p_list = ['mi2s','mi2a','mi3w','mi3td']
     
    for p in p_list:
        sql = 'select version from ' + t + '_' + p + ' order by Timestamp desc limit 10'
        #print sql
        rows = executsql(sql)
        if p is 'mi2s':
            for row in rows:
                Version = row["version"]
                mi2slist.append(Version)
        if p is 'mi2a':
            for row in rows:
                Version = row["version"]
                mi2alist.append(Version)
        if p is 'mi3w':
            for row in rows:
                Version = row["version"]
                mi3wlist.append(Version)
        if p is 'mi3td':
            for row in rows:
                Version = row["version"]
                mi3tdlist.append(Version)
                
    v_dic = {'mi2slist':mi2slist,'mi2alist':mi2alist,'mi3wlist':mi3wlist,'mi3tdlist':mi3tdlist}
    #print isinstance(v_dic,dict)
    return v_dic
@login_required(login_url='/accounts/login/')
def blComReasult(request):
    com_ver_list = []
    result_list = []
    global v_dic
    t = 'bl'
    blcompare(t)
    error = False
    product = request.GET.getlist('product')
    pro = str(''.join(product) )#将list转为str
    p = str(pro.split('/',1)[0]) #取/前的部分
    #print p
    version0 = request.GET.get('version0')
    com_ver_list.append(version0)
    version1 = request.GET.get('version1')
    com_ver_list.append(version1)
    com_ver_list_l = len(com_ver_list)
    if not p:
        error = True
        info = "请选择所要搜索的产品"
    elif not version0 and version1:
        error = True
        info = "请选择所要对比的版本"
    elif version0 == version1:
        error =True
        info = "请选择不同版本进行对比"
    #print len(p)
    else:
        if com_ver_list_l != 2:
            error = True
            info = "请选择所要对比的版本"
        else:
            tname = "bl_" + p
            for com_ver in com_ver_list:
                com_sql = 'select * from %s where version = "%s" order by Timestamp desc' % (tname,com_ver)
                rows = executsql(com_sql)
                #L = len(rows)
                for row in rows:
                    result_list.append(row)
                
        c_dic = {'result_list':result_list,'product':p}
        dic = dict(v_dic,**c_dic)
        return render_to_response('blsearch.html',dic)
    return render_to_response('blsearch.html', {'error': error,'info':info})
@login_required(login_url='/accounts/login/')
def currinfo(self):
    dtlist = []
    variety = '电流测试'
    p_list = ['mi2s','mi2a','mi3w','mi3td']
    global v_dic
    t = 'current'
    blcompare(t)
    for p in p_list:
        sql = 'select Timestamp from current_' + p + ' order by Timestamp desc limit 1'
        rows = executsql(sql)
        for row in rows:
            dt = row["Timestamp"]
            dtlist.append(dt)
    maxdt = max(dtlist)        
    newdt = maxdt.strftime("%Y-%m-%d %X") #在dtlist取出最大的时间值，把datetime转为str
    #print newdt
    for p in p_list:
        newsql = 'select * from current_' + p + ' where Timestamp = "%s"' %(newdt)
        rows = executsql(newsql)
        #print len(rows)
        if len(rows) == 1:
            product = p
            #print rows
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
    dic = {'Version':Version,'Item1': Item1, 'Item2': Item2,'Item3': Item3,'Item4': Item4,'Item5': Item5,'Item6': Item6,'Item7': Item7,'Item8': Item8, 'Item9': Item9,'Item10': Item10,
           'Item11': Item11,'Item12': Item12,'Item13': Item13,'Item14': Item14,'Item15': Item15,'Item16': Item16,'Item17': Item17,'Item18': Item18,'Item19':Item19,'Item20':Item20,'Item21':Item21}
    a_dic = {'product':product,'variety':variety}
    s_dic =dict(dic, **a_dic) 
    dic = dict(s_dic,**v_dic)
    return render_to_response('currinfo.html',dic)
@login_required(login_url='/accounts/login/')
def currsearch(request):
    global currsea_dic
    global currtag_dic
    global v_dic
    t = 'current'
    blcompare(t)
    currtag_dic = {}
    variety = '电流测试'
    error = False
    product = request.GET.getlist('product')
    pro = str(''.join(product) )#将list转为str
    p = str(pro.split('/',1)[0]) #取/前的部分
    #print p
    if not p:
        error = True
        info = "请选择所要搜索的产品"
    #print len(p)
    else:
        tag_dic(p)
        s_dic = {'product':p,'variety':variety}
        temp_dic = dict(s_dic,**currtag_dic)
        curramcharts(request)
        #合并两个字典
        dic = dict(currsea_dic, **temp_dic)
        dic = dict(dic,**v_dic)
        #print dic
        return render_to_response('currsearch.html',dic)
    return render_to_response('currinfo.html', {'error': error,'info':info})

@login_required(login_url='/accounts/login/')
def blamcharts(request):
    global blsea_dic
    product = request.GET.getlist('product')
    pro = str(''.join(product) )#将list转为str
    p = str(pro.split('/',1)[0]) #取/前的部分
    tname = "bl_" + p
    amcharts_sql = 'select * from %s order by Timestamp desc limit 3' % (tname)
    rows = executsql(amcharts_sql)
    result_list = []
    for row in rows:
        result_list.append(row)
    blsea_dic = {'result_list':result_list}
    return blsea_dic
@login_required(login_url='/accounts/login/')
def curramcharts(request):
    global currsea_dic
    product = request.GET.getlist('product')
    pro = str(''.join(product) )#将list转为str
    p = str(pro.split('/',1)[0]) #取/前的部分
    tname = "current_" + p
    amcharts_sql = 'select * from %s order by Timestamp desc limit 10' % (tname)
    rows = executsql(amcharts_sql)
    result_list = []
    for row in rows:
        result_list.append(row)
    currsea_dic = {'result_list':result_list}
    return currsea_dic
@login_required(login_url='/accounts/login/')
def currcompare(request):
    com_ver_list = []
    result_list = []
    global v_dic
    t = 'current'
    blcompare(t)
    error = False
    product = request.GET.getlist('product')
    pro = str(''.join(product) )#将list转为str
    p = str(pro.split('/',1)[0]) #取/前的部分
    #print p
    version0 = request.GET.get('version0')
    com_ver_list.append(version0)
    version1 = request.GET.get('version1')
    com_ver_list.append(version1)
    com_ver_list_l = len(com_ver_list)
    if not p:
        error = True
        info = "请选择所要搜索的产品"
    elif not version0 and version1:
        error = True
        info = "请选择所要对比的版本"
    elif version0 == version1:
        error =True
        info = "请选择不同版本进行对比"
    #print len(p)
    else:
        if com_ver_list_l != 2:
            error = True
            info = "请选择所要对比的版本"
        else:
            tname = t + '_' + p
            for com_ver in com_ver_list:
                com_sql = 'select * from %s where version = "%s" order by Timestamp desc' % (tname,com_ver)
                rows = executsql(com_sql)
                #L = len(rows)
                for row in rows:
                    result_list.append(row)
            print result_list
            result0 = result_list[0]
            result1 = result_list[1]
            #print result0,result1
            
        c_dic = {'result0':result0,'result1':result1,'product':p,'version0':version0,'version1':version1}
        dic = dict(v_dic,**c_dic)
        return render_to_response('currcompare.html',dic)
    return render_to_response('currcompare.html', {'error': error,'info':info})

def tag_dic(pro):
    global currtag_dic
    TLoc_Video = 300
    TContect = 350
    tagtem = 0
    if pro == "mi3":
        TGame= 800
        TScreen = 450
        TBrower = 600
        OMakeVideo = 1000
        CMakeVideo = 900
    if pro == "mi2":
        TGame = 450
        TScreen = 250
        TBrower = 200
        CMakeVideo = 550
        
    currtag_dic = {'TLoc_Video':TLoc_Video,'TGame':TGame,'TScreen':TScreen,'TContect':TContect,'TBrower':TBrower,'OMakeVideo':OMakeVideo,'CMakeVideo':CMakeVideo,'tagtem':tagtem}
    return currtag_dic
    
def executsql (sql):
    connection = MySQLdb.connect(user='root', db='testreport', passwd='xiaomi#1', host='localhost')  
    #执行SQL语句返回List，每行数据为Dict
    cursor=connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(sql)
    connection.close()
    return cursor.fetchall()