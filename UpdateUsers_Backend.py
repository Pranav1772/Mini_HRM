#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb,config,mysql.connector,requests
cgitb.enable()

print("Context-Type:Text/html\n")
form_inputs=cgi.FieldStorage()
id=form_inputs.getvalue('id')
name=form_inputs.getvalue('name')
email=form_inputs.getvalue('email')
password=form_inputs.getvalue('password')
status=form_inputs.getvalue('status')
role=form_inputs.getvalue('role')

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)
dbcursor=conn.cursor()
dbcursor.execute("update users_master set username='"+email+"',password='"+password+"',id='"+id+"',name='"+name+"',role='"+role+"',status='"+status+"' where id='"+str(id)+"';")
conn.commit()

if dbcursor.rowcount==1:
  form=f'''
          <!DOCTYPE html>
          <html>
          <head>
              <title>Redirecting</title>
              <meta http-equiv = "refresh" content = "0; url = UsersList.py" />
          </head>
          <body>
          print('<script>alert("Record updated Successfully")</script>')
          </body>
          </html>'''
  print(form)
else:
  form=f'''
          <!DOCTYPE html>
          <html>
          <head>
              <title>Redirecting</title>
              <meta http-equiv = "refresh" content = "0; url = UsersList.py" />
          </head>
          <body>
          <script>alert("Something Went Wrong")</script>
          </body>
          </html>
          '''
  print(form)