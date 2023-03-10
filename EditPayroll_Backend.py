#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb,config,mysql.connector
from pprint import pformat
from math import fabs
from dataclasses import dataclass
from statistics import harmonic_mean
from logging import basicConfig
from email.mime import base
from lib2to3.pgen2 import grammar
cgitb.enable()
print("Context-Type:Text/html\n")

form_input=cgi.FieldStorage()


idi=form_input.getvalue("id")
gross_salary=form_input.getvalue("gross_salary")



conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)



dbcursor=conn.cursor()
dbcursor.execute("update payroll set gross_salary='"+gross_salary+"' where id='"+idi+"';")
conn.commit()




if dbcursor.rowcount==1:
  form=f'''
          <!DOCTYPE html>
          <html>
          <head>
              <title>HTML Meta Tag</title>
              <meta http-equiv = "refresh" content = "0; url = EditPayroll2.py?id='''+str(idi)+'''" />
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
              <meta http-equiv = "refresh" content = "0; url = EditPayroll.py" />
          </head>
          <body>
          <script>alert("Something Went Wrong")</script>
          </body>
          </html>
          '''
  print(form)