#coding=utf-8 
'''
Created on 2014-2-10

@author: hequn
'''
import MySQLdb  
from xml.dom import minidom  

def parsexmlnode():
    folder = ''
    doc = minidom.parse("Camera_Stress_Testing_result.xml")  
    root = doc.documentElement  
    citys = root.getElementsByTagName("test")  
      
    #conn = MySQLdb.connect(host="local",user="local",passwd="local",db="bw_local", charset='utf8')  
    #cursor = conn.cursor()  
    for city in citys:  
        #print city.toxml()  
        nameNode = city.getElementsByTagName("Name")[0]  
        print (nameNode.nodeName + ":" + nameNode.childNodes[0].nodeValue)  
        ResultNode = city.getElementsByTagName("Result")[0]  
        print (ResultNode.nodeName + ":" + ResultNode.childNodes[0].nodeValue)  
        #failedReasonNode = city.getElementsByTagName("failedReason")[0] 
        #print (failedReasonNode.nodeName + ":" + failedReasonNode.childNodes[0].nodeValue) 
        #cursor.execute('insert into original(city,code) values(%s,%s);',(nameNode.childNodes[0].nodeValue,codeNode.childNodes[0].nodeValue))  
      
    #conn.commit()  
    #cursor.close()  
    #conn.close()  
    print "success"