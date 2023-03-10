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
did=cgi.FieldStorage().getvalue('id')
dbcursor=conn.cursor()
dbcursor.execute("delete from employee_details where id='"+did+"'")
conn.commit()
if dbcursor.rowcount==1:
  form=f'''
          <!DOCTYPE html>
          <html>
          <head>
              <title>HTML Meta Tag</title>
              <meta http-equiv = "refresh" content = "0; url = EmployeeDetailsList.py" />
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
              <meta http-equiv = "refresh" content = "0; url = EmployeeDetailsList.py" />
          </head>
          <body>
          <script>alert("Something Went Wrong")</script>
          </body>
          </html>
          '''
  print(form)