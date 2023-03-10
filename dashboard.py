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
dbcursor.execute("SELECT COUNT(cmp_reg_id) FROM company_details;")
x=dbcursor.fetchone()
dbcursor.execute("SELECT COUNT(dept_code) FROM department_details;")
y=dbcursor.fetchone()
dbcursor.execute("SELECT COUNT(id) FROM employee_details;")
z=dbcursor.fetchone()
dbcursor.execute("SELECT SUM(ns) FROM payroll;")
w=dbcursor.fetchone()

cssfiles='''<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback"><link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css"><link rel="stylesheet" href="plugins/overlayScrollbars/css/OverlayScrollbars.min.css"><link rel="stylesheet" href="dist/css/adminlte.min.css">'''

form=f'''
  <!-- Content Wrapper. Contains page content -->
    <div class="content-wrapper">
      <!-- Content Header (Page header) -->
      <div class="content-header">
        <div class="container-fluid">
          <div class="row mb-2">
            <div class="col-sm-6">
              <h1 class="m-0">Dashboard</h1>
            </div><!-- /.col -->
            <div class="col-sm-6">
              <ol class="breadcrumb float-sm-right">
                <li class="breadcrumb-item"><a href="#">Home</a></li>
                <li class="breadcrumb-item active">Dashboard v2</li>
              </ol>
            </div><!-- /.col -->
          </div><!-- /.row -->
        </div><!-- /.container-fluid -->
      </div>
      <!-- /.content-header -->

      <!-- Main content -->
      <section class="content">
        <div class="container-fluid">
          


<div class="row">
            <div class="col-12 col-sm-8 col-md-6">
              <div class="info-box">
                <span class="info-box-icon bg-info elevation-1"><i class="fa-solid fa-building"></i></span>

                <div class="info-box-content">
                  <span class="info-box-text">Total Companys</span>
                  <span class="info-box-number"><h1 style="text-align:center;">'''+str(x[0])+'''</h1></span>
                </div>
                <!-- /.info-box-content -->
              </div>
              <!-- /.info-box -->
            </div>
            <!-- /.col -->
            <div class="col-12 col-sm-8 col-md-6">
              <div class="info-box mb-3">
                <span class="info-box-icon bg-danger elevation-1"><i class="fa-thin fa-building-user"></i></span>

                <div class="info-box-content">
                  <span class="info-box-text">Total Department</span>
                  <span class="info-box-number"><h1 style="text-align:center;">'''+str(y[0])+'''</h1></span>
                </div>
                <!-- /.info-box-content -->
              </div>
              <!-- /.info-box -->
            </div>
            <!-- /.col -->   
          </div>

<div class="row">
            <div class="col-12 col-sm-8 col-md-6">
              <div class="info-box">
                <span class="info-box-icon bg-success elevation-1"><i class="fa-solid fa-users"></i></span>

                <div class="info-box-content">
                  <span class="info-box-text">Total Employee</span>
                  <span class="info-box-number"><h1 style="text-align:center;">'''+str(z[0])+'''</h1></span>
                </div>
                <!-- /.info-box-content -->
              </div>
              <!-- /.info-box -->
            </div>
            <!-- /.col -->
            <div class="col-12 col-sm-8 col-md-6">
              <div class="info-box mb-3">
                <span class="info-box-icon bg-danger elevation-1"><i class="fa-thin fa-file-invoice-dollar"></i></span>

                <div class="info-box-content">
                  <span class="info-box-text">Total Salary Paid</span>
                  <span class="info-box-number"><h1 style="text-align:center;">'''+str(w[0])+'''</h1></span>
                </div>
                <!-- /.info-box-content -->
              </div>
              <!-- /.info-box -->
            </div>
            <!-- /.col -->   
          </div>
          

          
        </div>
        <!--/. container-fluid -->
      </section>
      <!-- /.content -->
    </div>
    <!-- /.content-wrapper -->
'''

jsfiles='''<script src="plugins/jquery/jquery.min.js"></script><script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script><script src="plugins/overlayScrollbars/js/jquery.overlayScrollbars.min.js"></script><script src="dist/js/adminlte.js"></script><script src="plugins/jquery-mousewheel/jquery.mousewheel.js"></script><script src="plugins/raphael/raphael.min.js"></script><script src="plugins/jquery-mapael/jquery.mapael.min.js"></script><script src="plugins/jquery-mapael/maps/usa_states.min.js"></script><script src="plugins/chart.js/Chart.min.js"></script><script src="dist/js/pages/dashboard2.js"></script>'''

config.useHeader("Dashboard",cssfiles)
print(form)
config.useFooter(jsfiles)