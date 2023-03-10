#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb,config,mysql.connector
cgitb.enable()
print("Context-Type:Text/html\n")

form_input=cgi.FieldStorage()


name=form_input.getvalue("name")
id=form_input.getvalue("id")
gender=form_input.getvalue("gender")
designation=form_input.getvalue("designation")
department=form_input.getvalue("department")
pmobileno=form_input.getvalue("pmobileno")
typeemployment=form_input.getvalue("typeemployment")
email=form_input.getvalue("email")
gs=form_input.getvalue("gs")
bs=form_input.getvalue("bs")
hra=form_input.getvalue("hra")
da=form_input.getvalue("da")
fa=form_input.getvalue("fa")
ma=form_input.getvalue("ma")
te=form_input.getvalue("te")
pt=form_input.getvalue("pt")
pf=form_input.getvalue("pf")
td=form_input.getvalue("td")
ns=form_input.getvalue("ns")

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)



dbcursor=conn.cursor()
dbcursor.execute("update payroll set name='"+name+"',gender='"+gender+"',designation='"+designation+"',department='"+department+"',pmobileno='"+pmobileno+"',typeemployment='"+typeemployment+"',email='"+email+"',gross_salary='"+gs+"',bs='"+bs+"',hra='"+hra+"',da='"+da+"',fa='"+fa+"',ma='"+ma+"',te='"+te+"',pt='"+pt+"',pf='"+pf+"',td='"+td+"',ns='"+ns+"' where id="+str(id))
conn.commit()

if dbcursor.rowcount==1:
  form=f'''
          <!DOCTYPE html>
          <html>
          <head>
              <title>HTML Meta Tag</title>
              <meta http-equiv = "refresh" content = "0; url = dashboard.py"/>
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
              <meta http-equiv = "refresh" content = "0; url = EditPayroll2.py" />
          </head>
          <body>
          <script>alert("Something Went Wrong")</script>
          </body>
          </html>
          '''
  print(form)