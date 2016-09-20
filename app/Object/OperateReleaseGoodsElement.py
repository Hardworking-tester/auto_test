# encoding:utf-8
from selenium import webdriver
from HuaYingData import  ReadExcel,get_number_by_data
import time
class OperateReleaseGoodsElement():


    def operateElement(self,br,object_name,located_element,send_data):
        """该函数作用就是去操作已经定位到的元素，操作方式为sendkey或者click """
        releaseGoods_excel_path=r"G:\HuaYing\HuaYingData\registerByPhoneNumber_data.xls"
        releaseGoods_operate_sheet=ReadExcel.ReadExcel().getTableBySheetName(releaseGoods_excel_path,"operate_method")
        row_col_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(releaseGoods_excel_path,"operate_method",object_name)
        operate_method=releaseGoods_operate_sheet.cell_value(row_col_index[0],row_col_index[1]+1)
        # print operate_method
        # print object_name
        if operate_method=="click":
            located_element.click()
            time.sleep(2)
        elif operate_method=="sendkey" and object_name=="phoneName":
            # print located_element
            # print username
            located_element.clear()
            located_element.send_keys(phoneNumber)

            time.sleep(2)
        elif operate_method=="sendkey" and object_name=="firstpassword":
            located_element.send_keys(firstPassword)
            # print password
            time.sleep(2)

        elif operate_method=="sendkey" and object_name=="secondpassword":
            located_element.send_keys(secondPassword)
            # print password
            time.sleep(2)

        elif operate_method=="sendkey" and object_name=="picturecheckcode":
            located_element.send_keys(pictureCheckCode)
            # print password
            time.sleep(2)
        elif operate_method=="sendkey" and object_name=="smscheckcode":
            located_element.send_keys(smsCheckCode)
            # print password
            time.sleep(2)
