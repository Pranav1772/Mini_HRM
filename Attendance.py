#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb,config,mysql.connector
cgitb.enable()

from datetime import datetime 
import calendar
from datetime import date
from calendar import monthrange


  
todays_date = date.today()

months=todays_date.month
if months==1:
    month=12
else:
    month=months-1

years=todays_date.year
if months==1:
    year=years-1
else:
    year=years

num_days = monthrange(year, month)[1] 

TotalSundays = len([1 for i in calendar.monthcalendar(datetime.now().year,datetime.now().month-1) if i[6] != 0])                                  

totalworkingdays=num_days-TotalSundays





print("Context-Type:Text/html\n")

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)
dbcursor=conn.cursor()
dbcursor.execute("select * from employee_details;")
result=dbcursor.fetchall()


cssfiles='''<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback"><link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css"><link rel="stylesheet" href="plugins/datatables-bs4/css/dataTables.bootstrap4.min.css"><link rel="stylesheet" href="plugins/datatables-responsive/css/responsive.bootstrap4.min.css"><link rel="stylesheet" href="plugins/datatables-buttons/css/buttons.bootstrap4.min.css"><link rel="stylesheet" href="dist/css/adminlte.min.css">'''

config.useHeader(" Attendance",cssfiles)

print('''
    <form action="Attendance_backend.py" method="post">
  <div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <section class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1> Add Attendance</h1>
          </div>
          <div class="col-sm-6">
            <ol class="breadcrumb float-sm-right">
              <li class="breadcrumb-item"><a href="#">Home</a></li>
              <li class="breadcrumb-item active">Company Details List</li>
            </ol>
          </div>
        </div>
      </div><!-- /.container-fluid -->
    </section>

    <!-- Main content -->
    <section class="content">
        <div class="container-fluid">
          <div class="row">
            <div class="col-12">
              <div class="card">
              <div class="card-header">
                <h3 class="card-title">Fixed Header Table</h3>

                <div class="card-tools">
                  <div class="input-group input-group-sm" style="width: 150px;">
                    <input type="text" name="table_search" class="form-control float-right" placeholder="Search">

                    <div class="input-group-append">
                      <button type="submit" class="btn btn-default">
                        <i class="fas fa-search"></i>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              <!-- /.card-header -->
              <div class="card-body table-responsive p-0" style="height: 465px;">
                <table class="table table-head-fixed table-hover text-nowrap">
                  <thead>
                  <tr>
                    <th>id</th>
                    <th>Employee Name</th>
                    <th>Year</th>
                    <th>Month</th>
                    <th>Total Days In Month</th>
                    <th>Total Working Days </th>
                    <th>Total Present Days</th>    
                        
                    
                  </tr>
                  </thead>''')
for x in result:
  print('''       <tbody>
                  <tr>
                        
                    <td > <div class="row"><div class="col-60"><input type="text" class="form-control" name="id_list[]"  value="'''+str(x[0])+'''" readonly ></div> </div></td>
                    <td > <div class="row"><div class="col-100"><input type="text" class="form-control" name="employeename[]" value="'''+str(x[1]) + str(x[3])+'''" readonly ></div> </div></td>
                    <td > <div class="row"><div class="col-20"><input type="text" class="form-control" name="year[]" value="'''+str(year)+'''" readonly ></div> </div></td>
                    <td > <div class="row"><div class="col-20"><input type="text" class="form-control" name="month[]" value="'''+str(month)+'''" readonly ></div> </div></td>
                    <td > <div class="row"><div class="col-20"><input type="text" class="form-control" name="num_days[]" value="'''+str(num_days)+'''" readonly ></div> </div></td>
                    <td > <div class="row"><div class="col-20"><input type="text" class="form-control" name="totalworkingdays[]" value="'''+str(totalworkingdays)+'''" readonly ></div> </div></td>
                    <td > <div class="row"><div class="col-20"><input type="text" class="form-control" name="totalpresentdays[]" name="totalpresentdays[]" ></div> </div></td>
                               
                       
                  </tr>                  
                  </tbody>''')
print('''                                           
                  </tr>
                  </tfoot>
                </table>
              
              </div>
              <!-- /.card-body -->
            </div>
            <!-- /.card -->
          </div>
          <!-- /.col -->
          
          <div class="col-sm-12">
            <div class="form-group" align="Right">
              <button type="submit" class="btn btn-primary col-sm-4">submit Attendance</button>
            </div>
          </div>
          
          
          
        </div>
        <!-- /.row -->
      </div>
      <!-- /.container-fluid -->
    </section>
    
    <!-- /.content -->
  </div>
  </form>''')

jsfiles='''<script src="plugins/jquery/jquery.min.js"></script><script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script><script src="plugins/datatables/jquery.dataTables.min.js"></script><script src="plugins/datatables-bs4/js/dataTables.bootstrap4.min.js"></script><script src="plugins/datatables-responsive/js/dataTables.responsive.min.js"></script><script src="plugins/datatables-responsive/js/responsive.bootstrap4.min.js"></script><script src="plugins/datatables-buttons/js/dataTables.buttons.min.js"></script><script src="plugins/datatables-buttons/js/buttons.bootstrap4.min.js"></script><script src="plugins/jszip/jszip.min.js"></script><script src="plugins/pdfmake/pdfmake.min.js"></script><script src="plugins/pdfmake/vfs_fonts.js"></script><script src="plugins/datatables-buttons/js/buttons.html5.min.js"></script><script src="plugins/datatables-buttons/js/buttons.print.min.js"></script><script src="plugins/datatables-buttons/js/buttons.colVis.min.js"></script><script src="dist/js/adminlte.min.js"></script><script src="dist/js/demo.js"></script>'''

script='''<script>$(function(){$("#example1").DataTable({responsive:!0,lengthChange:!1,autoWidth:!1,buttons:["copy","csv","excel","pdf","print","colvis"]}).buttons().container().appendTo("#example1_wrapper .col-md-6:eq(0)"),$("#example2").DataTable({paging:!0,lengthChange:!1,searching:!1,ordering:!0,info:!0,autoWidth:!1,responsive:!0})})</script>'''


config.useFooter(jsfiles,script)