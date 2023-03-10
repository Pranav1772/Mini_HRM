#!C:\Users\Acer\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb,config,mysql.connector
cgitb.enable()

print("Context-Type:Text/html\n")
credentials=cgi.FieldStorage()
username=credentials.getvalue('username')
password=credentials.getvalue('password')

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)
dbcursor=conn.cursor()
dbcursor.execute("select * from users_master")

for x in dbcursor:
    if x[0]==username and x[1]==password:
        form=f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>HTML Meta Tag</title>
            <meta http-equiv = "refresh" content = "0; url = dashboard.py" />
        </head>
        <body>
        </body>
        </html>
        '''
        print(form)
        exit()

form=f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>HTML Meta Tag</title>
        <meta http-equiv = "refresh" content = "0; url = index.py" />
    </head>
    <body>
    <script>alert("Incorrect Username or Password")</script>
    </body>
    </html>'''
print(form)

