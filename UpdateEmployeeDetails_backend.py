#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe
import cgi
import mysql.connector
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")


form=cgi.FieldStorage()

id=form.getvalue('id')
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





conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)

dbcursor=conn.cursor()

if conn.is_connected():    
    dbcursor.execute("UPDATE employee_details set fname='"+fname+"',mname='"+mname+"',lname='"+lname+"',faname='"+faname+"',moname='"+moname+"',birthdate='"+birthdate+"',gender='"+gender+"',spname='"+spname+"',nationality='"+nationality+"',maritalstatus='"+maritalstatus+"',addressarea='"+addressarea+"',locality='"+locality+"',pincode='"+pincode+"',district='"+district+"',state='"+state+"',pmobileno='"+pmobileno+"',smobileno='"+smobileno+"',bankname='"+bankname+"',bankbranchname='"+bankbranchname+"',ifsccode='"+ifsccode+"',bankaccount='"+bankaccount+"',panno='"+panno+"',una='"+una+"',employment='"+employment+"',education='"+education+"',aadharcardno='"+aadharcardno+"',markofident='"+markofident+"',inputdata='"+inputdata+"',enddate='"+enddate+"',email='"+email+"',designation='"+designation+"',department='"+department+"' where id='"+id+"';")       
    conn.commit()
    form=f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>HTML Meta Tag</title>
            <meta http-equiv = "refresh" content = "0; url = EmployeeDetailsList.py" />
        </head>
        <body>
        <script>alert("Record inserted Successfully")</script>
        </body>
        </html>
        '''
    print(form)
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
        <script>alert("Something went wrong")</script>
        </body>
        </html>
        '''
    print(form)