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
dbcursor.execute("select * from users_master")
results=dbcursor.fetchall() 

cssfiles='''<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback"><link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css"><link rel="stylesheet" href="plugins/datatables-bs4/css/dataTables.bootstrap4.min.css"><link rel="stylesheet" href="plugins/datatables-responsive/css/responsive.bootstrap4.min.css"><link rel="stylesheet" href="plugins/datatables-buttons/css/buttons.bootstrap4.min.css"><link rel="stylesheet" href="dist/css/adminlte.min.css">'''

config.useHeader("Users List",cssfiles)
print('''
  <div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <section class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1> Users List</h1>
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
                    <th>Actions</th>
                    <th>Employee ID</th>
                    <th>Employee Name</th>
                    <th>Employee Email</th>   
                    <th>Role</th>   
                    <th>Status</th>            
                  </tr>
                  </thead>''')
for x in results:
  print('''       <tbody>
                  <tr>                    
                    <td>                      
                      <div class="row">                          
                        <div class="col-12">
                          <a href="UpdateUsers.py?id='''+str(x[2])+'''">                              
                            <button type="submit" class="btn btn-outline-warning btn-block btn-sm">Edit User</button>
                          </a>
                          <br>  
                          <a href="DeleteUserDetails.py?id='''+str(x[2])+'''">                              
                            <button type="submit" class="btn btn-outline-danger btn-block btn-sm">Delete User</button>
                          </a>                           
                        </div>
                      </div>                       
                    </td>
                    <td>'''+str(x[2])+'''</td>
                    <td>'''+str(x[3])+'''</td>
                    <td>'''+str(x[0])+'''</td>
                    <td>'''+str(x[4])+'''</td>
                    <td>'''+str(x[5])+'''</td>
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