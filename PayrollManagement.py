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
dbcursor=conn.cursor()
dbcursor.execute("select * from employee_details;")
result=dbcursor.fetchall()
cssfiles='''<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback"><link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css"><link rel="stylesheet" href="plugins/datatables-bs4/css/dataTables.bootstrap4.min.css"><link rel="stylesheet" href="plugins/datatables-responsive/css/responsive.bootstrap4.min.css"><link rel="stylesheet" href="plugins/datatables-buttons/css/buttons.bootstrap4.min.css"><link rel="stylesheet" href="dist/css/adminlte.min.css">'''

config.useHeader("Payroll Management",cssfiles)
print('''
  <div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <section class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1>Payroll Management</h1>
          </div>
          <div class="col-sm-6">
            <ol class="breadcrumb float-sm-right">
              <li class="breadcrumb-item"><a href="#">Home</a></li>
              <li class="breadcrumb-item active">Employee Details List</li>
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
                    <th>Actions</th>
                    <th>ID</th>
                    <th>NAME</th>                    
                    <th>GENDER</th>                    
                    <th>DESIGNATION</th> 
                    <th>DEPARTMENT</th>                    
                    <th>PRIMARY MOBILE NO:</th>                  
                    <th>TYPE OF EMPLOYMENT</th>                    
                    <th>MAIL</th>                    
                  </tr>
                  </thead>''')
for x in result:
  print('''<tbody>
                  <tr>                    
                    <td>                      
                      <div class="row">                          
                        <div class="col-12">
                          <a href="AddPayrollManagement.py?id='''+str(x[0])+'''">                      
                            <button type="submit" class="btn btn-outline-primary btn-block btn-sm">Add Payroll</button>
                          </a> 
                          <br>
                          <a href="EditPayroll.py?id='''+str(x[0])+'''">
                            <button type="submit" class="btn btn-outline-warning btn-block btn-sm">Edit Payroll</button>
                          </a>
                          <br>
                          <a href="Payslip.py?id='''+str(x[0])+'''">
                            <button type="submit" class="btn btn-outline-success btn-block btn-sm">Payslip </button>
                          </a>
                        </div>
                      </div>                       
                    </td>
                      <td>'''+str(x[0])+'''</td>
                      <td>'''+str(x[1])+" "+str(x[2])+" "+str(x[3])+'''</td>                      
                      <td>'''+str(x[7])+'''</td>                      
                      <td>'''+str(x[31])+'''</td>                      
                      <td>'''+str(x[32])+'''</td>                      
                      <td>'''+str(x[16])+'''</td>                      
                      <td>'''+str(x[24])+'''</td>                      
                      <td>'''+str(x[30])+'''</td>                                                  
                  </tr>                  
                  </tbody>''')
print('''         
                </table>
              
              </div>
              <!-- /.card-body -->
            </div>
            <!-- /.card -->
          </div>
          <!-- /.col -->
        </div>
        <!-- /.row -->
      </div>
      <!-- /.container-fluid -->
    </section>
    <!-- /.content -->
  </div>''')

jsfiles='''<script src="plugins/jquery/jquery.min.js"></script><script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script><script src="plugins/datatables/jquery.dataTables.min.js"></script><script src="plugins/datatables-bs4/js/dataTables.bootstrap4.min.js"></script><script src="plugins/datatables-responsive/js/dataTables.responsive.min.js"></script><script src="plugins/datatables-responsive/js/responsive.bootstrap4.min.js"></script><script src="plugins/datatables-buttons/js/dataTables.buttons.min.js"></script><script src="plugins/datatables-buttons/js/buttons.bootstrap4.min.js"></script><script src="plugins/jszip/jszip.min.js"></script><script src="plugins/pdfmake/pdfmake.min.js"></script><script src="plugins/pdfmake/vfs_fonts.js"></script><script src="plugins/datatables-buttons/js/buttons.html5.min.js"></script><script src="plugins/datatables-buttons/js/buttons.print.min.js"></script><script src="plugins/datatables-buttons/js/buttons.colVis.min.js"></script><script src="dist/js/adminlte.min.js"></script><script src="dist/js/demo.js"></script>'''

script='''<script>$(function(){$("#example1").DataTable({responsive:!0,lengthChange:!1,autoWidth:!1,buttons:["copy","csv","excel","pdf","print","colvis"]}).buttons().container().appendTo("#example1_wrapper .col-md-6:eq(0)"),$("#example2").DataTable({paging:!0,lengthChange:!1,searching:!1,ordering:!0,info:!0,autoWidth:!1,responsive:!0})})</script>'''


config.useFooter(jsfiles,script)