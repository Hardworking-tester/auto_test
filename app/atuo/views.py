# encoding:utf-8
# author:wwg
from flask import *
from . import auto
from forms import FunctionModelsForm,CaseInformationForm
from app.models import FunctionModelsDb,CaseInformationDb
from .. import db
from . import auto
import uuid
import uuid
@auto.route('/addModels',methods=['GET','POST'])
def addFunctionModels():
    form=FunctionModelsForm()
    if form.validate_on_submit():
        model=FunctionModelsDb(id=str(uuid.uuid4()).replace('-',''),name=form.model_name.data)
        form.model_name.data=''
        db.session.add(model)
        db.session.commit()

    return render_template('autotemplates/AddFunctionModel.html',form_html=form)

@auto.route('/',methods=['GET','POST'])
def index():
    return render_template('autotemplates/index.html')


@auto.route('/queryModel',methods=['GET','POST'])
def queryModels():
    query_model_name=FunctionModelsDb().query.all()
    return render_template('autotemplates/queryModel.html',model_names=query_model_name)


@auto.route('/addCase',methods=['GET','POST'])
def addCaseInformation():
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