# encoding:utf-8
# author:wwg
from flask import *
from . import auto
from forms import FunctionModelsForm,CaseInformationForm,DataTestForm,ElementLocateForm,SubmitTestForm
from app.models import FunctionModelsDb,CaseInformationDb,CaseDataDb,ElementLocateDb,ResultTestDb
from .. import db
from . import auto
import uuid
from ..resultlog import ResultLog
from ..action import login
from ..Data import get_number_by_data
from selenium import webdriver
@auto.route('/addModels',methods=['GET','POST'])
def addFunctionModels():
    """新增功能模块视图"""
    form=FunctionModelsForm()
    if form.validate_on_submit():
        model=FunctionModelsDb(id=str(uuid.uuid4()).replace('-',''),name=form.model_name.data)
        form.model_name.data=''
        db.session.add(model)
        db.session.commit()

    return render_template('autotemplates/AddFunctionModel.html',form_html=form)

@auto.route('/',methods=['GET','POST'])
def index():
    """首页访问视图"""
    return render_template('autotemplates/index.html')


@auto.route('/queryModel',methods=['GET','POST'])
def queryModels():
    """查询功能模块视图"""
    query_model_name=db.session.query(FunctionModelsDb).all()
    return render_template('autotemplates/queryModel.html',model_names=query_model_name)


@auto.route('/addCase',methods=['GET','POST'])
def addCaseInformation():
    """新增测试用例视图"""
    form =CaseInformationForm()
    if form.validate_on_submit():
        id = str(uuid.uuid4()).replace('-', '')
        case_number=form.case_number.data
        case_summary=form.case_summary.data
        model_id_foreign=form.model_name.data
        case_info=CaseInformationDb(id=id,case_number=case_number,case_summary=case_summary,model_id=model_id_foreign)
        form.case_number.data=''
        form.case_summary.data = ''
        db.session.add(case_info)
        db.session.commit()
    return render_template('autotemplates/addCaseInformation.html', form_html=form)


@auto.route('/queryCaseInformation',methods=['GET','POST'])
def queryCaseInformation():
    """查询所有测试用例视图"""
    query_case_information=db.session.query(CaseInformationDb).all()
    return render_template('autotemplates/queryCaseInformation.html',case_informations=query_case_information)



@auto.route('/addTestData',methods=['GET','POST'])
def addTestData():
    """新增测试数据"""
    form =DataTestForm()
    if form.validate_on_submit():
        id = str(uuid.uuid4()).replace('-', '')
        key_data=form.data_key.data
        value_data=form.data_value.data
        case_id_foreign=form.case_id.data
        test_data=CaseDataDb(id=id,key=key_data,value=value_data,case_id=case_id_foreign)
        form.data_key.data=''
        form.data_value.data = ''
        db.session.add(test_data)
        db.session.commit()
    return render_template('autotemplates/addTestData.html', form_html=form)



@auto.route('/addElementLocate',methods=['GET','POST'])
def addElementLocate():
    """新增元素定位方式及操作方式视图"""
    form =ElementLocateForm()
    if form.validate_on_submit():
        id = str(uuid.uuid4()).replace('-', '')
        element_name=form.element_name.data
        locate_method=form.locate_method.data
        locate_data = form.locate_data.data
        element_introdution = form.element_introdution.data
        operate_method = form.operate_method.data
        case_id_foreign=form.case_id.data
        operate_index=form.operate_index.data
        test_data=ElementLocateDb(id=id,element_name=element_name,locate_method=locate_method,locate_data=locate_data,element_introdution=element_introdution,operate_index=operate_index,operate_method=operate_method,case_id=case_id_foreign)
        form.element_name.data=''
        form.locate_method.data = ''
        form.locate_data.data = ''
        form.element_introdution.data = ''
        form.operate_method.data = ''
        form.operate_index=''
        db.session.add(test_data)
        db.session.commit()
    return render_template('autotemplates/addElementLocate.html', form_html=form)



@auto.route('/executeTest',methods=['GET','POST'])
def executeTest():
    """执行测试"""
    query_case_information=db.session.query(CaseInformationDb).all()
    if request.method=="POST":


        for m in query_case_information:

            if request.form.get(str(m)) !=None:
                ResultLog.ResultLog().info(request.form.get(str(m)))
                case_id_list = db.session.query(CaseInformationDb.id).filter_by(case_number=request.form.get(str(m))).all()
                case_id= case_id_list[0][0]
                relation_dict = {'case_0001':'login.Login().testSuccessLogin(case_id)'}#把测试用例编号和对应的方法放到字典里
                function_name=relation_dict[request.form.get(str(m))]
                eval(function_name)
    return render_template('autotemplates/executeTest.html',case_informations=query_case_information)


@auto.route('/getResult',methods=['GET','POST'])
def getResult():
    """得到测试结果"""
    query_case_information=db.session.query(CaseInformationDb).all()
    if request.method=="POST":
        for m in query_case_information:
            if request.form.get(str(m)) !=None:
                ResultLog.ResultLog().info(request.form.get(str(m)))
                case_number=request.form.get(str(m))
                case_id_list = db.session.query(ResultTestDb.id).filter_by(case_number=case_number).all()
                result_list = db.session.query(ResultTestDb.id,ResultTestDb.case_number,ResultTestDb.Result_flag,ResultTestDb.case_summary,ResultTestDb.add_time,ResultTestDb.image_path).filter_by(case_number=case_number).all()
    return render_template('autotemplates/getResult.html',result_data=result_list)


@auto.route('/executeTest11',methods=['GET','POST'])
def executeTest11():
    form=SubmitTestForm()
    return redirect("http://www.baidu.com")