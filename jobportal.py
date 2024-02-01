import sqlite3
from flask import Flask, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobinfo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

connection = sqlite3.connect('userbase.db',check_same_thread=False)

class Person:
  def __init__(self, usrname, emal , code):
    self.username = usrname
    self.email = emal
    self.code = code


# Creating our tables in our database
class Joblist(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(20), nullable=False)
    job_description = db.Column(db.String(100), nullable=False)
    occupatn_title = db.Column(db.String(20), nullable=False)
    job_category = db.Column(db.String(20), nullable=False)
    company_name = db.Column(db.String(20), nullable=False)
    about_company = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    ######################################################################################################################################################################################################################################################################################################################################################################################################################exit  DONT FORGET TO DO UNIQUE = TRUE FOR EMAILLLL WHEN YOU AGAIN CREATE THE JOBINFO DATABASE AS IN THE APPLICATION LIST WE ARE CONSIDERING EMAIL TO BE THE  CHOOSING FACTOR ###############################################################################################################################################################################
    employment_type = db.Column(db.String(20), nullable=False)
    qualification = db.Column(db.String(100), nullable=False)
    duration_of_employment = db.Column(db.String(20), nullable=False)
    required_employee = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    deadline = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    addreass = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.String(20), nullable=False)
    longitude = db.Column(db.String(20), nullable=False)
    occupatn_title = db.Column(db.String(20), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    recruitor_code = db.Column(db.String(50) , nullable = False)

    def __repr__(self) -> str: 
        return f"{self.sno} - {self.job_name} - {self.company_name} - {self.job_category} - {self.job_description}"

class Jobcompany(db.Model):
  # __tablename__ = "users"
  sno = db.Column(db.Integer,primary_key = True)
  comapanynaam = db.Column(db.String(50), nullable = False)
  companyaddress = db.Column(db.String(100))
  companyemail = db.Column(db.String(50))
  contactno = db.Column(db.Integer)
  companydesc = db.Column(db.String(100))
  companycity = db.Column(db.String(15))
  datecreated = db.Column(db.DateTime,default = datetime.utcnow)

class Jobcategory(db.Model):
  snonaam = db.Column(db.Integer,primary_key = True)
  categorynaam = db.Column(db.String(50), nullable = False)
  datecreatednaam = db.Column(db.DateTime, default = datetime.utcnow)

class Employee(db.Model):
  sno = db.Column(db.Integer , primary_key = True)
  comon_username = db.Column(db.String(50))
  comon_email = db.Column(db.String(50))
  comon_code = db.Column(db.String(50))
  comon_date_created = db.Column(db.DateTime , default = datetime.utcnow)


@app.route('/<rec_username>', methods = ['GET','POST'])
def index(rec_username):
  cursor = connection.cursor()
  cursor.execute(f"SELECT * FROM Recruitor WHERE username = '{rec_username}' ")
  recruitorff = cursor.fetchall()
  # print(recruitorff[0][18])
  jobdata = Joblist.query.filter_by(recruitor_code = recruitorff[0][18] )
  # jobdata = Joblist.query.all()
  # print(jobdata)
  companies1 = Jobcompany.query.all()
  companies = []
  for company in companies1:
    abc = []
    abc.append(0)
    abc.append(company.comapanynaam)
    companies.append(abc)

  categories1 = Jobcategory.query.all()
  categories = []
  for category in categories1:
    abc = []
    abc.append(0)
    abc.append(category.categorynaam)
    categories.append(abc)
  recruitor = Person(recruitorff[0][1] , recruitorff[0][2] , recruitorff[0][18])

  
  return render_template('index.html', jobdata = jobdata , recruitor = recruitor , categories = categories , companies = companies)

@app.route('/delete/<sno>/<rec_username>')
def delete_vacancy(sno , rec_username):
  job = Joblist.query.filter_by(sno = sno).first()
  db.session.delete(job)
  db.session.commit()
  return redirect(f'/{rec_username}')




@app.route('/update/<sno>/<rec_username>' , methods = ['GET','POST'])
def update_vacancy(sno , rec_username):
  if request.method == 'POST':
    jobname5 = request.form['jobname']
    jobdescription5 = request.form['jobdescription']
    occupationtitles5 = request.form['occupationtitle']
    jobcategorys5 = request.form['jobcategory']
    companynames5 = request.form['companyname']
    aboutcompanys5 = request.form['aboutcompany']
    salarys5 = request.form['salary']
    emailadds5 = request.form['emailadd']
    typeofemployments5 = request.form['typeofemployment']
    qualifications5 = request.form['qualification']
    durations5 = request.form['duration']
    employeenumbers5 = request.form['employeenumber']
    genders5 = request.form['genders']
    deadlines5 = request.form['deadlines']
    citys5 = request.form['city']
    countrys5 = request.form['country']
    addreasss5 = request.form['addreass']
    latitudes5 = request.form['latitude']
    longitudes5 = request.form['longitude']

    joblist = Joblist.query.filter_by(sno = sno).first()
    joblist.job_name = jobname5
    joblist.job_description = jobdescription5
    joblist.occupatn_title = occupationtitles5
    joblist.job_category = jobcategorys5
    joblist.company_name = companynames5
    joblist.about_company = aboutcompanys5
    joblist.salary = salarys5
    joblist.email = emailadds5
    joblist.employment_type = typeofemployments5
    joblist.qualification = qualifications5
    joblist.duration_of_employment = durations5
    joblist.required_employee = employeenumbers5
    joblist.gender = genders5
    joblist.deadline = deadlines5
    joblist.city = citys5
    joblist.country = countrys5
    joblist.addreass = addreasss5
    joblist.latitude = latitudes5
    joblist.longitude = longitudes5

    # print(joblist.job_name)
    # print(joblist.job_description)
    db.session.add(joblist)
    db.session.commit()
    return redirect(f"/{rec_username}")
  
  cursor = connection.cursor()
  cursor.execute(f"SELECT * FROM Recruitor WHERE username = '{rec_username}' ")
  recruitorff = cursor.fetchall()
  companies1 = Jobcompany.query.all()
  companies = []
  for company in companies1:
    abc = []
    abc.append(0)
    abc.append(company.comapanynaam)
    companies.append(abc)

  categories1 = Jobcategory.query.all()
  categories = []
  for category in categories1:
    abc = []
    abc.append(0)
    abc.append(category.categorynaam)
    categories.append(abc)
  recruitor = Person(recruitorff[0][1] , recruitorff[0][2] , recruitorff[0][18])
  job = Joblist.query.filter_by(sno = sno).first()
  return render_template('update-job-vacancy.html', job = job , companies = companies , categories = categories , recruitor = recruitor)

# Aaraam se kar check karte karte nahi to pata bhi nahi chalega aur bohot bada mess ban jaegaa and then dimaag phodna padega
@app.route('/addjob/<rec_username>', methods = ['GET','POST'])
def addjob(rec_username):
  cursor = connection.cursor()
  cursor.execute(f"SELECT * FROM Recruitor WHERE username = '{rec_username}' ")
  recruitorff = cursor.fetchall()
  if request.method == "POST":
    jobname = request.form['jobname']
    jobdescription = request.form['jobdescription']
    occupationtitles = request.form['occupationtitle']
    jobcategorys = request.form['jobcategory']
    companynames = request.form['companyname']
    aboutcompanys = request.form['aboutcompany']
    salarys = request.form['salary']
    emailadds = request.form['emailadd']
    typeofemployments = request.form['typeofemployment']
    qualifications = request.form['qualification']
    durations = request.form['duration']
    employeenumbers = request.form['employeenumber']
    genders = request.form['genders']
    deadlines = request.form['deadlines']
    citys = request.form['city']
    countrys = request.form['country']
    addreasss = request.form['addreass']
    latitudes = request.form['latitude']
    longitudes = request.form['longitude']



    joblist = Joblist(
     job_name = jobname,
     job_description = jobdescription,
     occupatn_title = occupationtitles,
     job_category = jobcategorys,
     company_name = companynames,
     about_company = aboutcompanys,
     salary = salarys,
     email = emailadds,
     employment_type = typeofemployments,
     qualification = qualifications,
     duration_of_employment = durations,
     required_employee = employeenumbers,
     gender = genders,
     deadline = deadlines,
     city = citys,
     country = countrys,
     addreass = addreasss,
     latitude = latitudes,
     longitude = longitudes,
     recruitor_code = recruitorff[0][18],
    )
    # print(joblist.job_name)
    # print(joblist.job_description)
    db.session.add(joblist)
    db.session.commit()
    return redirect(f"/{rec_username}")
  

  companies1 = Jobcompany.query.all()
  companies = []
  for company in companies1:
    abc = []
    abc.append(0)
    abc.append(company.comapanynaam)
    companies.append(abc)

  categories1 = Jobcategory.query.all()
  categories = []
  for category in categories1:
    abc = []
    abc.append(0)
    abc.append(category.categorynaam)
    categories.append(abc)
  recruitor = Person(recruitorff[0][1] , recruitorff[0][2],recruitorff[0][18])
  return render_template('addjob.html', recruitor = recruitor , categories = categories , companies = companies)

# Creating a route to show job details for user perspective 

@app.route('/jobdetails/<int:sno>/<usr>')
def jobdetails(sno,usr):
  cursor = connection.cursor()
  cursor.execute(f"SELECT * FROM User WHERE username = '{usr}' ")
  user = cursor.fetchall()
  job = Joblist.query.filter_by(sno = sno).first()
  return render_template('jobinfo.html' , job = job,user = user)

# create a route for job details for admin and recruitor perspective 

@app.route('/jobdetails-2/<int:sno>')
def jobdetails2(sno):
  job = Joblist.query.filter_by(sno = sno).first()
  return render_template('jobinfo2.html' , job = job)

@app.route('/displayjobs/<int:number>/<usr>' , methods = ['GET','POST'] )
def displayjob(number,usr):
  cursor = connection.cursor()
  cursor.execute(f"SELECT * FROM User WHERE username = '{usr}' ")
  user = cursor.fetchall()
  if len(user) :
    print("The list is not empty matlab user perspective")
  else :
    cursor.execute(f"SELECT * FROM Recruitor WHERE username = '{usr}' ")
    user = cursor.fetchall()
  
  if request.method == 'POST':
    if number == 1:
      city = request.form['city']
      citydata = Joblist.query.filter_by(city = city)
      companies = Jobcompany.query.all()
      categories = Jobcategory.query.all()
      return render_template('display_locationcity.html', jobdata = citydata , user = user , companies = companies , categories = categories)
    elif number == 2:
      country = request.form['country']
      countrydata = Joblist.query.filter_by(country = country)
      companies = Jobcompany.query.all()
      categories = Jobcategory.query.all()
      return render_template('display_locationcountry.html', jobdata = countrydata , user = user , companies = companies , categories = categories)
    elif number == 3:
      job_category = request.form['jobcategorybitch']
      categorydata = Joblist.query.filter_by(job_category = job_category)
      companies = Jobcompany.query.all()
      categories = Jobcategory.query.all()
      return render_template('display_category.html', jobdata = categorydata , user = user , companies = companies , categories = categories)
    elif number == 4:
      job_name = request.form['jobname']
      jobnamedata = Joblist.query.filter_by(job_name = job_name)
      companies = Jobcompany.query.all()
      categories = Jobcategory.query.all()
      # print(jobnamedata.job_name)
      return render_template('display_name.html', jobdata = jobnamedata , user = user , companies = companies , categories = categories)
    elif number == 5:
      typeofemployment = request.form['typeofemployment']
      typedata = Joblist.query.filter_by(employment_type = typeofemployment)
      companies = Jobcompany.query.all()
      categories = Jobcategory.query.all()
      return render_template('display_type.html', jobdata = typedata , user = user , companies = companies , categories = categories)
    elif number == 6:
      companyname = request.form['companyname']
      typedata = Joblist.query.filter_by(company_name = companyname)
      companies = Jobcompany.query.all()
      categories = Jobcategory.query.all()
      return render_template('display_cname.html', jobdata = typedata , user = user , companies = companies , categories = categories)

  if number == 1:
    jobdata = Joblist.query.all()
    companies = Jobcompany.query.all()
    categories = Jobcategory.query.all()
    return render_template('display_locationcity.html', jobdata = jobdata , user = user , companies = companies , categories = categories)
  if number == 2:
    jobdata = Joblist.query.all()
    companies = Jobcompany.query.all()
    categories = Jobcategory.query.all()
    return render_template('display_locationcountry.html', jobdata = jobdata , user = user , companies = companies , categories = categories)
  if number == 3:
    jobdata = Joblist.query.all()
    companies = Jobcompany.query.all()
    categories = Jobcategory.query.all()
    return render_template('display_category.html', jobdata = jobdata , user = user , companies = companies , categories = categories)
  if number == 4:
    jobdata = Joblist.query.all()
    companies = Jobcompany.query.all()
    categories = Jobcategory.query.all()
    return render_template('display_name.html', jobdata = jobdata , user = user , companies = companies , categories = categories)
  if number == 5:
    jobdata = Joblist.query.all()
    companies = Jobcompany.query.all()
    categories = Jobcategory.query.all()
    return render_template('display_type.html', jobdata = jobdata , user = user , companies = companies , categories = categories)
  if number == 6:
    jobdata = Joblist.query.all()
    companies = Jobcompany.query.all()
    categories = Jobcategory.query.all()
    return render_template('display_cname.html', jobdata = jobdata , user = user , companies = companies , categories = categories)


@app.route('/admin-dashboard')
def admin_dashboard():
  return render_template('admin-dashboard.html')


@app.route('/addcompany' , methods = ['GET','POST'])
def add_company():
  if request.method == 'POST':
    companynaam1 = request.form['companyname']
    companydescription1 = request.form['companydescription']
    companyemail1 = request.form['companyemail']
    contactno1 = request.form['companycontact']
    comapnyaddress1 = request.form['companyaddress']
    companycity1 = request.form['companycity']
    jobcompany = Jobcompany(
      comapanynaam = companynaam1,
      companyaddress = comapnyaddress1,
      contactno = contactno1,
      companyemail = companyemail1,
      companydesc = companydescription1,
      companycity = companycity1,
    )
    db.session.add(jobcompany)
    db.session.commit()
    return redirect('/displaycompany')
  
  return render_template('admin-addcompany.html')


@app.route('/displaycompany')
def display_company():
  companynameslist = Jobcompany.query.all()
  return render_template('admin-displaycompany.html', rahul = companynameslist)

@app.route('/displaycompany/delete/<name>')
def delete_company(name):
  compny = Jobcompany.query.filter_by(comapanynaam = name).first()
  db.session.delete(compny)
  db.session.commit()
  return redirect('/displaycompany')

@app.route('/displaycompany/update/<name>' , methods = ['GET','POST'])
def update_company(name):
  if request.method == 'POST':
    compname1 = request.form['companyname']
    compdesc1 = request.form['companydescription']
    compemail1 = request.form['companyemail']
    compcontactno1 = request.form['companycontact']
    compaddress1 = request.form['companyaddress']
    compcity1 = request.form['companycity']
    company = Jobcompany.query.filter_by(comapanynaam = name).first()
    company.comapanynaam = compname1
    company.companydesc = compdesc1
    company.companyemail = compemail1
    company.contactno = compcontactno1
    company.companyaddress = compaddress1
    company.companycity = compcity1
    db.session.add(company)
    db.session.commit()
    return redirect('/displaycompany')

  company = Jobcompany.query.filter_by(comapanynaam = name).first()
  return render_template('admin-updatecompany.html' , company = company)


@app.route('/add&displaycategories' , methods = ['GET', 'POST'])
def add_display_categories():
  if request.method == 'POST':
    thecategory = request.form['category']
    jobcategorybitch = Jobcategory(categorynaam = thecategory)
    db.session.add(jobcategorybitch)
    db.session.commit()
    
  categorylist1 = Jobcategory.query.all()
  return render_template('admin-display-category.html', categorylist1 = categorylist1)

@app.route('/add&displaycategories/delete/<a>')
def delete_category(a):
  catgry = Jobcategory.query.filter_by( categorynaam = a).first()
  db.session.delete(catgry)
  db.session.commit()
  return redirect('/add&displaycategories')

@app.route('/manageusers')
def manage_users():
  cursor4 = connection.cursor()
  cursor4.execute(f"SELECT * FROM 'User' ")
  users = cursor4.fetchall()
  return render_template('admin-manage-users.html' , users = users)

@app.route('/manage-recruitors')
def manage_recruitors():
  cursor4 = connection.cursor()
  cursor4.execute(f"SELECT * FROM 'Recruitor' ")
  recruitors = cursor4.fetchall()
  return render_template('admin-manage-recruitors.html' , recruitors = recruitors)

@app.route('/manageusers/delete/<a>')
def remove_user(a):
  cursor2 = connection.cursor()
  cursor2.execute(f"DELETE FROM 'User' WHERE username = '{a}' ")
  connection.commit()
  return redirect('/manageusers')


@app.route('/applied-job-list')
def admin_appliedjob_list():
  cursor = connection.cursor()
  cursor.execute(f"SELECT * FROM 'Applicationlist' ")
  applications = cursor.fetchall()
  totalappli = []
  for appli in applications:
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM 'User' WHERE username = '{appli[1]}' ")
    user = cursor.fetchall()
    job = Joblist.query.filter_by(email = appli[2]).first()
    applidetails = []
    applidetails.append(appli[1])#appending the username
    # print(user)
    applidetails.append(user[0][4])#appending the job title of the user
    applidetails.append(job.job_name)
    applidetails.append(job.company_name)
    applidetails.append(appli[3])
    applidetails.append(appli[2])
    applidetails.append(job.recruitor_code)
    totalappli.append(applidetails)
  
  print(totalappli)
  # job = Joblist.query.filter_by(sno = sno).first()
  return render_template('admin-appliedlist.html' ,totalappli =totalappli)

@app.route('/recruitor-applicants/<rec_username>')
def recruitor_appliedjob_list(rec_username):
  cursor = connection.cursor()
  cursor.execute(f"SELECT * FROM Recruitor WHERE username = '{rec_username}' ")
  recruitorff = cursor.fetchall()
  print(recruitorff)
  companies1 = Jobcompany.query.all()
  companies = []
  for company in companies1:
    abc = []
    abc.append(0)
    abc.append(company.comapanynaam)
    companies.append(abc)

  categories1 = Jobcategory.query.all()
  categories = []
  for category in categories1:
    abc = []
    abc.append(0)
    abc.append(category.categorynaam)
    categories.append(abc)

  recruitor = Person(recruitorff[0][1] , recruitorff[0][2] , recruitorff[0][18])
  cursor = connection.cursor()
  cursor.execute(f"SELECT * FROM 'Applicationlist' WHERE recruitor_code = '{recruitorff[0][18]}' ")
  applications = cursor.fetchall()
  totalappli = []
  for appli in applications:
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM 'User' WHERE username = '{appli[1]}' ")
    user = cursor.fetchall()
    job = Joblist.query.filter_by(email = appli[2]).first()
    applidetails = []
    applidetails.append(appli[1])#appending the username
    # print(user)
    applidetails.append(user[0][4])#appending the job title of the user
    applidetails.append(job.job_name)
    applidetails.append(job.company_name)
    applidetails.append(appli[3])
    applidetails.append(appli[2])
    applidetails.append(job.recruitor_code)
    totalappli.append(applidetails)
  return render_template('recruitor-appliedlist.html' , companies = companies , categories = categories , recruitor = recruitor , totalappli = totalappli , job_email = job.email)

@app.route('/admin-job-vacancy')
def admin_job_vacancy():
  jobdata = Joblist.query.all()
  # cursor = connection.cursor()
  # cursor.execute(f"SELECT * FROM Recruitor WHERE recruitor_code = '{}' ")
  # recruitorff = cursor.fetchall()
  companies = Jobcompany.query.all()
  categories = Jobcategory.query.all()

  return render_template('admin-job-vacancy.html' , companies = companies , categories = categories , jobdata = jobdata)

@app.route('/delete-jobvacancy/<sno>')
def admin_delete_vacancy(sno):
  job = Joblist.query.filter_by(sno = sno).first()
  db.session.delete(job)
  db.session.commit()
  return redirect('/admin-job-vacancy')


@app.route('/approve-application/<s>/<s1>/<code>' , methods = ['GET','POST'])
def approve_application(s,s1,code):

  if request.method == 'POST':
    message = request.form['message']
    current_time = datetime.now() 
    cursor = connection.cursor()
    sqlite_insert_query = f"""INSERT INTO Messages
                          ( user_ka_naam, company_ka_email, message , date_created) 
                           VALUES 
                          ("{s}","{s1}","{message}" , "{current_time}");"""
    cursor.execute(sqlite_insert_query)
    connection.commit()
    employee = Employee(
      comon_username = s,
      comon_email = s1,
      comon_code = code,
    )
    db.session.add(employee)
    db.session.commit()
    print("Check kar saara data add hua hai ki nahii") 
  companies1 = Jobcompany.query.all()
  companies = []
  for company in companies1:
    abc = []
    abc.append(0)
    abc.append(company.comapanynaam)
    companies.append(abc)

  categories1 = Jobcategory.query.all()
  categories = []
  for category in categories1:
    abc = []
    abc.append(0)
    abc.append(category.categorynaam)
    categories.append(abc)       
  return render_template('admin-approve-application.html' , username = s , companyemail = s1 , categories = categories , companies = companies , code  = code)

# @app.route('/reject-application/<usr>/<job_email>')
# def reject_application(usr , job_email):

@app.route('/recruitor-employee-list/<rec_username>')
def recruitor_employee(rec_username):
  cursor = connection.cursor()
  cursor.execute(f"SELECT * FROM Recruitor WHERE username = '{rec_username}' ")
  recruitorff = cursor.fetchall()
  recruitor = Person(recruitorff[0][1] , recruitorff[0][2] , recruitorff[0][18])
  companies = Jobcompany.query.all()
  categories = Jobcategory.query.all()
  employees = Employee.query.filter_by(comon_code = recruitorff[0][18])
  return render_template('recruitor-employee.html' , companies = companies , categories = categories , recruitor = recruitor , employees = employees)


if __name__ == "__main__":
  app.run(debug=True,port = 5000)