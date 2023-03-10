#!C:\Users\Acer\AppData\Local\Programs\Python\Python310\python.exe

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

config.useHeader("Employee Details List",cssfiles)
print('''
  <div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <section class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1>Employee Details List</h1>
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
                    <th>id</th>
                    <th>FIRST NAME</th>
                    <th>MIDDLE NAME</th>
                    <th>LAST NAME</th>
                    <th>FATHER NAME</th>
                    <th>MOTHER NAME</th>
                    <th>BIRTH DATE</th>
                    <th>GENDER</th>
                    <th>SPOUSE NAME</th>
                    <th>NATIONALITY</th>
                    <th>MARITAL STATUS</th>
                    <th>DESIGNATION</th> 
                    <th>DEPARTMENT</th>
                    <th>Address(Area and Street)</th>
                    <th>Locality</th>
                    <th>Pincode</th>
                    <th>District</th>
                    <th>State</th>
                    <th>PRIMARY MOBILE NO:</th>
                    <th>SECONDARY MOBILE NO:</th>
                    <th>Bank Name</th>
                    <th>Bank Branch Name</th>
                    <th>Bank IFSC Code</th>
                    <th>Bank Accound No.</th>
                    <th>PAN NO</th>
                    <th>UAN NO</th>
                    <th>TYPE OF EMPLOYMENT</th>
                    <th>EDUCATION TILL</th>
                    <th>AADHAR CARD NO</th>
                    <th>MARK OF IDENTIFICATION</th>
                    <th>STARTING DATE WORKING</th>
                    <th>END DATE WORKING</th>
                    <th>MAIL</th>                     
                  </tr>
                  </thead>''')
for x in result:
  print('''<tbody>
                  <tr>                    
                    <td>                      
                      <div class="row">                          
                        <div class="col-12">
                          <a href="UpdateEmployeeDetails.py?id='''+str(x[0])+'''">
                              
                            <button type="submit" class="btn btn-outline-warning btn-block btn-sm">Edit</button>
                          </a> 
                          <br>
                          <a href="DeleteEmployeeDetails_Backend.py?id='''+str(x[0])+'''"> 
                            <button type="submit" class="btn btn-outline-danger btn-block btn-sm">Delete</button>
                          </a>
                        </div>
                      </div>                       
                    </td>
                      <td>'''+str(x[0])+'''</td>
                      <td>'''+str(x[1])+'''</td>
                      <td>'''+str(x[2])+'''</td>
                      <td>'''+str(x[3])+'''</td>
                      <td>'''+str(x[4])+'''</td>
                      <td>'''+str(x[5])+'''</td>
                      <td>'''+str(x[6])+'''</td>
                      <td>'''+str(x[7])+'''</td>
                      <td>'''+str(x[8])+'''</td>
                      <td>'''+str(x[9])+'''</td>
                      <td>'''+str(x[10])+'''</td>
                      <td>'''+str(x[31])+'''</td>                      
                      <td>'''+str(x[32])+'''</td>
                      <td>'''+str(x[11])+'''</td>
                      <td>'''+str(x[12])+'''</td>
                      <td>'''+str(x[13])+'''</td>
                      <td>'''+str(x[14])+'''</td>
                      <td>'''+str(x[15])+'''</td>
                      <td>'''+str(x[16])+'''</td>
                      <td>'''+str(x[17])+'''</td>
                      <td>'''+str(x[18])+'''</td>
                      <td>'''+str(x[19])+'''</td>
                      <td>'''+str(x[20])+'''</td>
                      <td>'''+str(x[21])+'''</td>
                      <td>'''+str(x[22])+'''</td>
                      <td>'''+str(x[23])+'''</td>
                      <td>'''+str(x[24])+'''</td>
                      <td>'''+str(x[25])+'''</td>
                      <td>'''+str(x[26])+'''</td>
                      <td>'''+str(x[27])+'''</td>
                      <td>'''+str(x[28])+'''</td>
                      <td>'''+str(x[29])+'''</td>
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