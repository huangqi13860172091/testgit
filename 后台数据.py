# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:47:49 2020

@author: Administrator
"""


from selenium import webdriver
from lxml import etree
import pandas as pd
import time


def get_data(etree_obj):  
    '签约主播,虎牙号,流水收入'
    
  
    签约主播=etree_obj.xpath('//*[@id="app"]/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div/span/text()')

    虎牙号=etree_obj.xpath('//*[@id="app"]/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr/td[2]/div/text()') 
                

    流水收入=etree_obj.xpath('//*[@id="app"]/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr/td[3]/div/text()')

    


    return 签约主播,虎牙号,流水收入

if __name__=='__main__': 


    

    page_num=3  #页数
    url='https://ow.huya.com/#/ow/operationSummary/owincome'
    
    driver = webdriver.Chrome()#打开Chrome浏览器
    driver.get(url)#打开网址
    time.sleep(30)


    html_code = driver.page_source#获取网页代码
    etree_obj=etree.HTML(html_code)#将网页代码转为etree对象
    
    签约主播_list,虎牙号_list,流水收入_list=[],[],[]#初始化数据容器为空列表

    
    签约主播,虎牙号,流水收入=get_data(etree_obj)#解析数据

   
    #爬取下一页
    if page_num>1:
        for i in range(page_num):
            time.sleep(1)
            driver.find_element_by_xpath('//li[@class="pager pager--next"]').click()#点击下一页

            html_code = driver.page_source#获取网页代码-
            etree_obj=etree.HTML(html_code)#将网页代码转为etree对象
            签约主播,虎牙号,流水收入=get_data(etree_obj)#解析数据
            签约主播_list+=签约主播
            虎牙号_list+=虎牙号
            流水收入_list+=流水收入
            
    driver.close()
    
    #数据存储
    data=zip(签约主播_list,虎牙号_list,流水收入_list)
    data_df=pd.DataFrame(data,columns=['签约主播','虎牙号','流水收入'])
    data_df.to_excel('./63342.xlsx')
    

