# encoding:utf-8
# author:wwg
from flask_wtf import Form
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import *
from ..models import CaseInformationDb,FunctionModelsDb
class FunctionModelsForm(Form):
    model_name=StringField(u'请输入功能模块名称',validators=[Required()])
    submit = SubmitField(u'提交')


class CaseInformationForm(Form):
    case_number=StringField(u'请输入测试用例编号',validators=[Required()])
    case_summary=StringField(u'请输入测试用例概述',validators=[Required()])
    model_name=SelectField(u'所属功能模块')
    submit = SubmitField(u'提交')
    def __init__(self,*args, **kwargs):
        super(CaseInformationForm, self).__init__(*args, **kwargs)
        self.model_name.choices = [(FunctionModels.id, FunctionModels.name)
                             for FunctionModels in FunctionModelsDb.query.all()]
