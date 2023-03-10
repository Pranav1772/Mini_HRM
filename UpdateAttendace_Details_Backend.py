#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb,config,mysql.connector,requests
cgitb.enable()

print("Context-Type:Text/html\n")

form1=cgi.FieldStorage()



id_list=form1.getvalue("id_list[]")
employeename=form1.getvalue("employeename[]")
year=form1.getvalue("year[]")
month=form1.getvalue("month[]")
num_days=form1.getvalue("num_days[]")
totalworkingdays=form1.getvalue("totalworkingdays[]")
totalpresentdays=form1.getvalue("totalpresentdays[]")

y = len(id_list)

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)

for x in range(y):
    #print(x)
    #print(employeename[x])
    
    dbcursor=conn.cursor()
    dbcursor.execute("update attendance_details set  totalpresentdays='"+(totalpresentdays[x])+"' where id_list='"+(id_list[x])+"';")
    conn.commit()


form=f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>HTML Meta Tag</title>
            <meta http-equiv = "refresh" content = "0; url = UpdateAttendace.py" />
        </head>
        <body>
        <script>alert("attendance Update Successfully")</script>
        </body>
        </html>
        '''
print(form)
exit()