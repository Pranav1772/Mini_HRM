#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe
import cgi
import cgitb
import mysql.connector
import config,num2words
cgitb.enable()

print("Content-Type:text/html\n")

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)

id=cgi.FieldStorage().getvalue('id')


dbcursor=conn.cursor(buffered=True)
dbcursor.execute("select * from employee_details where id="+str(id))
x=dbcursor.fetchone()
dbcursor.execute("select * from attendance_details where id_list="+str(id))
y=dbcursor.fetchone()
dbcursor.execute("select * from payroll where id="+str(id))
z=dbcursor.fetchone()

cssfiles='''<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback"><link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css"><link rel="stylesheet" href="plugins/datatables-bs4/css/dataTables.bootstrap4.min.css"><link rel="stylesheet" href="plugins/datatables-responsive/css/responsive.bootstrap4.min.css"><link rel="stylesheet" href="plugins/datatables-buttons/css/buttons.bootstrap4.min.css"><link rel="stylesheet" href="dist/css/adminlte.min.css">
<style>
  @media print {
  body *:not(#my-section):not(#my-section *) {
    visibility: hidden;
  }
  #my-section, #my-action * {
    visibility: visible;
  }
  #my-section { 
    position: absolute;
    left: 0;
    top: 0;
  }
}</style>'''



print('''<div class="content-wrapper">
        <form action="AddPayroll_Backend.py" method="post">
          <!-- Content Header (Page header) -->
          <section class="content-header">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-12">
                        <div class="text-center lh-1 mb-2">
                            <h6 class="fw-bold">Payslip</h6> <span class="fw-normal">Payment slip for the month of June 2021</span>
                        </div>                        
                        <div class="row">
                            <div class="col-md-10">
                                <div class="row">
                                    <div class="col-md-6">
                                        <div> <span class="fw-bolder">EMP Code: </span> '''+str(x[0])+'''</div>
                                    </div>
                                    <div class="col-md-6">
                                        <div> <span class="fw-bolder">EMP Name: </span> '''+str(z[1])+''' </div>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-md-6">
                                        <div> <span class="fw-bolder">PF No.: </span> '''+str(x[23])+''' </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div> <span class="fw-bolder">Pan: </span> '''+str(x[22])+''' </div>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-md-6">
                                        <div> <span class="fw-bolder">ESI No.: </span> '''+str(x[20])+''' </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div> <span class="fw-bolder">Mode of Pay: </span> '''+str(x[18])+''' </div>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-md-6">
                                        <div> <span class="fw-bolder">Designation: </span> '''+z[3]+''' </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div> <span class="fw-bolder">Ac No.: </span> '''+x[21]+''' </div>
                                    </div>
                                </div>
                            </div>
                            <table class="mt-4 table table-bordered">
                                <thead class="bg-dark text-white">
                                    <tr>
                                        <th scope="col">Earnings</th>
                                        <th scope="col">Amount</th>
                                        <th scope="col">Deductions</th>
                                        <th scope="col">Amount</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <th scope="row">Basic</th>
                                        <td>'''+str(z[9])+'''</td>
                                        <td>PF</td>
                                        <td>'''+str(z[16])+'''</td>
                                    </tr>
                                    <tr>
                                        <th scope="row">DA</th>
                                        <td>550.00</td>
                                        <td>PT</td>
                                        <td>'''+str(z[15])+'''</td>
                                    </tr>
                                    <tr>
                                        <th scope="row">HRA</th>
                                        <td>'''+str(z[10])+'''</td>
                                        <td></td>
                                        <td></td>
                                    </tr>                                    
                                    <tr>
                                        <th scope="row">MA</th>
                                        <td>'''+str(z[13])+'''</td>
                                        <td></td>
                                        <td></td>
                                    </tr>                                    
                                    <tr class="border-top">
                                        <th scope="row">Total Earning</th>
                                        <td>'''+str(z[14])+'''</td>
                                        <td>Total Deductions</td>
                                        <td>'''+str(z[17])+'''</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="row">
                            <div class="col-md-4"> <br> <span class="fw-bold">Net Pay : '''+str(z[18])+'''</span> </div>
                            <div class="border col-md-8">
                                <div class="d-flex flex-column"> <span>In Words</span> <span>'''+num2words.num2words(z[18])+'''</span> </div>
                            </div>
                        </div>
                        <div class="d-flex justify-content-end">
                            <div class="d-flex flex-column mt-2"> <span class="mt-4">Authorised Signatory</span> </div>
                        </div>
                

                    </div>
                </div>
            </div>
            <script>
  window.addEventListener("load", window.print());
</script>
        </div>  ''')

jsfiles='''<script src="plugins/jquery/jquery.min.js"></script><script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script><script src="plugins/datatables/jquery.dataTables.min.js"></script><script src="plugins/datatables-bs4/js/dataTables.bootstrap4.min.js"></script><script src="plugins/datatables-responsive/js/dataTables.responsive.min.js"></script><script src="plugins/datatables-responsive/js/responsive.bootstrap4.min.js"></script><script src="plugins/datatables-buttons/js/dataTables.buttons.min.js"></script><script src="plugins/datatables-buttons/js/buttons.bootstrap4.min.js"></script><script src="plugins/jszip/jszip.min.js"></script><script src="plugins/pdfmake/pdfmake.min.js"></script><script src="plugins/pdfmake/vfs_fonts.js"></script><script src="plugins/datatables-buttons/js/buttons.html5.min.js"></script><script src="plugins/datatables-buttons/js/buttons.print.min.js"></script><script src="plugins/datatables-buttons/js/buttons.colVis.min.js"></script><script src="dist/js/adminlte.min.js"></script><script src="dist/js/demo.js"></script>'''

script='''<script>$(function(){$("#example1").DataTable({responsive:!0,lengthChange:!1,autoWidth:!1,buttons:["copy","csv","excel","pdf","print","colvis"]}).buttons().container().appendTo("#example1_wrapper .col-md-6:eq(0)"),$("#example2").DataTable({paging:!0,lengthChange:!1,searching:!1,ordering:!0,info:!0,autoWidth:!1,responsive:!0})})</script>'''



