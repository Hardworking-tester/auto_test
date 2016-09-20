# encoding:utf-8
from selenium import webdriver
from ..Data import  ReadExcel,get_number_by_data
import time
from ..models import CaseDataDb,CaseInformationDb,ElementLocateDb
from .. import db
class OperateElement():


    def operateElement(self,br,login_object,located_element,case_id):
        """该函数作用就是去操作已经定位到的元素，操作方式为sendkey或者click """

        operate_method=db.session.query(ElementLocateDb.operate_method).filter_by(element_name=login_object).all()[0][0]
        # print login_object
        # print operate_method
        if operate_method=="click":
            located_element.click()
            time.sleep(2)
        elif operate_method=="sendkey" :
            # print located_element
            # print username
            # located_element.clear()
            send_data=db.session.query(CaseDataDb.value).filter_by(key=login_object).all()[0][0]
            # print send_data
            # print "2222222222222"
            located_element.send_keys(send_data)
            time.sleep(2)


