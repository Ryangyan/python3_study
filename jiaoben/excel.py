import xlrd
import xlwt 
import pandas as pd
from openpyxl import load_workbook

data = xlrd.open_workbook('C:/Users/56957/Desktop/houxiao.xls')
table = data.sheet_by_index(0)
ID=[]
for rowNum in range(1,table.nrows):
    ID.append(table.row_values(rowNum)[5])
ID_year=[]
ID_month=[]
ID_day=[]
for i in ID:
    ID_year.append(int(i[6:10]))
    ID_month.append(int(i[10:12]))
    ID_day.append(int(i[12:14]))

def age_judge(year,month,day):
    age=[]
    for i in range(len(ID_year)):
        if (ID_month[i]==month and ID_day[i]<=day):
            age.append(year-ID_year[i])
        else:
            age.append(year-ID_year[i]-1)
    return age

# =============================================================================
# age_judge(2021,6,2)
# =============================================================================

data=pd.DataFrame(age_judge(2021,6,2))
writer = pd.ExcelWriter('C:/Users/56957/Desktop/A.xlsx')
data.to_excel(writer, 'page_1', float_format='%.5f')
# =============================================================================
# table.save()
# table.close()
# =============================================================================
