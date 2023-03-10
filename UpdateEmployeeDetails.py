#!C:\Users\Parth Desai\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb,config,mysql.connector

cgitb.enable()

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_hrm"
)

print("Context-Type:Text/html\n")

emp_id=cgi.FieldStorage().getvalue('id')
dbcursor=conn.cursor()
dbcursor.execute("select * from employee_details where id='"+str(emp_id)+"'")
result=dbcursor.fetchone()

#print(result)


cssfiles=f'''<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback"><link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css"><link rel="stylesheet" href="plugins/daterangepicker/daterangepicker.css"><link rel="stylesheet" href="plugins/icheck-bootstrap/icheck-bootstrap.min.css"><link rel="stylesheet" href="plugins/bootstrap-colorpicker/css/bootstrap-colorpicker.min.css"><link rel="stylesheet" href="plugins/tempusdominus-bootstrap-4/css/tempusdominus-bootstrap-4.min.css"><link rel="stylesheet" href="plugins/select2/css/select2.min.css"><link rel="stylesheet" href="plugins/select2-bootstrap4-theme/select2-bootstrap4.min.css"><link rel="stylesheet" href="plugins/bootstrap4-duallistbox/bootstrap-duallistbox.min.css"><link rel="stylesheet" href="plugins/bs-stepper/css/bs-stepper.min.css"><link rel="stylesheet" href="plugins/dropzone/min/dropzone.min.css"><link rel="stylesheet" href="dist/css/adminlte.min.css"><link rel="stylesheet" href="dist/css/intlTelInput.css">'''

form=f'''
      <div class="content-wrapper">
      <form action="UpdateEmployeeDetails_backend.py" method="post">
      <!-- Content Header (Page header) -->
      <section class="content-header">
        <div class="container-fluid">
          <div class="row mb-2">
            <div class="col-sm-6">
              <h1>Upadate Employee Details</h1>
            </div>
            <div class="col-sm-6">
              <ol class="breadcrumb float-sm-right">
                <li class="breadcrumb-item"><a href="dashboard.html">Home</a></li>
                <li class="breadcrumb-item active">Add New Employee</li>
              </ol>
            </div>
          </div>
        </div><!-- /.container-fluid -->
      </section>

      <!-- Main content -->
      <form action="UpdateEmployeeDetails_backend.py" method="post">
      <section class="content">
        <div class="container-fluid">
          <!-- general form elements disabled -->
          <div class="card card-primary">
            <div class="card-header">
              <h3 class="card-title">Employee Registration Details</h3>
            </div>
            <!-- /.card-header -->
            <div class="card-body">
            <div class="row">
                  <div class="col-sm-12">
                    <!-- text input -->
                    <div class="form-group">
                      <label for="fname">Employee id</label>
                      <input type="text" class="form-control" name="id" placeholder="Enter id" value='''+str(result[0])+'''>
                    </div>                 
                </div>
              </div>
                <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label for="fname">FIRST NAME</label>
                      <input type="text" class="form-control" name="fname" placeholder="Enter first name" value='''+str(result[1])+'''>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <div class="form-group">
                        <label>MIDDLE NAME</label>
                        <input type="text" class="form-control" name="mname" placeholder="Enter middle name" value='''+str(result[2])+'''>
                      </div>
                  </div>
                </div>
              </div>
                <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>LAST NAME</label>
                        <input type="text" class="form-control" name="lname" placeholder="Enter last name" value='''+str(result[3])+'''>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>FATHER NAME</label>
                        <input type="text" class="form-control" name="faname" placeholder="Enter Father Name" value='''+str(result[4])+'''>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>MOTHER NAME</label>
                      <input type="text" class="form-control" name="moname" placeholder="Enter Mother Name" value='''+str(result[5])+'''> 
                    </div>
                  </div>
                <div class="col-sm-6">
                    <div class="form-group">
                      <label>BIRTH DATE</label>
                        <div class="input-group date" data-target-input="nearest">
                          <input type="text" class="form-control datetimepicker-input" data-target="#reservationdate"
                            placeholder="00/00/0000"  name="birthdate" value='''+str(result[6])+'''/>
                          <div class="input-group-append" data-target="#reservationdate" data-toggle="datetimepicker">
                            <div class="input-group-text"><i class="fas fa-calendar-alt"></i></div>
                          </div>
                        </div>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>GENDER</label>
                      <select class="form-control select2bs4" style="width: 100%"; name="gender">
                        <option value='''+str(result[7])+'''>'''+str(result[7])+'''</option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                        <option value="Transgender">Transgender</option>
                        <option value="Prefer not to respond">Prefer not to respond</option>
                      </select> 
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>SPOUSE NAME</label>
                      <input type="text" class="form-control" name="spname" placeholder="Enter Spouse Name" value='''+str(result[8])+'''>                   
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>NATIONALITY</label>               
					<select class="form-control select2bs4" style="width: 100%"; name="nationality">
                  <option value='''+str(result[9])+'''>'''+str(result[9])+'''</option>
				  <option value="indian">Indian</option>
				  <option value="afghan">Afghan</option>
				  <option value="albanian">Albanian</option>
				  <option value="algerian">Algerian</option>
				  <option value="american">American</option>
				  <option value="andorran">Andorran</option>
				  <option value="angolan">Angolan</option>
				  <option value="antiguans">Antiguans</option>
				  <option value="argentinean">Argentinean</option>
				  <option value="armenian">Armenian</option>
				  <option value="australian">Australian</option>
				  <option value="austrian">Austrian</option>
				  <option value="azerbaijani">Azerbaijani</option>
				  <option value="bahamian">Bahamian</option>
				  <option value="bahraini">Bahraini</option>
				  <option value="bangladeshi">Bangladeshi</option>
				  <option value="barbadian">Barbadian</option>
				  <option value="barbudans">Barbudans</option>
				  <option value="batswana">Batswana</option>
				  <option value="belarusian">Belarusian</option>
				  <option value="belgian">Belgian</option>
				  <option value="belizean">Belizean</option>
				  <option value="beninese">Beninese</option>
				  <option value="bhutanese">Bhutanese</option>
				  <option value="bolivian">Bolivian</option>
				  <option value="bosnian">Bosnian</option>
				  <option value="brazilian">Brazilian</option>
				  <option value="british">British</option>
				  <option value="bruneian">Bruneian</option>
				  <option value="bulgarian">Bulgarian</option>
				  <option value="burkinabe">Burkinabe</option>
				  <option value="burmese">Burmese</option>
				  <option value="burundian">Burundian</option>
				  <option value="cambodian">Cambodian</option>
				  <option value="cameroonian">Cameroonian</option>
				  <option value="canadian">Canadian</option>
				  <option value="cape verdean">Cape Verdean</option>
				  <option value="central african">Central African</option>
				  <option value="chadian">Chadian</option>
				  <option value="chilean">Chilean</option>
				  <option value="chinese">Chinese</option>
				  <option value="colombian">Colombian</option>
				  <option value="comoran">Comoran</option>
				  <option value="congolese">Congolese</option>
				  <option value="costa rican">Costa Rican</option>
				  <option value="croatian">Croatian</option>
				  <option value="cuban">Cuban</option>
				  <option value="cypriot">Cypriot</option>
				  <option value="czech">Czech</option>
				  <option value="danish">Danish</option>
				  <option value="djibouti">Djibouti</option>
				  <option value="dominican">Dominican</option>
				  <option value="dutch">Dutch</option>
				  <option value="east timorese">East Timorese</option>
				  <option value="ecuadorean">Ecuadorean</option>
				  <option value="egyptian">Egyptian</option>
				  <option value="emirian">Emirian</option>
				  <option value="equatorial guinean">Equatorial Guinean</option>
				  <option value="eritrean">Eritrean</option>
				  <option value="estonian">Estonian</option>
				  <option value="ethiopian">Ethiopian</option>
				  <option value="fijian">Fijian</option>
				  <option value="filipino">Filipino</option>
				  <option value="finnish">Finnish</option>
				  <option value="french">French</option>
				  <option value="gabonese">Gabonese</option>
				  <option value="gambian">Gambian</option>
				  <option value="georgian">Georgian</option>
				  <option value="german">German</option>
				  <option value="ghanaian">Ghanaian</option>
				  <option value="greek">Greek</option>
				  <option value="grenadian">Grenadian</option>
				  <option value="guatemalan">Guatemalan</option>
				  <option value="guinea-bissauan">Guinea-Bissauan</option>
				  <option value="guinean">Guinean</option>
				  <option value="guyanese">Guyanese</option>
				  <option value="haitian">Haitian</option>
				  <option value="herzegovinian">Herzegovinian</option>
				  <option value="honduran">Honduran</option>
				  <option value="hungarian">Hungarian</option>
				  <option value="icelander">Icelander</option>
				  <option value="indonesian">Indonesian</option>
				  <option value="iranian">Iranian</option>
				  <option value="iraqi">Iraqi</option>
				  <option value="irish">Irish</option>
				  <option value="israeli">Israeli</option>
				  <option value="italian">Italian</option>
				  <option value="ivorian">Ivorian</option>
				  <option value="jamaican">Jamaican</option>
				  <option value="japanese">Japanese</option>
				  <option value="jordanian">Jordanian</option>
				  <option value="kazakhstani">Kazakhstani</option>
				  <option value="kenyan">Kenyan</option>
				  <option value="kittian and nevisian">Kittian and Nevisian</option>
				  <option value="kuwaiti">Kuwaiti</option>
				  <option value="kyrgyz">Kyrgyz</option>
				  <option value="laotian">Laotian</option>
				  <option value="latvian">Latvian</option>
				  <option value="lebanese">Lebanese</option>
				  <option value="liberian">Liberian</option>
				  <option value="libyan">Libyan</option>
				  <option value="liechtensteiner">Liechtensteiner</option>
				  <option value="lithuanian">Lithuanian</option>
				  <option value="luxembourger">Luxembourger</option>
				  <option value="macedonian">Macedonian</option>
				  <option value="malagasy">Malagasy</option>
				  <option value="malawian">Malawian</option>
				  <option value="malaysian">Malaysian</option>
				  <option value="maldivan">Maldivan</option>
				  <option value="malian">Malian</option>
				  <option value="maltese">Maltese</option>
				  <option value="marshallese">Marshallese</option>
				  <option value="mauritanian">Mauritanian</option>
				  <option value="mauritian">Mauritian</option>
				  <option value="mexican">Mexican</option>
				  <option value="micronesian">Micronesian</option>
				  <option value="moldovan">Moldovan</option>
				  <option value="monacan">Monacan</option>
				  <option value="mongolian">Mongolian</option>
				  <option value="moroccan">Moroccan</option>
				  <option value="mosotho">Mosotho</option>
				  <option value="motswana">Motswana</option>
				  <option value="mozambican">Mozambican</option>
				  <option value="namibian">Namibian</option>
				  <option value="nauruan">Nauruan</option>
				  <option value="nepalese">Nepalese</option>
				  <option value="new zealander">New Zealander</option>
				  <option value="ni-vanuatu">Ni-Vanuatu</option>
				  <option value="nicaraguan">Nicaraguan</option>
				  <option value="nigerien">Nigerien</option>
				  <option value="north korean">North Korean</option>
				  <option value="northern irish">Northern Irish</option>
				  <option value="norwegian">Norwegian</option>
				  <option value="omani">Omani</option>
				  <option value="pakistani">Pakistani</option>
				  <option value="palauan">Palauan</option>
				  <option value="panamanian">Panamanian</option>
				  <option value="papua new guinean">Papua New Guinean</option>
				  <option value="paraguayan">Paraguayan</option>
				  <option value="peruvian">Peruvian</option>
				  <option value="polish">Polish</option>
				  <option value="portuguese">Portuguese</option>
				  <option value="qatari">Qatari</option>
				  <option value="romanian">Romanian</option>
				  <option value="russian">Russian</option>
				  <option value="rwandan">Rwandan</option>
				  <option value="saint lucian">Saint Lucian</option>
				  <option value="salvadoran">Salvadoran</option>
				  <option value="samoan">Samoan</option>
				  <option value="san marinese">San Marinese</option>
				  <option value="sao tomean">Sao Tomean</option>
				  <option value="saudi">Saudi</option>
				  <option value="scottish">Scottish</option>
				  <option value="senegalese">Senegalese</option>
				  <option value="serbian">Serbian</option>
				  <option value="seychellois">Seychellois</option>
				  <option value="sierra leonean">Sierra Leonean</option>
				  <option value="singaporean">Singaporean</option>
				  <option value="slovakian">Slovakian</option>
				  <option value="slovenian">Slovenian</option>
				  <option value="solomon islander">Solomon Islander</option>
				  <option value="somali">Somali</option>
				  <option value="south african">South African</option>
				  <option value="south korean">South Korean</option>
				  <option value="spanish">Spanish</option>
				  <option value="sri lankan">Sri Lankan</option>
				  <option value="sudanese">Sudanese</option>
				  <option value="surinamer">Surinamer</option>
				  <option value="swazi">Swazi</option>
				  <option value="swedish">Swedish</option>
				  <option value="swiss">Swiss</option>
				  <option value="syrian">Syrian</option>
				  <option value="taiwanese">Taiwanese</option>
				  <option value="tajik">Tajik</option>
				  <option value="tanzanian">Tanzanian</option>
				  <option value="thai">Thai</option>
				  <option value="togolese">Togolese</option>
				  <option value="tongan">Tongan</option>
				  <option value="trinidadian or tobagonian">Trinidadian or Tobagonian</option>
				  <option value="tunisian">Tunisian</option>
				  <option value="turkish">Turkish</option>
				  <option value="tuvaluan">Tuvaluan</option>
				  <option value="ugandan">Ugandan</option>
				  <option value="ukrainian">Ukrainian</option>
				  <option value="uruguayan">Uruguayan</option>
				  <option value="uzbekistani">Uzbekistani</option>
				  <option value="venezuelan">Venezuelan</option>
				  <option value="vietnamese">Vietnamese</option>
				  <option value="welsh">Welsh</option>
				  <option value="yemenite">Yemenite</option>
				  <option value="zambian">Zambian</option>
				  <option value="zimbabwean">Zimbabwean</option>
				</select>
					</div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>MARITAL STATUS</label>
                        <select class="form-control select2bs4" style="width: 100%"; name="maritalstatus">
                          <option value='''+str(result[10])+'''>'''+str(result[10])+'''</option>
                          <option value="Yes">Yes</option>
                          <option>No</option>
                          <option>Prefer not to respond</option>
                        </select>                    
                      </div>
                  </div>
                </div>
                
                
               <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>DESIGNATION</label>
                      <input type="text" class="form-control" name="designation" placeholder="Enter Designation" value='''+str(result[31])+'''>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label> DEPARTMENT </label>
                      <input type="text" class="form-control" name="department" placeholder="Enter department" value='''+str(result[32])+'''>                   
                    </div>
                  </div>
                </div> 
                
                
            </div>
            <!-- /.card-body -->
          </div>
          
          <div class="card card-primary">
            <div class="card-header">
              <h3 class="card-title">Address Details & Contact Informational</h3>
            </div>
            <!-- /.card-header -->
            <div class="card-body">
                <div class="row">
                  <div class="col-sm-12">
                    <!-- text input -->
                    <div class="form-group">
                      <label> Address(Area and Street)</label>
                      <textarea class="form-control" rows="3" placeholder="Enter Area and Street" name="addressarea" >'''+str(result[11])+'''</textarea>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>Locality</label>
                      <input type="text" class="form-control" placeholder="Enter locality" name="locality" value='''+str(result[12])+'''>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>Pincode</label>
                      <input type="text" class="form-control" placeholder="Enter Pincode" name="pincode" value='''+str(result[13])+'''>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <div class="form-group">
                      <label>District</label>
                      <select class="form-control select2 select2-primary" data-dropdown-css-class="select2-primary"
                        style="width: 100%;" name="district">
					<option value='''+str(result[14])+'''>'''+str(result[14])+'''</option>
					<option value="Anantapur" >Anantapur</option>
					<option value="Chittoor">Chittoor</option>
					<option value="East Godavari">East Godavari</option>
					<option value="Kolhapur">Kolhapur</option>
				</select>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <div class="form-group">
                      <label>State</label>
                      <select class="form-control select2 select2-primary" data-dropdown-css-class="select2-primary"
                        style="width: 100%;" name="state">    
                    <option value='''+str(result[15])+'''>'''+str(result[15])+'''</option>
					<option value="Andhra Pradesh">Andhra Pradesh</option>
					<option value="Andaman and Nicobar Islands">Andaman and Nicobar Islands</option>
					<option value="Arunachal Pradesh">Arunachal Pradesh</option>
					<option value="Assam">Assam</option>
					<option value="Bihar">Bihar</option>
					<option value="Chandigarh">Chandigarh</option>
					<option value="Chhattisgarh">Chhattisgarh</option>
					<option value="Dadar and Nagar Haveli">Dadar and Nagar Haveli</option>
					<option value="Daman and Diu">Daman and Diu</option>
					<option value="Delhi">Delhi</option>
					<option value="Lakshadweep">Lakshadweep</option>
					<option value="Puducherry">Puducherry</option>
					<option value="Goa">Goa</option>
					<option value="Gujarat">Gujarat</option>
					<option value="Haryana">Haryana</option>
					<option value="Himachal Pradesh">Himachal Pradesh</option>
					<option value="Jammu and Kashmir">Jammu and Kashmir</option>
					<option value="Jharkhand">Jharkhand</option>
					<option value="Karnataka">Karnataka</option>
					<option value="Kerala">Kerala</option>
					<option value="Madhya Pradesh">Madhya Pradesh</option>
					<option value="Maharashtra">Maharashtra</option>
					<option value="Manipur">Manipur</option>
					<option value="Meghalaya">Meghalaya</option>
					<option value="Mizoram">Mizoram</option>
					<option value="Nagaland">Nagaland</option>
					<option value="Odisha">Odisha</option>
					<option value="Punjab">Punjab</option>
					<option value="Rajasthan">Rajasthan</option>
					<option value="Sikkim">Sikkim</option>
					<option value="Tamil Nadu">Tamil Nadu</option>
					<option value="Telangana">Telangana</option>
					<option value="Tripura">Tripura</option>
					<option value="Uttar Pradesh">Uttar Pradesh</option>
					<option value="Uttarakhand">Uttarakhand</option>
					<option value="West Bengal">West Bengal</option>
					</select>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>PRIMARY MOBILE NO:</label>
                      <input type="text" class="form-control" name="pmobileno" placeholder="Enter primary Mobile No" value='''+str(result[16])+'''>                    
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <!-- text input -->
                    <div class="form-group">
                      <label>SECONDARY MOBILE NO:</label>
                      <input type="text" class="form-control" name="smobileno" placeholder="Enter Secondary Mobile No" value='''+str(result[17])+'''>
                </div>
                  </div>
                </div>

            </div>
            <!-- /.card-body -->
          </div>

          <div class="card card-primary">
            <div class="card-header">
              <h3 class="card-title">Banking Details</h3>
            </div>
            <!-- /.card-header -->
            <div class="card-body">
                <div class="row">
                  <div class="col-sm-6">
                    <div class="form-group is-warning">
                      <label>Bank Name</label>
                      <input type="text" class="form-control" placeholder="Enter First Name" name="bankname" value='''+str(result[18])+'''>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <div class="form-group">
                      <label>Bank Branch Name</label>
                      <input type="text" class="form-control" placeholder="Enter Last Name" name="bankbranchname" value='''+str(result[19])+'''>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <div class="form-group">
                      <label>Bank IFSC Code</label>
                      <input type="text" class="form-control" placeholder="Enter IFSC Code" name="ifsccode" value='''+str(result[20])+'''>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <div class="form-group">
                      <label>Bank Accound No.</label>
                      <div class="input-group mb-3">
                        <input type="text" class="form-control" placeholder="Enter Account No." name="bankaccount" value='''+str(result[21])+'''>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <div class="form-group">
                      <label>PAN CARD NUMBER (PAN NO.)</label>
                      <input type="text" class="form-control" name="panno" placeholder="Enter Pan No" value='''+str(result[22])+'''>
                  </div>
                  </div>
                  <div class="col-sm-6">
                    <div class="form-group">
                      <label>Universal Account Number (UAN NO.)</label>
                      <input type="text" class="form-control" name="una" placeholder="Enter UAN  No" value='''+str(result[23])+'''>
                    </div>
                  </div>
                </div>
            </div>
            <!-- /.card-body -->
          </div>

          <div class="card card-primary">
            <div class="card-header">
              <h3 class="card-title">More Informational</h3>
            </div>
            <!-- /.card-header -->
            <div class="card-body">
                <div class="row">
                  <div class="col-sm-6">
                    <div class="form-group is-warning">
                      <label>TYPE OF EMPLOYMENT</label>
                      <select class="form-control select2bs4" style="width: 100%"; name="employment">
                        <option value='''+str(result[24])+'''>'''+str(result[24])+'''</option>
                        <option selected="selected">Full-Time Employees</option>
                        <option value="Part-Time Employees">Part-Time Employees</option>
                        <option value="Temporary Employees">Temporary Employees</option>
                        <option value="Internship">Internship</option>
                      </select>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <div class="form-group">
                      <label>EDUCATION TILL</label>
                      <input type="text" class="form-control" name="education" placeholder="Enter Education Till" value='''+str(result[25])+'''> 
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <div class="form-group is-warning">
                      <label>AADHAR CARD NO</label>
                          <input type="text" class="form-control" name="aadharcardno"
                            placeholder="Enter Aadhar Card No" value='''+str(result[26])+'''>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <div class="form-group">
                      <label>MARK OF IDENTIFICATION</label>
                      <input type="text" class="form-control" name="markofiden" placeholder="Enter Mark Of Identification" value='''+str(result[27])+'''> 
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <div class="form-group is-warning">
                      <label>STARTING DATE WORKING</label>
                      <div class="input-group date" id="reservationdate" data-target-input="nearest">
                        <input type="text" class="form-control datetimepicker-input"
                          data-target="#reservationdate" placeholder="00/00/0000" name="inputdata" value='''+str(result[28])+'''/>
                        <div class="input-group-append" data-target="#reservationdate"
                          data-toggle="datetimepicker">
                          <div class="input-group-text"><i class="fa fa-calendar"></i></div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-sm-6">
                    <div class="form-group">
                      <label>END DATE WORKING</label>
                          <div class="input-group date" id="reservationdate" data-target-input="nearest">
                            <input type="text" class="form-control datetimepicker-input"
                              data-target="#reservationdate" placeholder="00/00/0000" name="enddate" value='''+str(result[29])+''' />
                            <div class="input-group-append" data-target="#reservationdate"
                              data-toggle="datetimepicker">
                              <div class="input-group-text"><i class="fa fa-calendar"></i></div>
                            </div>
                          </div>
                    </div>
                  </div>
                </div>
                 <div class="row">
                  <div class="col-sm-6">
                    <div class="form-group">
                    <label for="exampleInputFile">Upload a Photo</label>
                    <div class="input-group">
                      <div class="custom-file">
                        <input type="file" class="custom-file-input" name="uploadphoto" value='''+str(result[30])+'''>
                        <label class="custom-file-label" for="exampleInputFile">Choose file</label>
                      </div>
                      <div class="input-group-append">
                        <span class="input-group-text">Upload</span>
                      </div>
                    </div>
                    </div>
                    </div>
                  
                  <div class="col-sm-6">
                    <div class="form-group">
                      <label>EMAIL</label>
                      <input type="email" class="form-control" name="email" placeholder="Enter Email" value='''+str(result[30])+'''> 
                    </div>
                  </div>
                </div>              
            </div>
            <!-- /.card-body -->
          </div>
          <div class="col-sm-12">
            <div class="form-group">
              <button type="submit" class="btn btn-primary col-sm-12">Add New Employee</button>
            </div>
          </div>
        </div>
      </form>
    </div> '''

jsfiles=f'''<script src="plugins/jquery/jquery.min.js"></script><script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script><script src="plugins/select2/js/select2.full.min.js"></script><script src="plugins/bootstrap4-duallistbox/jquery.bootstrap-duallistbox.min.js"></script><script src="plugins/moment/moment.min.js"></script><script src="plugins/inputmask/jquery.inputmask.min.js"></script><script src="plugins/daterangepicker/daterangepicker.js"></script><script src="plugins/bootstrap-colorpicker/js/bootstrap-colorpicker.min.js"></script><script src="plugins/tempusdominus-bootstrap-4/js/tempusdominus-bootstrap-4.min.js"></script><script src="plugins/bootstrap-switch/js/bootstrap-switch.min.js"></script><script src="plugins/bs-stepper/js/bs-stepper.min.js"></script><script src="plugins/dropzone/min/dropzone.min.js"></script><script src="dist/js/adminlte.min.js"></script><script src="dist/js/demo.js"></script><script src="plugins/bs-custom-file-input/bs-custom-file-input.min.js"></script>'''

script='''<script>$(function(){$(".select2").select2(),$(".select2bs4").select2({theme:"bootstrap4"}),$("#datemask").inputmask("dd/mm/yyyy",{placeholder:"dd/mm/yyyy"}),$("#datemask2").inputmask("mm/dd/yyyy",{placeholder:"mm/dd/yyyy"}),$("[data-mask]").inputmask(),$("#reservationdate").datetimepicker({format:"L"}),$("#reservationdatetime").datetimepicker({icons:{time:"far fa-clock"}}),$("#reservation").daterangepicker(),$("#reservationtime").daterangepicker({timePicker:!0,timePickerIncrement:30,locale:{format:"MM/DD/YYYY hh:mm A"}}),$("#daterange-btn").daterangepicker({ranges:{Today:[moment(),moment()],Yesterday:[moment().subtract(1,"days"),moment().subtract(1,"days")],"Last 7 Days":[moment().subtract(6,"days"),moment()],"Last 30 Days":[moment().subtract(29,"days"),moment()],"This Month":[moment().startOf("month"),moment().endOf("month")],"Last Month":[moment().subtract(1,"month").startOf("month"),moment().subtract(1,"month").endOf("month")]},startDate:moment().subtract(29,"days"),endDate:moment()},function(e,t){$("#reportrange span").html(e.format("MMMM D, YYYY")+" - "+t.format("MMMM D, YYYY"))}),$("#timepicker").datetimepicker({format:"LT"}),$(".duallistbox").bootstrapDualListbox(),$(".my-colorpicker1").colorpicker(),$(".my-colorpicker2").colorpicker(),$(".my-colorpicker2").on("colorpickerChange",function(e){$(".my-colorpicker2 .fa-square").css("color",e.color.toString())}),$("input[data-bootstrap-switch]").each(function(){$(this).bootstrapSwitch("state",$(this).prop("checked"))})}),document.addEventListener("DOMContentLoaded",function(){window.stepper=new Stepper(document.querySelector(".bs-stepper"))}),Dropzone.autoDiscover=!1;var previewNode=document.querySelector("#template");previewNode.id="";var previewTemplate=previewNode.parentNode.innerHTML;previewNode.parentNode.removeChild(previewNode);var myDropzone=new Dropzone(document.body,{url:"/target-url",thumbnailWidth:80,thumbnailHeight:80,parallelUploads:20,previewTemplate:previewTemplate,autoQueue:!1,previewsContainer:"#previews",clickable:".fileinput-button"});myDropzone.on("addedfile",function(e){e.previewElement.querySelector(".start").onclick=function(){myDropzone.enqueueFile(e)}}),myDropzone.on("totaluploadprogress",function(e){document.querySelector("#total-progress .progress-bar").style.width=e+"%"}),myDropzone.on("sending",function(e){document.querySelector("#total-progress").style.opacity="1",e.previewElement.querySelector(".start").setAttribute("disabled","disabled")}),myDropzone.on("queuecomplete",function(e){document.querySelector("#total-progress").style.opacity="0"}),document.querySelector("#actions .start").onclick=function(){myDropzone.enqueueFiles(myDropzone.getFilesWithStatus(Dropzone.ADDED))},document.querySelector("#actions .cancel").onclick=function(){myDropzone.removeAllFiles(!0)}</script><script>$(function(){bsCustomFileInput.init()})</script>'''

config.useHeader("Update Company Details",cssfiles)
print(form)
config.useFooter(jsfiles,script)