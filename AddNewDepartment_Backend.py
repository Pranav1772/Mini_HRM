#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb,config,mysql.connector
cgitb.enable()

print("Context-Type:Text/html\n")
form_inputs=cgi.FieldStorage()
dept_code=form_inputs.getvalue('dept_code')
dept_name=form_inputs.getvalue('dept_name')
dept_email=form_inputs.getvalue('dept_email')
dept_no=form_inputs.getvalue('dept_no')
dept_opening_date=form_inputs.getvalue('dept_opening_date')
dept_hd_fname=form_inputs.getvalue('dept_hd_fname')
dept_hd_lname=form_inputs.getvalue('dept_hd_lname')
dept_hd_email=form_inputs.getvalue('dept_hd_email')
dept_hd_no=form_inputs.getvalue('dept_hd_no')
company_name=form_inputs.getvalue('company_name')

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)

dbcursor=conn.cursor()
dbcursor.execute("insert into department_details values('"+dept_code+"','"+dept_name+"','"+dept_email+"','"+dept_no+"','"+dept_opening_date+"','"+dept_hd_fname+"','"+dept_hd_lname+"','"+dept_hd_email+"','"+dept_hd_no+"','"+company_name+"');")
conn.commit()
if dbcursor.rowcount==1:
  form=f'''
          <!DOCTYPE html>
          <html>
          <head>
              <title>HTML Meta Tag</title>
              <meta http-equiv = "refresh" content = "0; url = CompanyDetailsList.py" />
          </head>
          <body>
          print('<script>alert("Record inserted Successfully")</script>')
          </body>
          </html>'''
  print(form)
else:
  form=f'''
          <!DOCTYPE html>
          <html>
          <head>
              <title>HTML Meta Tag</title>
              <meta http-equiv = "refresh" content = "0; url = AddNewCOmpany.py" />
          </head>
          <body>
          <script>alert("Something Went Wrong")</script>
          </body>
          </html>
          '''
  print(form)