#coding:utf-8

import xlrd

path = r'C:\Users\Administrator\Desktop\test'
file = '大亚湾电子政务网络DHCPv6规划表v2.0-20200427.xlsx'
#打开文件
data = xlrd.open_workbook(path + '/' + file)
#获取sheet表格数
sheet_nums = len(data.sheets())
#
for i in range(sheet_nums):
    sheet1 = data.sheets()[i]
    #sheet2 = data.sheet_by_name('IPV6地址规划')
rows = sheet1.nrows
cols = sheet1.ncols
#print(rows,cols)
for i in range(rows):
    print(','.join(sheet1.row_values(i)))
