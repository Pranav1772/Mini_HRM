#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb,config,mysql.connector,math
cgitb.enable()

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)

id=cgi.FieldStorage().getvalue('id')
dbcursor=conn.cursor()
dbcursor.execute("select * from payroll where id="+str(id))
x=dbcursor.fetchone()

gross_salary_int=int(x[8])

monthly_gross_salary=gross_salary_int/12
basic_salary=monthly_gross_salary*0.5
hra=basic_salary*0.4
da=basic_salary*0.2
ma=basic_salary*0.16
fa=basic_salary*0.13
other_allowance=basic_salary*0.11
pf=basic_salary*0.12
if basic_salary<=10000:
    pt=0
elif basic_salary>=20000:
    pt=200
else:
    pt=500
total_deductions=pf+pt
total_earnings=basic_salary+hra+da+ma+fa+other_allowance
net_salary=total_earnings-total_deductions


print("Context-Type:Text/html\n")

cssfiles=f'''<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback"><link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css"><link rel="stylesheet" href="plugins/daterangepicker/daterangepicker.css"><link rel="stylesheet" href="plugins/icheck-bootstrap/icheck-bootstrap.min.css"><link rel="stylesheet" href="plugins/bootstrap-colorpicker/css/bootstrap-colorpicker.min.css"><link rel="stylesheet" href="plugins/tempusdominus-bootstrap-4/css/tempusdominus-bootstrap-4.min.css"><link rel="stylesheet" href="plugins/select2/css/select2.min.css"><link rel="stylesheet" href="plugins/select2-bootstrap4-theme/select2-bootstrap4.min.css"><link rel="stylesheet" href="plugins/bootstrap4-duallistbox/bootstrap-duallistbox.min.css"><link rel="stylesheet" href="plugins/bs-stepper/css/bs-stepper.min.css"><link rel="stylesheet" href="plugins/dropzone/min/dropzone.min.css"><link rel="stylesheet" href="dist/css/adminlte.min.css"><link rel="stylesheet" href="dist/css/intlTelInput.css">'''

config.useHeader("Add Payroll",cssfiles)


print(''' 
        <div class="content-wrapper">
        <form action="AddPayrollManagement2_Backend.py" method="post">
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
                          <input type="text" class="form-control" placeholder="Enter Employee Name" name="name" value="'''+str(x[1])+'''" readonly>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Gender</label>
                          <input type="text" class="form-control" placeholder="Gender" name="gender" value="'''+str(x[2])+'''" readonly>
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Designation</label>
                          <input type="text" class="form-control" placeholder="Enter Employee Name" name="designation" value="'''+str(x[3])+'''" readonly>
                        </div>
                      </div>
                    </div>                    
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Department</label>
                          <input type="text" class="form-control" placeholder="Enter Employee Name" name="department" value="'''+str(x[4])+'''" readonly>
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Primary Mobile No.</label>
                          <input type="text" class="form-control" placeholder="Enter Employee Name" name="pmobileno" value="'''+str(x[5])+'''" readonly>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Type of Employment</label>
                          <input type="text" class="form-control" placeholder="Enter Employee Name" name="typeemployment" value="'''+str(x[6])+'''" readonly>
                        </div>
                      </div> 
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Email  </label>
                          <input type="text" class="form-control" placeholder="Enter Employee Name" name="email" value="'''+str(x[7])+'''" readonly>
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
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Gross Salary</label>
                          <input type="text" class="form-control" placeholder="Enter gross salary" name="gs" value="'''+str(x[8])+'''" readonly>
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Basic Salary</label>
                          <input type="text" class="form-control" placeholder="Enter Dearness allowance" name="bs" value="'''+str(math.floor(basic_salary))+'''" readonly>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>House Rent Allowance</label>
                          <input type="text" class="form-control" placeholder="Enter gross salary" name="hra" value="'''+str(math.floor(hra))+'''" readonly>
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Direct Allowance</label>
                          <input type="text" class="form-control" placeholder="Enter Dearness allowance" name="da" value="'''+str(math.floor(da))+'''" readonly>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Food Allowance</label>
                          <input type="text" class="form-control" placeholder="Enter gross salary" name="fa" value="'''+str(math.floor(fa))+'''" readonly>
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Medical Allowance</label>
                          <input type="text" class="form-control" placeholder="Enter Dearness allowance" name="ma" value="'''+str(math.floor(ma))+'''" readonly>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>other Allowance</label>
                          <input type="text" class="form-control" placeholder="Enter gross salary" name="oa" value="'''+str(math.floor(other_allowance))+'''" readonly>
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Total Earnings</label>
                          <input type="text" class="form-control" placeholder="Enter Dearness allowance" name="te" value="'''+str(math.floor(total_earnings))+'''" readonly>
                        </div>
                      </div>
                    </div>                                                                              
                </div>
                <!-- /.card-body -->
              </div>              
              <div class="card card-primary">
                <div class="card-header">
                  <h3 class="card-title">Deductions</h3>
                </div>
                <!-- /.card-header -->
                <div class="card-body">
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Professional Tax</label>
                          <input type="text" class="form-control" placeholder="Enter gross salary" name="pt" value="'''+str(math.floor(pt))+'''" readonly>
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Provident Fund</label>
                          <input type="text" class="form-control" placeholder="Enter " name="pf" value="'''+str(math.floor(pf))+'''" readonly>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Tatal Deductions</label>
                          <input type="text" class="form-control" placeholder="Enter gross salary" name="td" value="'''+str(math.floor(total_deductions))+'''" readonly>
                        </div>
                      </div>                      
                    </div>                                                          
                </div>
                </div>
                <!-- /.card-body -->
                <div class="card card-primary">
                <div class="card-header">
                  <h3 class="card-title">Net Salary</h3>
                </div>
                <!-- /.card-header -->
                <div class="card-body">
                <div class="col-sm-12">
                  <div class="form-group">
                    <input type="text" class="form-control" placeholder="Enter " name="ns" value="'''+str(math.floor(net_salary))+'''" readonly>
                  </div>
                </div>                                                           
                </div>
              </div>                                       
              </div>                                        
              <div class="col-sm-12">
                <div class="form-group">
                  <button type="submit" class="btn btn-primary col-sm-12">Save Payroll</button>
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
