#encoding:utf-8
import os
import sys,xlrd
from selenium.webdriver.common.by import By
from HuaYingData import ReadExcel,get_number_by_data
import OperateLoginElement
from Action import Browser
import time,OperateRegisterElement
class LocateRegisterObject():
    #该类主要是去定位登录功能中所用到的元素
    def getRegisterObject(self,browser,phoneNumber,firstPassword,secondPassword,pictureCheckCode,smsCheckCode,alertmessage):
        """循环需要定位的元素，拿到一个元素之后去调用getLocatMethodAndData方法，取得元素的定位方式以及定位所需数据"""
        register_excel_path=r"G:\HuaYing\HuaYingData\registerByPhoneNumber_data.xls"
        register_object_sheet=ReadExcel.ReadExcel().getTableBySheetName(register_excel_path,"objname_locatemethod_locatedata")
        rows=register_object_sheet.nrows
        register_object_list=[]
        for i in range(rows):
            register_object_list.append(register_object_sheet.cell_value(i,0))
        # print register_object_list
        register_object_list.pop(0)
        # print register_object_list
        for login_object in register_object_list:
            self.getLocateMethodAndData(browser,login_object,phoneNumber,firstPassword,secondPassword,pictureCheckCode,smsCheckCode,alertmessage)



    def getLocateMethodAndData(self,browser,objname,phoneNumber,firstPassword,secondPassword,pictureCheckCode,smsCheckCode,alertmessage):
        """根据需要定位的元素的名称得到需要定位的元素的定位方式以及定位数据"""
        register_excel_path=r"G:\HuaYing\HuaYingData\registerByPhoneNumber_data.xls"
        register_object_sheet=ReadExcel.ReadExcel().getTableBySheetName(register_excel_path,"objname_locatemethod_locatedata")
        row_col_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(register_excel_path,"objname_locatemethod_locatedata",objname)
        old_how=register_object_sheet.cell_value(row_col_list[0],row_col_list[1]+1)
        what=register_object_sheet.cell_value(row_col_list[0],row_col_list[1]+2)
        #在这里增加一个字典是因为如果直接把By.ID写在excel里的话，取出来不能用
        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}
        new_how=locate_method_dict[old_how]
        # print new_how
        self.locateElement(browser,new_how,what,objname,phoneNumber,firstPassword,secondPassword,pictureCheckCode,smsCheckCode,alertmessage)

    def locateElement(self,browser,how,what,obj_name,phoneNumber,firstPassword,secondPassword,pictureCheckCode,smsCheckCode,alertmessage):
        br=browser
        # print br
        located_element=br.find_element(by=how,value=what)
        OperateRegisterElement.OperateElement().operateElement(br,obj_name,located_element,phoneNumber,firstPassword,secondPassword,pictureCheckCode,smsCheckCode,alertmessage)


