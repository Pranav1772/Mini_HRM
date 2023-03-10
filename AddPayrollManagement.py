#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe

import config
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-Type:text/html\n")

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)

id=cgi.FieldStorage().getvalue('id')
dbcursor=conn.cursor()
dbcursor.execute("select * from employee_details where id ='"+str(id)+"';")
results=dbcursor.fetchall()

cssfiles=f'''<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback"><link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css"><link rel="stylesheet" href="plugins/daterangepicker/daterangepicker.css"><link rel="stylesheet" href="plugins/icheck-bootstrap/icheck-bootstrap.min.css"><link rel="stylesheet" href="plugins/bootstrap-colorpicker/css/bootstrap-colorpicker.min.css"><link rel="stylesheet" href="plugins/tempusdominus-bootstrap-4/css/tempusdominus-bootstrap-4.min.css"><link rel="stylesheet" href="plugins/select2/css/select2.min.css"><link rel="stylesheet" href="plugins/select2-bootstrap4-theme/select2-bootstrap4.min.css"><link rel="stylesheet" href="plugins/bootstrap4-duallistbox/bootstrap-duallistbox.min.css"><link rel="stylesheet" href="plugins/bs-stepper/css/bs-stepper.min.css"><link rel="stylesheet" href="plugins/dropzone/min/dropzone.min.css"><link rel="stylesheet" href="dist/css/adminlte.min.css"><link rel="stylesheet" href="dist/css/intlTelInput.css">'''

config.useHeader("Add Payroll",cssfiles)

for x in results:
  print(''' 
        <div class="content-wrapper">
        <form action="AddPayrollManagement_Backend.py" method="post">
          <!-- Content Header (Page header) -->
          <section class="content-header">
            <div class="container-fluid">
              <div class="row mb-2">
                <div class="col-sm-6">
                  <h1>Add Payroll</h1>
                </div>
                <div class="col-sm-6">
                  <ol class="breadcrumb float-sm-right">
                    <li class="breadcrumb-item"><a href="index.html">Home</a></li>
                    <li class="breadcrumb-item active">Add New User</li>
                  </ol>
                </div>
              </div>
            </div><!-- /.container-fluid -->
          </section>

          <!-- Main content -->
          <section class="content">
            
            <div class="container-fluid">
              <!-- general form elements disabled -->
              <div class="card card-primary">
                <div class="card-header">
                  <h3 class="card-title">Employee  Details</h3>
                </div>
                <!-- /.card-header -->
                <div class="card-body">
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>ID</label>
                          <input type="text" class="form-control" placeholder="Enter employee id" name="id" value="'''+str(x[0])+'''" readonly>
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Name</label>
                          <input type="text" class="form-control" placeholder="Enter Employee Name" name="fname" value="'''+str(x[1])+" "+str(x[2])+" "+str(x[3])+'''" readonly>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Gender</label>
                          <input type="text" class="form-control" placeholder="Gender" name="gender" value="'''+str(x[7])+'''" readonly>
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Designation</label>
                          <input type="text" class="form-control" placeholder="Enter Designation" name="designation" value="'''+str(x[31])+'''" readonly>
                        </div>
                      </div>
                    </div>                    
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Department</label>
                          <input type="text" class="form-control" placeholder="Enter Department" name="department" value="'''+str(x[32])+'''" readonly>
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Primary Mobile No.</label>
                          <input type="text" class="form-control" placeholder="Enter Primary Mobile No" name="pmobileno" value="'''+str(x[16])+'''" readonly>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Type of Employment</label>
                          <input type="text" class="form-control" placeholder="Enter Employee type" name="typeemployment" value="'''+str(x[24])+'''" readonly>
                        </div>
                      </div> 
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Email  </label>
                          <input type="text" class="form-control" placeholder="Enter email" name="email" value="'''+str(x[30])+'''" readonly>
                        </div>
                      </div>                    
                    </div>
                </div>
                <!-- /.card-body -->
              </div>   
              <div class="card card-primary">
                <div class="card-header">
                  <h3 class="card-title">Earnings</h3>
                </div>
                <!-- /.card-header -->
                <div class="card-body">
                    <div class="row">
                      <div class="col-sm-12">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Gross Salary For Year</label>
                          <input type="text" class="form-control" placeholder="Enter gross salary For Year" name="gross_salary">
                        </div>
                      </div>                      
                    </div>
                    
              <div class="col-sm-12">
                <div class="form-group">
                  <button type="submit" class="btn btn-primary col-sm-12">Get Detailed Payroll</button>
                </div>
              </div>
              
            </div>
        </form>
      </div>
    </div>
    ''')

jsfiles=f'''<script src="plugins/jquery/jquery.min.js"></script><script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script><script src="plugins/select2/js/select2.full.min.js"></script><script src="plugins/bootstrap4-duallistbox/jquery.bootstrap-duallistbox.min.js"></script><script src="plugins/moment/moment.min.js"></script><script src="plugins/inputmask/jquery.inputmask.min.js"></script><script src="plugins/daterangepicker/daterangepicker.js"></script><script src="plugins/bootstrap-colorpicker/js/bootstrap-colorpicker.min.js"></script><script src="plugins/tempusdominus-bootstrap-4/js/tempusdominus-bootstrap-4.min.js"></script><script src="plugins/bootstrap-switch/js/bootstrap-switch.min.js"></script><script src="plugins/bs-stepper/js/bs-stepper.min.js"></script><script src="plugins/dropzone/min/dropzone.min.js"></script><script src="dist/js/adminlte.min.js"></script><script src="dist/js/demo.js"></script><script src="plugins/bs-custom-file-input/bs-custom-file-input.min.js"></script>'''

script='''<script>$(function(){$(".select2").select2(),$(".select2bs4").select2({theme:"bootstrap4"}),$("#datemask").inputmask("dd/mm/yyyy",{placeholder:"dd/mm/yyyy"}),$("#datemask2").inputmask("mm/dd/yyyy",{placeholder:"mm/dd/yyyy"}),$("[data-mask]").inputmask(),$("#reservationdate").datetimepicker({format:"L"}),$("#reservationdatetime").datetimepicker({icons:{time:"far fa-clock"}}),$("#reservation").daterangepicker(),$("#reservationtime").daterangepicker({timePicker:!0,timePickerIncrement:30,locale:{format:"MM/DD/YYYY hh:mm A"}}),$("#daterange-btn").daterangepicker({ranges:{Today:[moment(),moment()],Yesterday:[moment().subtract(1,"days"),moment().subtract(1,"days")],"Last 7 Days":[moment().subtract(6,"days"),moment()],"Last 30 Days":[moment().subtract(29,"days"),moment()],"This Month":[moment().startOf("month"),moment().endOf("month")],"Last Month":[moment().subtract(1,"month").startOf("month"),moment().subtract(1,"month").endOf("month")]},startDate:moment().subtract(29,"days"),endDate:moment()},function(e,t){$("#reportrange span").html(e.format("MMMM D, YYYY")+" - "+t.format("MMMM D, YYYY"))}),$("#timepicker").datetimepicker({format:"LT"}),$(".duallistbox").bootstrapDualListbox(),$(".my-colorpicker1").colorpicker(),$(".my-colorpicker2").colorpicker(),$(".my-colorpicker2").on("colorpickerChange",function(e){$(".my-colorpicker2 .fa-square").css("color",e.color.toString())}),$("input[data-bootstrap-switch]").each(function(){$(this).bootstrapSwitch("state",$(this).prop("checked"))})}),document.addEventListener("DOMContentLoaded",function(){window.stepper=new Stepper(document.querySelector(".bs-stepper"))}),Dropzone.autoDiscover=!1;var previewNode=document.querySelector("#template");previewNode.id="";var previewTemplate=previewNode.parentNode.innerHTML;previewNode.parentNode.removeChild(previewNode);var myDropzone=new Dropzone(document.body,{url:"/target-url",thumbnailWidth:80,thumbnailHeight:80,parallelUploads:20,previewTemplate:previewTemplate,autoQueue:!1,previewsContainer:"#previews",clickable:".fileinput-button"});myDropzone.on("addedfile",function(e){e.previewElement.querySelector(".start").onclick=function(){myDropzone.enqueueFile(e)}}),myDropzone.on("totaluploadprogress",function(e){document.querySelector("#total-progress .progress-bar").style.width=e+"%"}),myDropzone.on("sending",function(e){document.querySelector("#total-progress").style.opacity="1",e.previewElement.querySelector(".start").setAttribute("disabled","disabled")}),myDropzone.on("queuecomplete",function(e){document.querySelector("#total-progress").style.opacity="0"}),document.querySelector("#actions .start").onclick=function(){myDropzone.enqueueFiles(myDropzone.getFilesWithStatus(Dropzone.ADDED))},document.querySelector("#actions .cancel").onclick=function(){myDropzone.removeAllFiles(!0)}</script><script>$(function(){bsCustomFileInput.init()})</script>'''

config.useFooter(jsfiles,script)