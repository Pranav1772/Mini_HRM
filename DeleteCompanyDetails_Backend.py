#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb,config,mysql.connector
cgitb.enable()

print("Context-Type:Text/html\n")
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)

cmp_reg_id=cgi.FieldStorage().getvalue('cmp_reg_id')
dbcursor=conn.cursor()
dbcursor.execute("delete from company_details where cmp_reg_id='"+cmp_reg_id+"'")
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
          print('<script>alert("Record deleted Successfully")</script>')
          </body>
          </html>'''
  print(form)
else:
  form=f'''
          <!DOCTYPE html>
          <html>
          <head>
              <title>HTML Meta Tag</title>
              <meta http-equiv = "refresh" content = "0; url = CompanyDetailsList.py" />
          </head>
          <body>
          <script>alert("Something Went Wrong")</script>
          </body>
          </html>
          '''
  print(form)