#coding=utf-8 
'''
Created on 2014-1-2

@author: hequn
'''
import MySQLdb
import usefull_var

def executsql (sql):
    connection = MySQLdb.connect(user='root', db='testreport', passwd='xiaomi#1', host='localhost')  
    #执行SQL语句返回List，每行数据为Dict
    cursor=connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(sql)
    connection.close()
    return cursor.fetchall()

def QueryVersionAllTable(t):
    mi2slist = []
    mi2alist = []
    mi3wlist = []
    mi3tdlist = []
    
    TestProductList = usefull_var.TestProductList    
     
    for p in TestProductList:
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
                
    all_version_dic = {'mi2slist':mi2slist,'mi2alist':mi2alist,'mi3wlist':mi3wlist,'mi3tdlist':mi3tdlist}
    #print isinstance(all_version_dic,dict)
    return all_version_dic
    
def QueryVersionSignalTable(t,p):
        
    sql = 'select version from ' + t + '_' + p + ' order by Timestamp desc limit 1'
    rows = executsql(sql)
    for row in rows:
        version = row["version"]
    return version

def amcharts(request,t):
    product = request.GET.getlist('product')
    pro = str(''.join(product) )#将list转为str
    p = str(pro.split('/',1)[0]) #取/前的部分
    
    tname = t + '_' + p
    amcharts_sql = 'select * from %s order by Timestamp desc limit 3' % (tname)
    rows = executsql(amcharts_sql)
    result_list = []
    for row in rows:
        result_list.append(row)
    amcharts_dic = {'result_list':result_list}
    #print result_list
    return amcharts_dic
