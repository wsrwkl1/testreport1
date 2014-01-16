#coding=utf-8 
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from database import executsql, QueryVersionAllTable,amcharts,QueryVersionSignalTable
from getselectedinfo import GetLatestInfoAllTable, GetLatestInfoSignalTable,getcompareinfo
from getvariety import getvar

#@login_required(login_url='/accounts/login')
def home(self):
    dic = GetLatestInfoAllTable(self)
    return render_to_response('index.html',dic)

#######################################################
#variety 测试种类
#info_dic 所查询的表中的所有信息
#template 页需要的一些变量
########################################################
#@login_required(login_url='/accounts/login') 
def blinfo(self):
    t = 'bl'
    variety = getvar(t)
    info_dic = GetLatestInfoSignalTable(t)
    all_version_dic = QueryVersionAllTable(t)
    product = info_dic.get('p')
    latestversion = QueryVersionSignalTable(t,product)   
    other_dic = {'product':product,'latestversion':latestversion,'variety':variety}
    temp_dic = dict(all_version_dic,**other_dic)
    result_dic =dict(info_dic, **temp_dic) 
    return render_to_response('blinfo.html',result_dic)

#@login_required(login_url='/accounts/login/')
def blsearch(request):
    error = False
    t = 'bl'
    variety = getvar(t)
    all_version_dic = QueryVersionAllTable(t)
    #print t
    product = request.GET.getlist('product')
    pro = str(''.join(product) )#将list转为str
    p = str(pro.split('/',1)[0]) #取/前的部分
    #print p
    if not p:
        error = True
        info = "请在左侧单选列表中选择所要查询的产品"
    #print len(p)
    else:
        latestversion = QueryVersionSignalTable(t,p)
        other_dic = {'product':p,'variety':variety,'latestversion':latestversion}
        #print other_dic
        amcharts_dic = amcharts(request,t)
        #print amcharts_dic
        #合并两个字典
        temp_dic = dict(all_version_dic,**other_dic)
        result_dic = dict(amcharts_dic, **temp_dic)
        #print result_dic
        return render_to_response('blsearch.html',result_dic)
    return render_to_response('blinfo.html', {'error': error,'info':info})

#@login_required(login_url='/accounts/login/')
def blComReasult(request):
    
    t = 'bl'
    all_version_dic = QueryVersionAllTable(t)
    info_dic = getcompareinfo(request,t)
    result_dic = dict(all_version_dic,**info_dic)
    error = info_dic.get('error')
    info = info_dic.get('info')
    if error == True:
        return render_to_response('blcompare.html', {'error': error,'info':info})
    else:
        return render_to_response('blcompare.html',result_dic)

#@login_required(login_url='/accounts/login/')
def currinfo(self):
    t = 'current'
    variety = getvar(t)
    all_version_dic = QueryVersionAllTable(t)
    info_dic = GetLatestInfoSignalTable(t)
    product = info_dic.get('p')
    latestversion = QueryVersionSignalTable(t,product)
    other_dic = {'product':product,'variety':variety,'latestversion':latestversion}
    temp_dic =dict(info_dic, **other_dic) 
    result_dic = dict(temp_dic,**all_version_dic)
    return render_to_response('currinfo.html',result_dic)

#@login_required(login_url='/accounts/login/')
def currsearch(request):
    t = 'current'
    variety = getvar(t)
    all_version_dic = QueryVersionAllTable(t)
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
        #tag_dic(p)
        latestversion = QueryVersionSignalTable(t,p)
        other_dic = {'product':p,'variety':variety,'latestversion':latestversion}
        amcharts_dic = amcharts(request,t)
        #print amcharts_dic,s_dic
        #合并两个字典
        temp_dic = dict(amcharts_dic, **other_dic)
        result_dic = dict(temp_dic,**all_version_dic)
        #print temp_dic
        return render_to_response('currsearch.html',result_dic)
    return render_to_response('currinfo.html', {'error': error,'info':info})

#@login_required(login_url='/accounts/login/')
def currcompare(request):
    t = 'current'
    all_version_dic = QueryVersionAllTable(t)
    info_dic = getcompareinfo(request,t)
    error = info_dic.get('error')
    info = info_dic.get('info')
    result_list = info_dic.get('result_list')
    result0 = result_list[0]
    result1 = result_list[1]
    dic = {'result0':result0,'result1':result1}
    temp_dic = dict(dic,**info_dic)
    result_dic = dict(all_version_dic,**temp_dic)
    if error == True:
        return render_to_response('currcompare.html', {'error': error,'info':info})
    else:
        return render_to_response('currcompare.html',result_dic)