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
dbcursor.execute("select * from company_details;")
result=dbcursor.fetchall()
cssfiles='''<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback"><link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css"><link rel="stylesheet" href="dist/css/adminlte.min.css">'''

config.useHeader("Company Details List",cssfiles)
print('''
  <div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <section class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1>Company Details</h1>
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
                    <th>Company Registration ID</th>
                    <th>Company Name</th>
                    <th>Company Official Email</th>
                    <th>Company Official number</th>
                    <th>Company Registration Date</th>
                    <th>Company Logo</th>
                    <th>Company GST No.</th>
                    <th>Company Type</th>                    
                    <th>Company Bank Name</th>
                    <th>Company Bank Branch Name</th>
                    <th>Company Bank IFSC Code</th>
                    <th>Company Bank Accound No.</th>
                    <th>Company Address(Area and Street)</th>
                    <th>Company Locality</th>
                    <th>Company Pincode</th>
                    <th>Company District</th>
                    <th>Company State</th>
                    <th>Company Owner First Name</th>
                    <th>Company Owner Last Name</th>
                    <th>Company Owner Email</th>
                    <th>Company Owner Number</th>
                  </tr>
                  </thead>''')
for x in result:
  print('''       <tbody>
                  <tr>
                    <td>                      
                      <div class="row">                          
                        <div class="col-12">
                          <a href="UpdateCompanyDetails.py?cmp_reg_id='''+x[0]+'''">
                              
                            <button type="submit" class="btn btn-outline-warning btn-block btn-sm">Edit</button>
                          </a> 
                          <br>
                          <a href="DeleteCompanyDetails_Backend.py?cmp_reg_id='''+x[0]+'''"> 
                            <button type="submit" class="btn btn-outline-danger btn-block btn-sm">Delete</button>
                          </a>
                        </div>
                      </div>                       
                    </td>
                    <td>'''+x[0]+'''</td>
                    <td>'''+x[1]+'''</td>
                    <td>'''+x[2]+'''</td>
                    <td>'''+x[3]+'''</td>
                    <td>'''+x[4]+'''</td>
                    <td>'''+str(x[5])+'''</td>
                    <td>'''+x[6]+'''</td>
                    <td>'''+str(x[7])+'''</td>                    
                    <td>'''+x[8]+'''</td>
                    <td>'''+x[9]+'''</td>
                    <td>'''+x[10]+'''</td>
                    <td>'''+x[11]+'''</td>
                    <td>'''+x[12]+'''</td>
                    <td>'''+x[13]+'''</td>
                    <td>'''+x[14]+'''</td>
                    <td>'''+str(x[15])+'''</td>
                    <td>'''+str(x[16])+'''</td>
                    <td>'''+x[17]+'''</td>
                    <td>'''+x[18]+'''</td>
                    <td>'''+x[19]+'''</td>
                    <td>'''+x[20]+'''</td>
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

jsfiles='''<script src="plugins/jquery/jquery.min.js"></script><script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script><script src="dist/js/adminlte.min.js"></script><script src="dist/js/demo.js"></script>'''

#script='''<script>$(function(){$("#example1").DataTable({responsive:!0,lengthChange:!1,autoWidth:!1,buttons:["copy","csv","excel","pdf","print","colvis"]}).buttons().container().appendTo("#example1_wrapper .col-md-6:eq(0)"),$("#example2").DataTable({paging:!0,lengthChange:!1,searching:!1,ordering:!0,info:!0,autoWidth:!1,responsive:!0})})</script>'''

config.useFooter(jsfiles)