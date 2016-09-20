# encoding:utf-8
import xlrd
class GetRowAndColNumber():
    def getRowAndColNumber(self,excel_path,sheet_name,key):
        """该函数的作用：通过参数sheet_name和key，去返回一个该key所在行号和列号的列表"""
        row_col_list=[]
        data=xlrd.open_workbook(excel_path)
        table=data.sheet_by_name(sheet_name)
        rows=table.nrows
        cols=table.ncols
        for r in range(rows):
            for c in range(cols):
                if table.cell_value(r,c)==key:
                    row_col_list.append(r)
                    row_col_list.append(c)
                    # print row_col_list
                    # print table.cell_value(r,c)
                    return row_col_list












# pp=GetRowAndColNumber()
# pp.getRowAndColNumber(r"G:\HuaYing\HuaYingData\login_data.xls","username_password_data","case_0004")