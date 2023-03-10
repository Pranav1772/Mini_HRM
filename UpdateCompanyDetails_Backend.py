#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb,config,mysql.connector,requests
cgitb.enable()

print("Context-Type:Text/html\n")
form_inputs=cgi.FieldStorage()
cmp_reg_id=form_inputs.getvalue('cmp_reg_id')
cmp_name=form_inputs.getvalue('cmp_name')
cmp_email=form_inputs.getvalue('cmp_email')
cmp_no=form_inputs.getvalue('cmp_no')
cmp_reg_date=form_inputs.getvalue('cmp_reg_date')
cmp_logo=form_inputs.getvalue('cmp_logo')
cmp_gst_no=form_inputs.getvalue('cmp_gst_no')
cmp_type=form_inputs.getvalue('cmp_type')
cmp_bnk_name=form_inputs.getvalue('cmp_bnk_name')
cmp_bnk_brn_name=form_inputs.getvalue('cmp_bnk_brn_name')
cmp_bnk_ifsc_code=form_inputs.getvalue('cmp_bnk_ifsc_code')
cmp_bnk_acc_no=form_inputs.getvalue('cmp_bnk_acc_no')
cmp_addr=form_inputs.getvalue('cmp_addr')
cmp_locality=form_inputs.getvalue('cmp_locality')
cmp_pincode=form_inputs.getvalue('cmp_pincode')
cmp_district=form_inputs.getvalue('cmp_district')
cmp_state=form_inputs.getvalue('cmp_state')
cmp_own_fname=form_inputs.getvalue('cmp_own_fname')
cmp_own_lname=form_inputs.getvalue('cmp_own_lname')
cmp_own_email=form_inputs.getvalue('cmp_own_email')
cmp_own_no=form_inputs.getvalue('cmp_own_no')

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)
dbcursor=conn.cursor()
dbcursor.execute("update company_details set cmp_reg_id='"+cmp_reg_id+"',cmp_name='"+cmp_name+"',cmp_email='"+cmp_email+"',cmp_no='"+cmp_no+"',cmp_reg_date='"+cmp_reg_date+"',cmp_logo='"+cmp_logo+"',cmp_gst_no='"+cmp_gst_no+"',cmp_type="+cmp_type+",cmp_bnk_name='"+cmp_bnk_name+"',cmp_bnk_brn_name='"+cmp_bnk_brn_name+"',cmp_bnk_ifsc_code='"+cmp_bnk_ifsc_code+"',cmp_bnk_acc_no='"+cmp_bnk_acc_no+"',cmp_addr='"+cmp_addr+"',cmp_locality='"+cmp_locality+"',cmp_pincode='"+cmp_pincode+"',cmp_district="+cmp_district+",cmp_state="+cmp_state+",cmp_own_fname='"+cmp_own_fname+"',cmp_own_lname='"+cmp_own_lname+"',cmp_own_email='"+cmp_own_email+"',cmp_own_no='"+cmp_own_no+"' where cmp_reg_id='"+cmp_reg_id+"';")
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
          print('<script>alert("Record updated Successfully")</script>')
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