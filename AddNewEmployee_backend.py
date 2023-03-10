#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe
import cgi
import mysql.connector
import cgitb
import os
cgitb.enable()
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
fname=form.getvalue("fname")
mname=form.getvalue("mname")
lname=form.getvalue("lname")
faname=form.getvalue("faname")
moname=form.getvalue("moname")
birthdate=form.getvalue("birthdate")
gender=form.getvalue("gender")
spname=form.getvalue("spname")
nationality=form.getvalue("nationality")
maritalstatus=form.getvalue("maritalstatus")
addressarea=form.getvalue("addressarea")
locality=form.getvalue("locality")
pincode=form.getvalue("pincode")
district=form.getvalue("district")
state=form.getvalue("state")
pmobileno=form.getvalue("pmobileno")
smobileno=form.getvalue("smobileno")
bankname=form.getvalue("bankname")
bankbranchname=form.getvalue("bankbranchname")
ifsccode=form.getvalue("ifsccode")
bankaccount=form.getvalue("bankaccount")
panno=form.getvalue("panno")
una=form.getvalue("una")
employment=form.getvalue("employment")
education=form.getvalue("education")
aadharcardno=form.getvalue("aadharcardno")
markofident=form.getvalue("markofiden")
inputdata=form.getvalue("inputdata")
enddate=form.getvalue("enddate")
email=form.getvalue("email")
designation=form.getvalue("designation")
department=form.getvalue("department")
print(form)
print(department)
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)
dbcursor=conn.cursor()

fi=form['emp_photo']
uploadFileName=""
print(fi)
if fi.filename:
	# This code will strip the leading absolute path from your file-name
	fn =os.path.splitext(fi.filename)
	ext =os.path.splitext(fi.filename)
	#print(ext[0])
	uploadFileName='emp_photo'+str(fname)+ext[1]
	#print(uploadFileName)
	# open for reading & writing the file into the server
	open(uploadFileName, 'wb').write(fi.file.read())
	#print('file uploaded')
else:
    print('file not uploaded')





if conn.is_connected():
    
    query="insert into employee_details (fname,mname,lname,faname,moname,birthdate,gender,spname,nationality,maritalstatus,addressarea,locality,pincode,district,state,pmobileno,smobileno,bankname,bankbranchname,ifsccode,bankaccount,panno,una,employment,education,aadharcardno,markofident,inputdata,enddate,email,designation,department,emp_photo)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
   
    
    val=(fname,mname,lname,faname,moname,birthdate,gender,spname,nationality,maritalstatus,addressarea,locality,pincode,district,state,pmobileno,smobileno,bankname,bankbranchname,ifsccode,bankaccount,panno,una,employment,education,aadharcardno,markofident,inputdata,enddate,email,designation,department,uploadFileName)
    dbcursor.execute(query,val)
    form=f'''
            <!DOCTYPE html>
        <html>
        <head>
            <title>HTML Meta Tag</title>
            <meta http-equiv = "refresh" content = "0; url = AddNewEmployee.py" />
        </head>
        <body>
        <script>alert("Record inserted Successfully")</script>
        </body>
        </html>
        '''
    print(form)
    
    conn.commit()
else :
    print(dbcursor.etchwarnings(),'-error list')
    
    form=f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>HTML Meta Tag</title>
            <meta http-equiv = "refresh" content = "0; url = AddNewEmployee.py" />
        </head>
        <body>
        <script>alert("Record inserted Successfully")</script>
        </body>
        </html>
        '''
    print(form)












