import xlwt
import pymysql

_host = '127.0.0.1'
_db = 'ABA'
_user = 'aba_django'
_password = 'aba_django'
_table = 'webapp_program'
_excel_name = 'excel_sheet'

conn = pymysql.connect(host=_host, user=_user, password=_password, db=_db, charset='utf8')
cursor = conn.cursor()
count = cursor.execute('SELECT id, name, created_date FROM %s' % _table)
print('has %s line' % count)

cursor.scroll(0, mode='absolute')
ret = cursor.fetchall()
fields = cursor.description
excel = xlwt.Workbook()
sheet = excel.add_sheet(_excel_name, cell_overwrite_ok=True)

for k, v in enumerate(fields):
    sheet.write(0, k, v[0])

for key, value in enumerate(ret):
    for kk, vv in enumerate(value):
        sheet.write(key + 1, kk, vv)

excel.save('./%s.xlsx' % _excel_name)
