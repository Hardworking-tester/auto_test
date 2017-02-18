#encoding:utf-8
import os
import sys,xlrd
from selenium.webdriver.common.by import By
from ..Data import ReadExcel,get_number_by_data
import OperateLoginElement
import time,OperateLoginElement
from  .. import db
from ..models import CaseDataDb,CaseInformationDb,ElementLocateDb
from ..resultlog import ResultLog
class LocateLoginObject():
    #该类主要是去获取登录功能中所用到的元素
    log=ResultLog.ResultLog()
    def getLocateObject(self,br,case_id):
        """根据测试用例id得到此测试用例对应的所有元素名称"""
        # login_object_list=db.session.query(ElementLocateDb.element_name).filter_by(case_id=case_id).all()
        login_object_list = db.session.query(ElementLocateDb.element_name).filter_by(case_id=case_id).order_by(ElementLocateDb.operate_index.asc()).all()
        for i in range(login_object_list.__len__()):
            login_object=login_object_list[i][0]
            self.log.info(login_object)
            self.getLocateMethodAndData(br,login_object,case_id)




    def getLocateMethodAndData(self,br,login_object,case_id):
        """根据需要定位的元素的名称得到需要定位的元素的定位方式以及定位数据"""

        old_how=db.session.query(ElementLocateDb.locate_method).filter_by(element_name=login_object).all()[0][0]
        # print old_how
        what=db.session.query(ElementLocateDb.locate_data).filter_by(element_name=login_object).all()[0][0]
        # print what
        #在这里增加一个字典是因为如果直接把By.ID写在数据库里的话，取出来不能用
        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}
        new_how=locate_method_dict[old_how]
        # print new_how
        self.locateElement(br,new_how,what,login_object,case_id)

    def locateElement(self,br,how,what,login_object,case_id):
        br=br
        # print br
        located_element=br.find_element(by=how,value=what)
        # print located_element
        # print "1111111111111"
        OperateLoginElement.OperateElement().operateElement(br,login_object,located_element,case_id)


