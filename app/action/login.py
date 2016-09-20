# encoding:utf-8
# author:
from ..Data import  get_number_by_data
from ..Data import ReadExcel
from selenium import webdriver
import unittest
from time import sleep
import HTMLTestRunner
from ..Object import LocateLoginObject
from .. import db
from ..models import CaseDataDb
class Login():

    # def setUp(self):
    #     self.br=webdriver.Firefox()
    #     self.br.get("http://www.xnwmall.com")
    #     return self.br

    def getUsernameAndPasswordByCaseId(self,case_id):
        test_data=db.session.query(CaseDataDb.key,CaseDataDb.value).filter_by(case_id=case_id).all()
        return test_data
    def testSuccessLogin(self,case_id):
        br=webdriver.Firefox()
        br.get("http://sso.xnwmall.com/mall/login.shtml")
        # test_data=self.getUsernameAndPasswordByCaseId(case_id)
        LocateLoginObject.LocateLoginObject().getLocateObject(br,case_id)
        if br.current_url=='http://user.xnwmall.com/login/login.shtml':
            print u"登录成功，已进入会员中心"
            sleep(4)
        br.quit()
        # else:
        #     print u"登录失败"
        # self.br.get_screenshot_as_file("G:\\pyresult\\image_SuccessLogin.png")
        # print("image_SuccessLogin.png")

    # def testLoginByErrorPassword(self):
    #
    #     testCase_id="case_0003"
    #     print testCase_id
    #     username_password_data=self.getUsernameAndPasswordByCaseId(testCase_id)
    #     username=username_password_data[0]
    #     password=username_password_data[1]
    #     errorMessage=username_password_data[2]
    #     LocateLoginObject.LocateLoginObject().getLocateObject(self.br,username,password,errorMessage)
    #     if self.dealAlert(errorMessage):
    #         # print "password is false and errorMessage is right"
    #         print u"密码错误、提示语正确"
    #     else:
    #         # print "password is false and errorMessage is false"
    #         print u"密码错误，提示语也错误"
    #     self.br.get_screenshot_as_file("G:\\pyresult\\image_ERRORPassword.png")
    #     print("image_ERRORPassword.png")
    #
    # def testLoginByEmptyUsername(self):
    #
    #     testCase_id="case_0002"
    #     print testCase_id
    #     username_password_data=self.getUsernameAndPasswordByCaseId(testCase_id)
    #     username=username_password_data[0]
    #     password=username_password_data[1]
    #     errorMessage=username_password_data[2]
    #     LocateLoginObject.LocateLoginObject().getLocateObject(self.br,username,password,errorMessage)
    #     if self.dealAlert(errorMessage):
    #         # print "password is false and errorMessage is right"
    #         print u"登录名为空、提示语正确"
    #     else:
    #         # print "password is false and errorMessage is false"
    #         print u"登录名为空，提示语也错误"
    #     self.br.get_screenshot_as_file("G:\\pyresult\\image_EmptyUsername.png")
    #     print("image_EmptyUsername.png")
    #
    #
    # def testLoginByNotExistUsername(self):
    #
    #     testCase_id="case_0001"
    #     print testCase_id
    #     username_password_data=self.getUsernameAndPasswordByCaseId(testCase_id)
    #     username=username_password_data[0]
    #     password=username_password_data[1]
    #     errorMessage=username_password_data[2]
    #     LocateLoginObject.LocateLoginObject().getLocateObject(self.br,username,password,errorMessage)
    #     if self.dealAlert(errorMessage):
    #         # print "password is false and errorMessage is right"
    #         print u"账号不存在、提示语正确"
    #     else:
    #         # print "password is false and errorMessage is false"
    #         print u"登录账号不存在，提示语也错误"
    #     self.br.get_screenshot_as_file("G:\\pyresult\\image_NotExistUsername.png")
    #     print("image_NotExistUsername.png")
    #
    # def dealAlert(self,alertmessage):
    #     """处理错误信息"""
    #     #错误信息增加断言
    #     print (u"错误信息为：%s" %self.br.find_element_by_css_selector("span.text_error").text)
    #     print (u"预期错误信息为：%s" %alertmessage)
    #     if alertmessage==self.br.find_element_by_css_selector("span.text_error").text:
    #         return True
    #     else:
    #         return False

    # def tearDown(self):
    #     self.br.close()
