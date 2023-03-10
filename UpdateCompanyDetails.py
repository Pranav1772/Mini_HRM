#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb,config,mysql.connector

cgitb.enable()

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)

cmp_reg_id=cgi.FieldStorage().getvalue('cmp_reg_id')
dbcursor=conn.cursor()
dbcursor.execute("select * from company_details where cmp_reg_id='"+cmp_reg_id+"'")
result=dbcursor.fetchone()


cssfiles=f'''<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback"><link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css"><link rel="stylesheet" href="plugins/daterangepicker/daterangepicker.css"><link rel="stylesheet" href="plugins/icheck-bootstrap/icheck-bootstrap.min.css"><link rel="stylesheet" href="plugins/bootstrap-colorpicker/css/bootstrap-colorpicker.min.css"><link rel="stylesheet" href="plugins/tempusdominus-bootstrap-4/css/tempusdominus-bootstrap-4.min.css"><link rel="stylesheet" href="plugins/select2/css/select2.min.css"><link rel="stylesheet" href="plugins/select2-bootstrap4-theme/select2-bootstrap4.min.css"><link rel="stylesheet" href="plugins/bootstrap4-duallistbox/bootstrap-duallistbox.min.css"><link rel="stylesheet" href="plugins/bs-stepper/css/bs-stepper.min.css"><link rel="stylesheet" href="plugins/dropzone/min/dropzone.min.css"><link rel="stylesheet" href="dist/css/adminlte.min.css"><link rel="stylesheet" href="dist/css/intlTelInput.css">'''

form=f'''
      <div class="content-wrapper">
        <form action="UpdateCompanyDetails_Backend.py" method="post">
          <!-- Content Header (Page header) -->
          <section class="content-header">
            <div class="container-fluid">
              <div class="row mb-2">
                <div class="col-sm-6">
                  <h1>Update Company Details</h1>
                </div>
                <div class="col-sm-6">
                  <ol class="breadcrumb float-sm-right">
                    <li class="breadcrumb-item"><a href="index.html">Home</a></li>
                    <li class="breadcrumb-item active">Update Company Details</li>
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
                  <h3 class="card-title">Company Registration Details</h3>
                </div>
                <!-- /.card-header -->
                <div class="card-body">
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Company Registration Id</label>
                          <input type="text" class="form-control" placeholder="Enter Registration Id" name="cmp_reg_id" value="'''+result[0]+'''">
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Company Name</label>
                          <input type="text" class="form-control" placeholder="Enter Company Name" name="cmp_name" value="'''+result[1]+'''">
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Company Official Email</label>
                          <div class="input-group mb-3">
                            <input type="email" class="form-control" placeholder="Enter Official Email" name="cmp_email" value="'''+result[2]+'''">
                            <div class="input-group-append">
                              <span class="input-group-text"><i class="fas fa-envelope"></i></span>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Company Official number</label>
                          <div class="input-group mb-3">
                            <input type="text" class="form-control" placeholder="Enter Official Number" name="cmp_no" value="'''+result[3]+'''">
                            <div class="input-group-append">
                              <span class="input-group-text"><i class="fas fa-phone"></i></span>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Company Registration Date</label>
                          <div class="input-group date" id="reservationdate" data-target-input="nearest">
                            <input type="text" class="form-control datetimepicker-input" data-target="#reservationdate"
                              placeholder="Enter Registration Date" name="cmp_reg_date" value="'''+result[4]+'''"/>
                            <div class="input-group-append" data-target="#reservationdate" data-toggle="datetimepicker">
                              <div class="input-group-text"><i class="fas fa-calendar-alt"></i></div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label for="exampleInputFile">Company Logo</label>
                          <div class="input-group">
                            <div class="custom-file">
                              <input type="file" class="custom-file-input" id="exampleInputFile" name="cmp_logo">
                              <label class="custom-file-label" for="exampleInputFile">'''+str(result[5])+'''</label>
                            </div>
                            <div class="input-group-append">
                              <span class="input-group-text">Upload</span>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Company GST No.</label>
                          <input type="text" class="form-control" placeholder="Enter GST No." name="cmp_gst_no" value="'''+result[6]+'''">
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <div class="form-group">
                          <label>Company Type</label>
                          <select class="form-control select2bs4" 
                            style="width: 100%;" name="cmp_type">
                            <option selected="selected" value="'''+str(result[7])+'''">'''+str(result[7])+'''</option>
                            <option value="1">Private company limited by shares</option>
                            <option value="2">Public limited company</option>
                            <option value="3">Limited liability partnership</option>                          
                          </select>
                        </div>
                      </div>
                    </div>
                </div>
                <!-- /.card-body -->
              </div>
              <div class="card card-primary">
                <div class="card-header">
                  <h3 class="card-title">Company Banking Details</h3>
                </div>
                <!-- /.card-header -->
                <div class="card-body">
                    <div class="row">
                      <div class="col-sm-6">
                        <div class="form-group is-warning">
                          <label>Company Bank Name</label>
                          <input type="text" class="form-control" placeholder="Enter Bank Name" name="cmp_bnk_name" value="'''+result[8]+'''">
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <div class="form-group">
                          <label>Company Bank Branch Name</label>
                          <input type="text" class="form-control" placeholder="Enter Bank Branch Name"
                            name="cmp_bnk_brn_name" value="'''+result[9]+'''">
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <div class="form-group">
                          <label>Company Bank IFSC Code</label>
                          <input type="text" class="form-control" placeholder="Enter IFSC Code" name="cmp_bnk_ifsc_code" value="'''+result[10]+'''">
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <div class="form-group">
                          <label>Company Bank Accound No.</label>
                          <div class="input-group mb-3">
                            <input type="text" class="form-control" placeholder="Enter Account No." name="cmp_bnk_acc_no" value="'''+result[11]+'''">
                          </div>
                        </div>
                      </div>
                    </div>
                </div>
                <!-- /.card-body -->
              </div>
              <div class="card card-primary">
                <div class="card-header">
                  <h3 class="card-title">Company Address Details</h3>
                </div>
                <!-- /.card-header -->
                <div class="card-body">
                    <div class="row">
                      <div class="col-sm-12">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Company Address(Area and Street)</label>
                          <textarea class="form-control" rows="3" placeholder="Enter Area and Street"
                            name="cmp_addr">'''+result[12]+'''</textarea>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Company Locality</label>
                          <input type="text" class="form-control" placeholder="Enter locality" name="cmp_locality" value="'''+result[13]+'''">
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <!-- text input -->
                        <div class="form-group">
                          <label>Company Pincode</label>
                          <input type="text" class="form-control" placeholder="Enter Pincode" name="cmp_pincode" value="'''+result[14]+'''">
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <div class="form-group">
                          <label>Company District</label>
                          <select class="form-control select2bs4" data-dropdown-css-class="select2-primary"
                            style="width: 100%;" name="cmp_district">
                            <option selected="selected" value="'''+str(result[15])+'''">'''+str(result[15])+'''</option>
                            <option value="1">Kolhapur</option>
                            <option value="2">Satara</option>
                          </select>
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <div class="form-group">
                          <label>Company State</label>
                          <select class="form-control select2bs4" data-dropdown-css-class="select2-primary"
                            style="width: 100%;" name="cmp_state">
                            <option selected="selected" value="'''+str(result[16])+'''">'''+str(result[16])+'''</option>
                            <option value="1">Maharashtra</option>
                            <option value="2">Gujarat</option>
                          </select>
                        </div>
                      </div>
                    </div>
                </div>
                <!-- /.card-body -->
              </div>
              <div class="card card-primary">
                <div class="card-header">
                  <h3 class="card-title">Company Owner Details</h3>
                </div>
                <!-- /.card-header -->
                <div class="card-body">
                    <div class="row">
                      <div class="col-sm-6">
                        <div class="form-group is-warning">
                          <label>Company Owner First Name</label>
                          <input type="text" class="form-control" placeholder="Enter First Name" name="cmp_own_fname" value="'''+result[17]+'''">
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <div class="form-group">
                          <label>Company Owner Last Name</label>
                          <input type="text" class="form-control" placeholder="Enter Last Name" name="cmp_own_lname" value="'''+result[18]+'''">
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-sm-6">
                        <div class="form-group is-warning">
                          <label>Company Owner Email</label>
                          <div class="input-group mb-3">
                            <input type="text" class="form-control" placeholder="Enter Owner Email" name="cmp_own_email" value="'''+result[19]+'''">
                            <div class="input-group-append">
                              <span class="input-group-text"><i class="fas fa-envelope"></i></span>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="col-sm-6">
                        <div class="form-group">
                          <label>Company Owner Number</label>
                          <div class="input-group mb-3">
                            <input type="text" class="form-control" placeholder="Enter Owner Number" name="cmp_own_no" value="'''+result[20]+'''">
                            <div class="input-group-append">
                              <span class="input-group-text"><i class="fas fa-phone"></i></span>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                </div>
                <!-- /.card-body -->
              </div>
              <div class="col-sm-12">
                <div class="form-group">
                  <button type="submit" class="btn btn-primary col-sm-12">Add New Company</button>
                </div>
              </div>
            </div>
        </form>
      </div>
    </div>
'''

jsfiles=f'''<script src="plugins/jquery/jquery.min.js"></script><script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script><script src="plugins/select2/js/select2.full.min.js"></script><script src="plugins/bootstrap4-duallistbox/jquery.bootstrap-duallistbox.min.js"></script><script src="plugins/moment/moment.min.js"></script><script src="plugins/inputmask/jquery.inputmask.min.js"></script><script src="plugins/daterangepicker/daterangepicker.js"></script><script src="plugins/bootstrap-colorpicker/js/bootstrap-colorpicker.min.js"></script><script src="plugins/tempusdominus-bootstrap-4/js/tempusdominus-bootstrap-4.min.js"></script><script src="plugins/bootstrap-switch/js/bootstrap-switch.min.js"></script><script src="plugins/bs-stepper/js/bs-stepper.min.js"></script><script src="plugins/dropzone/min/dropzone.min.js"></script><script src="dist/js/adminlte.min.js"></script><script src="dist/js/demo.js"></script><script src="plugins/bs-custom-file-input/bs-custom-file-input.min.js"></script>'''

script='''<script>$(function(){$(".select2").select2(),$(".select2bs4").select2({theme:"bootstrap4"}),$("#datemask").inputmask("dd/mm/yyyy",{placeholder:"dd/mm/yyyy"}),$("#datemask2").inputmask("mm/dd/yyyy",{placeholder:"mm/dd/yyyy"}),$("[data-mask]").inputmask(),$("#reservationdate").datetimepicker({format:"L"}),$("#reservationdatetime").datetimepicker({icons:{time:"far fa-clock"}}),$("#reservation").daterangepicker(),$("#reservationtime").daterangepicker({timePicker:!0,timePickerIncrement:30,locale:{format:"MM/DD/YYYY hh:mm A"}}),$("#daterange-btn").daterangepicker({ranges:{Today:[moment(),moment()],Yesterday:[moment().subtract(1,"days"),moment().subtract(1,"days")],"Last 7 Days":[moment().subtract(6,"days"),moment()],"Last 30 Days":[moment().subtract(29,"days"),moment()],"This Month":[moment().startOf("month"),moment().endOf("month")],"Last Month":[moment().subtract(1,"month").startOf("month"),moment().subtract(1,"month").endOf("month")]},startDate:moment().subtract(29,"days"),endDate:moment()},function(e,t){$("#reportrange span").html(e.format("MMMM D, YYYY")+" - "+t.format("MMMM D, YYYY"))}),$("#timepicker").datetimepicker({format:"LT"}),$(".duallistbox").bootstrapDualListbox(),$(".my-colorpicker1").colorpicker(),$(".my-colorpicker2").colorpicker(),$(".my-colorpicker2").on("colorpickerChange",function(e){$(".my-colorpicker2 .fa-square").css("color",e.color.toString())}),$("input[data-bootstrap-switch]").each(function(){$(this).bootstrapSwitch("state",$(this).prop("checked"))})}),document.addEventListener("DOMContentLoaded",function(){window.stepper=new Stepper(document.querySelector(".bs-stepper"))}),Dropzone.autoDiscover=!1;var previewNode=document.querySelector("#template");previewNode.id="";var previewTemplate=previewNode.parentNode.innerHTML;previewNode.parentNode.removeChild(previewNode);var myDropzone=new Dropzone(document.body,{url:"/target-url",thumbnailWidth:80,thumbnailHeight:80,parallelUploads:20,previewTemplate:previewTemplate,autoQueue:!1,previewsContainer:"#previews",clickable:".fileinput-button"});myDropzone.on("addedfile",function(e){e.previewElement.querySelector(".start").onclick=function(){myDropzone.enqueueFile(e)}}),myDropzone.on("totaluploadprogress",function(e){document.querySelector("#total-progress .progress-bar").style.width=e+"%"}),myDropzone.on("sending",function(e){document.querySelector("#total-progress").style.opacity="1",e.previewElement.querySelector(".start").setAttribute("disabled","disabled")}),myDropzone.on("queuecomplete",function(e){document.querySelector("#total-progress").style.opacity="0"}),document.querySelector("#actions .start").onclick=function(){myDropzone.enqueueFiles(myDropzone.getFilesWithStatus(Dropzone.ADDED))},document.querySelector("#actions .cancel").onclick=function(){myDropzone.removeAllFiles(!0)}</script><script>$(function(){bsCustomFileInput.init()})</script>'''

config.useHeader("Update Company Details",cssfiles)
print(form)
config.useFooter(jsfiles,script)