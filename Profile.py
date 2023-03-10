#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe
import cgi
import cgitb
import mysql.connector
import config
cgitb.enable()
print("Content-Type:text/html\n")

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)

dbcursor=conn.cursor()
dbcursor.execute("select * from employee_details;")
x=dbcursor.fetchone()

cssfiles='''<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback"><link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css"><link rel="stylesheet" href="plugins/datatables-bs4/css/dataTables.bootstrap4.min.css"><link rel="stylesheet" href="plugins/datatables-responsive/css/responsive.bootstrap4.min.css"><link rel="stylesheet" href="plugins/datatables-buttons/css/buttons.bootstrap4.min.css"><link rel="stylesheet" href="dist/css/adminlte.min.css">'''

config.useHeader("Profile",cssfiles)


print(''' <!-- Content Wrapper. Contains page content -->
  <div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <section class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1>Profile</h1>
          </div>
          <div class="col-sm-6">
            <ol class="breadcrumb float-sm-right">
              <li class="breadcrumb-item"><a href="#">Home</a></li>
              <li class="breadcrumb-item active">User Profile</li>
            </ol>
          </div>
        </div>
      </div><!-- /.container-fluid -->
    </section>

    <!-- Main content -->
    <section class="content">
      <div class="container-fluid">
        

            <!-- Profile Image -->
            <div class="card card-primary card-outline">
              <div class="card-body box-profile">
                <div class="text-center">
               <img style="vertical-align: middle;
                      width: 210px;
                      height: 210px;
                      border-radius: 50%;"
                       src="dist/img/avatar5.png"
                       alt="User profile picture"
                       > 
                </div>

                <h3 class="profile-username text-center">Nihal Sayyad</h3>

                <p class="text-muted text-center">Devloper</p>
                
                <p class="text-muted text-center">id : '''+str(x[0])+'''</p>

              </div>
              <!-- /.card-body -->
            </div>
            <!-- /.card -->
            
                
              <div class="container-fluid">
                <div class="row">
                  <!-- left column -->
                  
                  <div class="col-md-6">
                    <!-- jquery validation -->

                    <div class="card card-primary">
                      <div class="card-header">
                        <h3 class="card-title">PERSONAL DETAILS</h3>
                      </div>
                      <!-- /.card-header -->
                      <!-- form start -->
                      
                      <div class="card-body">
                <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>FIRST NAME :</label>
                       <label style=padding-left:30px;><td>'''+str(x[1])+'''</td></label>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label>MIDDLE NAME :</label>
                        <label style=padding-left:33px;>'''+str(x[2])+'''</label>
                      </div>
                  </div>
                </div>
              </div>
              
              <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label for="fname">LAST NAME :</label>
                        <label style=padding-left:35px;>'''+str(x[3])+'''</label>                      
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label>FATHER NAME :</label>
                        <label style=padding-left:33px;>'''+str(x[4])+'''</label>
                      </div>
                  </div>
                </div>
              </div>
              
              <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label for="fname">MOTHER NAME :</label>
                        <label style=padding-left:10px;>'''+str(x[5])+'''</label>                      
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label>BIRTH DATE :</label>
                        <label style=padding-left:48px;>'''+str(x[6])+'''</label>
                      </div>
                  </div>
                </div>
              </div>
              
              <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label for="fname">GENDER :</label>
                        <label style=padding-left:55px;>'''+str(x[7])+'''</label>                      
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label>SPOUSE NAME :</label>
                        <label style=padding-left:30px;>'''+str(x[8])+'''</label>
                      </div>
                  </div>
                </div>
              </div>
              
              <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label for="fname">NATIONALITY :</label>
                        <label style=padding-left:20px;>'''+str(x[9])+'''</label>                      
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label>MARITAL STATUS :</label>
                        <label style=padding-left:15px;>'''+str(x[10])+'''</label>
                      </div>
                  </div>
                </div>
              </div>
              
              <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label for="fname">DESIGNATION :</label>
                        <label style=padding-left:15px;>'''+str(x[31])+'''</label>                      
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label>DEPARTMENT :</label>
                        <label style=padding-left:38px;>'''+str(x[32])+'''</label>
                      </div>
                  </div>
                </div>
              </div>
              
 
              </div>
  
                    </div>
                    <!-- /.card -->
                    </div>


                    <div class="col-md-6">
                    <!-- jquery validation -->

                    <div class="card card-primary">
                      <div class="card-header">
                        <h3 class="card-title">ADDRESS & CONTACT DETAILS</h3>
                      </div>
                      <!-- /.card-header -->
                      <!-- form start -->
                      
                      <div class="card-body">
                <div class="card-body">
                <div class="row">
                  <div class="col-sm-12">
                    <!-- text input -->
                    <div class="form-group">
                      <label>Address(Area and Street) :</label>
                       <label style=padding-left:25px;>'''+str(x[11])+''' </label>
                    </div>
                  </div>
                  
              </div>
              
              <div class="row">
                  <div class="col-sm-12">
                    <!-- text input -->
                    <div class="form-group">
                      <label>Locality :</label>
                       <label style=padding-left:38px;>'''+str(x[12])+''' </label>
                    </div>
                  </div>
                  
              </div>
              
              
              
              
              <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>Pincode :</label>
                       <label style=padding-left:38px;>'''+str(x[13])+''' </label>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label>District :</label>
                        <label style=padding-left:58px;>'''+str(x[14])+'''</label>
                      </div>
                  </div>
                </div>
              </div>
              
              <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>State :</label>
                       <label style=padding-left:58px;>'''+str(x[15])+''' </label>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label>P MOBILE NO :</label>
                        <label style=padding-left:20px;>'''+str(x[16])+'''</label>
                      </div>
                  </div>
                </div>
              </div>
              
              <div class="row">
                  <div class="col-sm-12">
                    <!-- text input -->
                    <div class="form-group">
                      <label>S MOBILE NO :</label>
                       <label style=padding-left:8px;>'''+str(x[17])+''' </label>
                    </div>
                  </div>
                  
              </div>
              
              
          
              </div>              
              </div>
  
                    </div>
                    <!-- /.card -->
                    </div>
                </div>
                <!-- /.row -->
              </div><!-- /.container-fluid -->
        
        
              <div class="container-fluid">
                <div class="row">
                  <!-- left column -->
                  
                  <div class="col-md-6">
                    <!-- jquery validation -->

                    <div class="card card-primary">
                      <div class="card-header">
                        <h3 class="card-title">Banking Details</h3>
                      </div>
                      <!-- /.card-header -->
                      <!-- form start -->
                      
                      <div class="card-body">
                <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>Bank Name :</label>
                       <label style=padding-left:15px;>'''+str(x[18])+'''</label>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label>Bank Branch Name :</label>
                        <label style=padding-left:15px;>'''+str(x[19])+'''</label>
                      </div>
                  </div>
                </div>
              </div>
              
              <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label >IFSC Code :</label>
                        <label style=padding-left:25px;>'''+str(x[20])+'''</label>                      
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label>Bank Accound No. :</label>
                        <label style=padding-left:20px;>'''+str(x[21])+'''</label>
                      </div>
                  </div>
                </div>
              </div>
              
              <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label >PAN NO. :</label>
                        <label style=padding-left:35px;>'''+str(x[22])+'''</label>                      
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label>UAN NO. :</label>
                        <label style=padding-left:85px;>'''+str(x[23])+'''</label>
                      </div>
                  </div>
                </div>
              </div>
              
              <div class="row">
                  <div class="col-sm-12">
                    <!-- text input -->
                    <div class="form-group">
                      <label>  </label>
                       
                    </div>
                  </div>
                </div>
              
              
              </div>
              </div>
              </div>


                    
                    <div class="col-md-6">
                    <!-- jquery validation -->

                    <div class="card card-primary">
                      <div class="card-header">
                        <h3 class="card-title">More Informational</h3>
                      </div>
                      <!-- /.card-header -->
                      <!-- form start -->
                      
                <div class="card-body">
                <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>TYPE OF EMPLOYMENT :</label>
                       <label style=padding-left:7px;>'''+str(x[24])+'''</label>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label >EDUCATION TILL :</label>
                        <label style=padding-left:25px;>'''+str(x[25])+'''</label>
                      </div>
                  </div>
                </div>
              </div>
              
              <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label for="fname">AADHAR CARD NO :</label>
                        <label style=padding-left:40px;>'''+str(x[26])+'''</label>                      
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label>MARK OF <br>IDENTIFICATION  :</br></label>
                        <label style=padding-left:23px;>'''+str(x[27])+'''</label>
                      </div>
                  </div>
                </div>
              </div>
              
              <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label for="fname">STARTING DATE :</label>
                        <label style=padding-left:55px;>'''+str(x[28])+'''</label>                      
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label>END DATE :</label>
                        <label style=padding-left:68px;>'''+str(x[29])+'''</label>
                      </div>
                  </div>
                </div>
              </div>
              
               <div class="row">
                  <div class="col-sm-12">
                    <!-- text input -->
                    <div class="form-group">
                      <label>EMAIL :</label>
                       <label style=padding-left:118px;>'''+str(x[30])+''' </label>
                    </div>
                  </div>
                </div>
              
              
              </div>
              </div>
              </div>

  
                    </div>
                    <!-- /.card -->
                    </div>
                </div>
                <!-- /.row -->
              </div><!-- /.container-fluid -->

        
        
    </section>
    <!-- /.content -->
  </div>
  <!-- /.content-wrapper -->''')
 
 
jsfiles='''<script src="plugins/jquery/jquery.min.js"></script><script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script><script src="plugins/datatables/jquery.dataTables.min.js"></script><script src="plugins/datatables-bs4/js/dataTables.bootstrap4.min.js"></script><script src="plugins/datatables-responsive/js/dataTables.responsive.min.js"></script><script src="plugins/datatables-responsive/js/responsive.bootstrap4.min.js"></script><script src="plugins/datatables-buttons/js/dataTables.buttons.min.js"></script><script src="plugins/datatables-buttons/js/buttons.bootstrap4.min.js"></script><script src="plugins/jszip/jszip.min.js"></script><script src="plugins/pdfmake/pdfmake.min.js"></script><script src="plugins/pdfmake/vfs_fonts.js"></script><script src="plugins/datatables-buttons/js/buttons.html5.min.js"></script><script src="plugins/datatables-buttons/js/buttons.print.min.js"></script><script src="plugins/datatables-buttons/js/buttons.colVis.min.js"></script><script src="dist/js/adminlte.min.js"></script><script src="dist/js/demo.js"></script>'''

script='''<script>$(function(){$("#example1").DataTable({responsive:!0,lengthChange:!1,autoWidth:!1,buttons:["copy","csv","excel","pdf","print","colvis"]}).buttons().container().appendTo("#example1_wrapper .col-md-6:eq(0)"),$("#example2").DataTable({paging:!0,lengthChange:!1,searching:!1,ordering:!0,info:!0,autoWidth:!1,responsive:!0})})</script>'''



config.useFooter(jsfiles,script)