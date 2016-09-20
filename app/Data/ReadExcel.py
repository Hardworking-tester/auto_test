#encoding:utf-8
import xlrd
class ReadExcel():

    def getTableBySheetName(self,file_path,sheetname):
        """
        读取一个excel文件并返回该表格对象
        """
        data=xlrd.open_workbook(file_path)
        table=data.sheet_by_name(sheetname)
        return table
    def getDataByRowColIndex(self,file_path,sheetname,rowid,colid):
        data=xlrd.open_workbook(file_path)
        table=data.sheet_by_name(sheetname)
        cell_data=table.cell_value(rowid,colid)
        return cell_data



pp=ReadExcel()
pp.getTableBySheetName(r"G:\HuaYing\HuaYingData\login_data.xls","username_password_data")