from flask import Flask, render_template, redirect, url_for,request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import string
import random
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userbase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'
connection1 = sqlite3.connect('jobinfo.db',check_same_thread=False)
connection2 = sqlite3.connect('userbase.db',check_same_thread=False)

class User( db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    job_title = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    website_url = db.Column(db.String(50))
    age = db.Column(db.Integer)
    education_lvl = db.Column(db.String(50))
    experience = db.Column(db.String(50))
    description = db.Column(db.String(100))
    user_country = db.Column(db.String(50))
    user_city = db.Column(db.String(50))
    user_addreass = db.Column(db.String(100))
    facebook_url = db.Column(db.String(50))
    twitter_url = db.Column(db.String(50))
    linkedin_url = db.Column(db.String(50))
    insta_url = db.Column(db.String(50))

class Recruitor( db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    job_title = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    website_url = db.Column(db.String(50))
    age = db.Column(db.Integer)
    education_lvl = db.Column(db.String(50))
    experience = db.Column(db.String(50))
    description = db.Column(db.String(100))
    user_country = db.Column(db.String(50))
    user_city = db.Column(db.String(50))
    user_addreass = db.Column(db.String(100))
    facebook_url = db.Column(db.String(50))
    twitter_url = db.Column(db.String(50))
    linkedin_url = db.Column(db.String(50))
    insta_url = db.Column(db.String(50))
    recruitor_code = db.Column(db.String(50))


class Userresume(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(15))
    contactno = db.Column(db.Integer)
    emailaddr = db.Column(db.String(50))
    linkedin_url = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    pfs1 = db.Column(db.String(15))
    pfs2 = db.Column(db.String(15))
    pfs3 = db.Column(db.String(15))
    pfs4 = db.Column(db.String(15))
    pfs5 = db.Column(db.String(15)) 
    interest = db.Column(db.String(200))
    l1 = db.Column(db.String(15))
    l2 = db.Column(db.String(15))
    l3 = db.Column(db.String(15))
    exp_joining_year = db.Column(db.Integer)
    exp_company_name = db.Column(db.String(50))
    exp_job_title = db.Column(db.String(50))
    exp_job_desc = db.Column(db.String(200))
    profile_desc = db.Column(db.String(200))
    name = db.Column(db.String(50))
    job_title = db.Column(db.String(50))
    percentage10 = db.Column(db.Integer)
    institute10 = db.Column(db.String(50))
    board10 = db.Column(db.String(50))
    percentage12 = db.Column(db.Integer)
    institute12 = db.Column(db.String(50))
    board12 = db.Column(db.String(50)) 
    others_education = db.Column(db.String(200))   

class Applicationlist(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(50))
    company_email = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow) 
    recruitor_code = db.Column(db.String(50))

class Messages(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    user_ka_naam = db.Column(db.String(50))
    company_ka_email = db.Column(db.String(50))
    message = db.Column(db.String(500))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user_type = request.form['user-type']
        if user_type == "user":
            user = User.query.filter_by(username=form.username.data).first()
            if user:
                if check_password_hash(user.password, form.password.data):
                    cursor1 = connection1.cursor()
                    cursor1.execute("SELECT * FROM 'Jobcompany' ")
                    companies = cursor1.fetchall()
                    cursor1.execute("SELECT * FROM 'Jobcategory' ")
                    categories = cursor1.fetchall()
                    # return render_template("index1.html",user = user , companies =    companies , categories = categories)
                    return redirect(f'/main-index/{user.username}/user')
        elif user_type == "recruitor":
            recruitor = Recruitor.query.filter_by(username=form.username.data).first()
            if recruitor:
                if check_password_hash(recruitor.password, form.password.data):
                    cursor1 = connection1.cursor()
                    cursor1.execute("SELECT * FROM 'Jobcompany' ")
                    companies = cursor1.fetchall()
                    cursor1.execute("SELECT * FROM 'Jobcategory' ")
                    categories = cursor1.fetchall()
                    # return render_template("index1.html",user = user , companies =    companies , categories = categories)
                    return redirect(f'/main-index/{recruitor.username}/recruit')
        
        
        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/main-index/<usr>/<num>')
def main_index(usr,num):
    if num == "user":
        user = User.query.filter_by(username= usr).first()
        cursor1 = connection1.cursor()
        cursor1.execute("SELECT * FROM 'Jobcompany' ")
        companies = cursor1.fetchall()
        cursor1.execute("SELECT * FROM 'Jobcategory' ")
        categories = cursor1.fetchall()
        return render_template("index1.html" , user = user, companies = companies ,     categories = categories , user_type =num)
    elif num == "recruit":
        recruitor = Recruitor.query.filter_by(username = usr).first()
        cursor1 = connection1.cursor()
        cursor1.execute("SELECT * FROM 'Jobcompany' ")
        companies = cursor1.fetchall()
        cursor1.execute("SELECT * FROM 'Jobcategory' ")
        categories = cursor1.fetchall()
        return render_template("index1.html" , user = recruitor, companies = companies ,     categories = categories , user_type = num)
    
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        user_type = request.form['user-type']
        if user_type == "user":
            new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            new_resume = Userresume(username = form.username.data)
            db.session.add(new_resume)
            db.session.commit()
        elif user_type == "recruitor":
            res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 20))
            new_recruitor = Recruitor(username=form.username.data, email=form.email.data, password=hashed_password, recruitor_code = str(res))
            db.session.add(new_recruitor)
            db.session.commit()

        return redirect(url_for('login'))
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)



@app.route('/', methods = ['GET'])
def user_profile():
    a = request.args.get('a')
    user = User.query.filter_by(username= a ).first()
    cursor1 = connection1.cursor()
    cursor1.execute("SELECT * FROM 'Jobcompany' ")
    companies = cursor1.fetchall()
    cursor1.execute("SELECT * FROM 'Jobcategory' ")
    categories = cursor1.fetchall()
      
    return render_template('user-dashboard.html' , user = user , categories = categories , companies = companies)

@app.route('/recruitor-dashboard/<a>', methods = ['GET'])
def recruitor_profile(a):
    recruitor = Recruitor.query.filter_by(username= a ).first()
    cursor1 = connection1.cursor()
    cursor1.execute("SELECT * FROM 'Jobcompany' ")
    companies = cursor1.fetchall()
    cursor1.execute("SELECT * FROM 'Jobcategory' ")
    categories = cursor1.fetchall()
      
    return render_template('recruitor-dashboard.html' , recruitor = recruitor , categories = categories , companies = companies)
   
@app.route('/viewprofile', methods=['GET'])
def user_view_profile():
    b = request.args.get('b')
    user = User.query.filter_by(username = b).first()
    cursor1 = connection1.cursor()
    cursor1.execute("SELECT * FROM 'Jobcompany' ")
    companies = cursor1.fetchall()
    cursor1.execute("SELECT * FROM 'Jobcategory' ")
    categories = cursor1.fetchall()
    return render_template('user-view-profile.html', user = user , categories = categories , companies = companies)

@app.route('/recruitor-viewprofile/<b>', methods=['GET'])
def recruitor_view_profile(b):
    recruitor = Recruitor.query.filter_by(username = b).first()
    cursor1 = connection1.cursor()
    cursor1.execute("SELECT * FROM 'Jobcompany' ")
    companies = cursor1.fetchall()
    cursor1.execute("SELECT * FROM 'Jobcategory' ")
    categories = cursor1.fetchall()
    return render_template('recruitor-view-profile.html', recruitor = recruitor , categories = categories , companies = companies)


@app.route('/updateprofile/<c>', methods=['GET', 'POST'])
def update_profile(c):
    if request.method == 'POST':
        username1 = request.form['user-name']
        emailaddreass1 = request.form['email-addreass']
        jobtitle1 = request.form['job-title']
        phonenumber1 = request.form['phone-number']
        websiteurl1 = request.form['website-url']
        userage1 = request.form['user-age']
        educationlevel1 = request.form['education-level']
        userexperience1 = request.form['user-experience']
        userdescription1 = request.form['user-description']
        usercity1 = request.form['user-city']
        usercountry1 = request.form['user-country']
        useraddreass1 = request.form['user-addreass']
        facebookurl1 = request.form['facebook-url']
        twitterurl1 = request.form['twitter-url']
        linkedinurl1 = request.form['linkedin-url']
        instaurl1 = request.form['insta-url']

        user = User.query.filter_by(username = c).first()
        user.username = username1
        user.email = emailaddreass1
        user.job_title = jobtitle1
        user.phone = phonenumber1
        user.website_url = websiteurl1
        user.age = userage1
        user.education_lvl = educationlevel1
        user.experience = userexperience1
        user.description = userdescription1
        user.user_city = usercity1
        user.user_country = usercountry1
        user.user_addreass = useraddreass1
        user.facebook_url = facebookurl1
        user.twitter_url = twitterurl1
        user.linkedin_url = linkedinurl1
        user.insta_url = instaurl1
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_view_profile', b = user.username) )


    user = User.query.filter_by(username = c).first()
    cursor1 = connection1.cursor()
    cursor1.execute("SELECT * FROM 'Jobcompany' ")
    companies = cursor1.fetchall()
    cursor1.execute("SELECT * FROM 'Jobcategory' ")
    categories = cursor1.fetchall()
    return render_template('user-update-profile.html', user = user , companies = companies ,categories = categories)

@app.route('/recruitor-updateprofile/<c>', methods=['GET', 'POST'])
def recruitor_update_profile(c):
    if request.method == 'POST':
        username1 = request.form['user-name']
        emailaddreass1 = request.form['email-addreass']
        jobtitle1 = request.form['job-title']
        phonenumber1 = request.form['phone-number']
        websiteurl1 = request.form['website-url']
        userage1 = request.form['user-age']
        educationlevel1 = request.form['education-level']
        userexperience1 = request.form['user-experience']
        userdescription1 = request.form['user-description']
        usercity1 = request.form['user-city']
        usercountry1 = request.form['user-country']
        useraddreass1 = request.form['user-addreass']
        facebookurl1 = request.form['facebook-url']
        twitterurl1 = request.form['twitter-url']
        linkedinurl1 = request.form['linkedin-url']
        instaurl1 = request.form['insta-url']

        recruitor = Recruitor.query.filter_by(username = c).first()
        recruitor.username = username1
        recruitor.email = emailaddreass1
        recruitor.job_title = jobtitle1
        recruitor.phone = phonenumber1
        recruitor.website_url = websiteurl1
        recruitor.age = userage1
        recruitor.education_lvl = educationlevel1
        recruitor.experience = userexperience1
        recruitor.description = userdescription1
        recruitor.user_city = usercity1
        recruitor.user_country = usercountry1
        recruitor.user_addreass = useraddreass1
        recruitor.facebook_url = facebookurl1
        recruitor.twitter_url = twitterurl1
        recruitor.linkedin_url = linkedinurl1
        recruitor.insta_url = instaurl1
        
        db.session.add(recruitor)
        db.session.commit()
        return redirect(url_for('recruitor_view_profile', b = recruitor.username) )


    recruitor = Recruitor.query.filter_by(username = c).first()
    cursor1 = connection1.cursor()
    cursor1.execute("SELECT * FROM 'Jobcompany' ")
    companies = cursor1.fetchall()
    cursor1.execute("SELECT * FROM 'Jobcategory' ")
    categories = cursor1.fetchall()
    return render_template('recruitor-update-profile.html', recruitor = recruitor , companies = companies ,categories = categories)

@app.route('/update-resume/<d>', methods = ['POST','GET'])
def resume(d):
    if request.method == 'POST':
        # username3 = request.form['username3']
        print("sdfdagdfandgahbfadbdfagfhagdhfdhadfhtadhadgdb")
        email3 = request.form['email3']
        myname3 = request.form['myname3']
        jobtitle3 = request.form['jobtitle3']
        phonenumber3 = request.form['phonenumber3']
        linkedinurl3 = request.form['linkedinurl3']
        mydescription3 = request.form['mydescription3']
        city3 = request.form['city3']
        state3 = request.form['state3']
        s1 = request.form['s1']
        s2 = request.form['s2']
        s3 = request.form['s3']
        s4 = request.form['s4']
        s5 = request.form['s5']
        joinyear3 = request.form['joinyear3']
        compname3 = request.form['compname3']
        title3 = request.form['title3']
        compexp3 = request.form['compexp3']
        l1 = request.form['l1']
        l2 = request.form['l2']
        l3 = request.form['l3']
        percentage103 = request.form['percentage10']
        institute103 = request.form['institute10']
        board103 = request.form['board10']
        percentage123 = request.form['percentage12']
        institute123 = request.form['institute12']
        board123 = request.form['board12']
        other3 = request.form['other3']
        otherinterest3 = request.form['otherinterest3']

        resume = Userresume.query.filter_by(username = d).first()
        resume.emailaddr = email3
        resume.name = myname3
        resume.job_title = jobtitle3
        resume.contactno = phonenumber3
        resume.linkedin_url = linkedinurl3
        resume.profile_desc = mydescription3
        resume.city = city3
        resume.state = state3
        resume.pfs1 = s1
        resume.pfs2 = s2
        resume.pfs3 = s3
        resume.pfs4 = s4
        resume.pfs5 = s5
        resume.exp_joining_year = joinyear3
        resume.exp_company_name = compname3
        resume.exp_job_title = title3
        resume.exp_job_desc = compexp3
        resume.l1= l1
        resume.l2 = l2
        resume.l3 = l3
        resume.percentage10 = percentage103
        resume.institute10 = institute103
        resume.board10 = board103
        resume.percentage12 = percentage123
        resume.institute12 = institute123
        resume.board12 = board123
        resume.others_education = other3
        resume.interest = otherinterest3
        print(resume.job_title)
        db.session.add(resume)
        db.session.commit()

        
    user = User.query.filter_by(username = d).first()
    print("dgfdgh45454545454545454545454545454545454")
    resume = Userresume.query.filter_by(username = d).first()
    cursor1 = connection1.cursor()
    cursor1.execute("SELECT * FROM 'Jobcompany' ")
    companies = cursor1.fetchall()
    cursor1.execute("SELECT * FROM 'Jobcategory' ")
    categories = cursor1.fetchall()
    return render_template('update-resume.html', user = user , resume = resume , categories = categories , companies = companies)


@app.route('/show-resume/<e>')
def viewresume(e):
    resume = Userresume.query.filter_by(username = e).first()
    return render_template('resume.html' , resume = resume)

@app.route('/applyjob/<f>/<g>/<code>' , methods = ['POST','GET'])
def applyjobbtch(f,g,code):
    application = Applicationlist(
        username = f,
        company_email = g,
        recruitor_code = code,
    )
    db.session.add(application)
    db.session.commit()
    user = User.query.filter_by(username= f).first()
    cursor1 = connection1.cursor()
    cursor1.execute("SELECT * FROM 'Jobcompany' ")
    companies = cursor1.fetchall()
    cursor1.execute("SELECT * FROM 'Jobcategory' ")
    categories = cursor1.fetchall()
    return render_template("index1.html" , user = user, companies = companies ,     categories = categories , user_type = "user" , applied = "yes")

@app.route('/my-applied-jobs/<m>')
def my_applied_jobs(m):
    user = User.query.filter_by(username = m).first()
    appliedjobs = Applicationlist.query.filter_by(username = user.username)
    cursor1 = connection1.cursor()
    cursor1.execute("SELECT * FROM 'Jobcompany' ")
    companies = cursor1.fetchall()
    cursor1.execute("SELECT * FROM 'Jobcategory' ")
    categories = cursor1.fetchall()
    jobdetails = []
    for job in appliedjobs:
        # print(job.company_email)
        cursor1 = connection1.cursor()
        cursor1.execute(f"SELECT * FROM Joblist WHERE email = '{job.company_email}' ")
        jobdetail = cursor1.fetchall()
        jobdetails.append(jobdetail)
    print(jobdetails[0][0][7])
    return render_template('user-applied-jobs.html' , user = user , jobdetails = jobdetails , categories = categories , companies = companies )

@app.route('/my-applied-jobs/delete/<usr>/<email>')
def delete_user_applied_job(usr,email):
    job = Applicationlist.query.filter_by(username = usr,company_email = email).first()
    db.session.delete(job)
    db.session.commit()
    return redirect(f'/my-applied-jobs/{usr}')

@app.route('/your-messages/<z>')
def user_messages(z):
    user = User.query.filter_by(username = z).first()
    messages = Messages.query.filter_by(user_ka_naam = user.username)
    joblist = []
    cursor1 = connection1.cursor()
    cursor1.execute("SELECT * FROM 'Jobcompany' ")
    companies = cursor1.fetchall()
    cursor1.execute("SELECT * FROM 'Jobcategory' ")
    categories = cursor1.fetchall()
    for message in messages:
        cursor = connection1.cursor()
        cursor.execute(f"SELECT * FROM 'Joblist' WHERE email = '{message.company_ka_email}' ")
        job = cursor.fetchall()
        joblist.append(job)
        

    length = len(joblist)
    return render_template('user-messages.html' , user = user , joblist = joblist , length = length , messages = messages , companies = companies , categories = categories)


@app.route('/reject-application/<usr>/<email>/<rec_username>')
def reject_application(usr , email , rec_username):
    message = Messages(
        user_ka_naam = usr,
        company_ka_email = email,
        message = "Your Application for this job has been rejected,please try again in some other job and dont lose hope.",
        date_created = datetime.now(),
    )
    db.session.add(message)
    db.session.commit()
    job = Applicationlist.query.filter_by(username = usr,company_email = email).first()
    db.session.delete(job)
    db.session.commit()
    return render_template('recruitor-reject-alert.html')

@app.route('/change-password/<usr>')
def change_password(usr):
    user = User.query.filter_by(username = usr).first()
    cursor1 = connection1.cursor()
    cursor1.execute("SELECT * FROM 'Jobcompany' ")
    companies = cursor1.fetchall()
    cursor1.execute("SELECT * FROM 'Jobcategory' ")
    categories = cursor1.fetchall()
    return render_template('changepassword-1.html' , categories = categories , companies = companies , user = user)

@app.route('/change-password/gfgf/<rec_usr>')
def rec_change_password(rec_usr):
    recruitor = Recruitor.query.filter_by(username = rec_usr).first()
    cursor1 = connection1.cursor()
    cursor1.execute("SELECT * FROM 'Jobcompany' ")
    companies = cursor1.fetchall()
    cursor1.execute("SELECT * FROM 'Jobcategory' ")
    categories = cursor1.fetchall()
    return render_template('changepassword-2.html' , categories = categories , companies = companies , recruitor = recruitor)


@app.route('/main-home-page')
def main_home_page():
    return render_template('index-3.html')
if __name__ == '__main__':
    app.run(debug=True,port = 9555)