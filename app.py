from flask import Flask, render_template, request ,redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''  # Replace with your MySQL password
app.config['MYSQL_DATABASE_DB'] = 'providentfundsandfurnishing'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

con = mysql.connect()
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS providentfund (id INT AUTO_INCREMENT PRIMARY KEY, mr_ms_mrs text, name text, dateofbirth date, fatherandhusband text, relationinrespect text, gender text, mobilenumber integer, email text, emppovidentfunds text, emppensionscheme text, uaborprevious text, account text, dateofexit date, certificateissued text, pensionpayment text, internationworker text, india text, otherthanindia text, passport text,  passportfrom date , passportto date, educationalqualification text, maritalstatus varchar(225), specially varchar(225), category varchar(225), bankkycnumber text, banknumber text, bankremark text, nprkycnumber text, nprnumber text, nprremark text, permanentkycnumber text, permanentnumber text,  permanentremark text, passportkycnumber text, passportnumber text, passportremark text, drivinglicencekycnumber text, drivinglicencenumber text , drivinglicenceremark text, electioncardkycnumber text, electioncardnumber text, electioncardremark text,  rationcardkycnumber text, rationcardnumber text, rationcardremark text, esiccardkycnumber text, esiccardnumber text, esiccardremark text)")
cur.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY , username text , password text)")
cur.execute("CREATE TABLE IF NOT EXISTS informationform (id INT AUTO_INCREMENT PRIMARY KEY , first_name text, middle_name text, surname text, employee_code text, reporting_manager text, department text, permanent_address text, PostalCodeorPinCode text, Present_Address text, dateofbirth date, sex text, birthplace text, bloodgroup text, nationality text, religion text,  pan text, language text, maritalstatus text, marriage_date date, spouse_name text, spouse_dob date, children_count text, first_child_name text, first_child_dob date,  second_child_name text, second_child_dob date, third_child_name text,  third_child_dob date, contact_number text,  mobile_number text, emergency_contact text, email_id text, SSCName text, SSCSpecialization text, SSCSPassingYearMonth date, SSCPercentage text, SSCGrade text, HSCName text, HSCSpecialization text,    HSCPassingYearMonth date, HSCPercentage text , HSCGrade text, GraduationName text, GraduationSpecialization text,   GraduationPassingYearMonth date, GraduationPercentage text, GraduationGrade text, DiplomaName text, DiplomaSpecialization text, DiplomaPassingYearMonth date, DiplomaPercentage text, DiplomaGrade text, DegreeName text, DegreeSpecialization text,  DegreePassingYearMonth date, DegreePercentage text, DegreeGrade text, MastersorPostGraduationName text , MastersorPostGraduationSpecialization text,  MastersorPostGraduationPassingYearMonth date, MastersorPercentage text, MastersorGrade text, DoctorateName text, DoctorateSpecialization text,  DoctoratePassingYearMonth date, DoctoratePercentage text, DoctorateGrade text, OthersName text, OthersSpecialization text,   OthersPassingYearMonth date,  OthersPercentage text, OthersGrade text, aOrganization text, aDesignation text, aLocation text, aDurationfrom date, aDurationto date, bOrganization text, bDesignation text, bLocation text, bDurationfrom date, bDurationto date, cOrganization text, cDesignation text, cLocation text, cDurationfrom date, cDurationto date, dOrganization text, dDesignation text, dLocation text, dDurationfrom date, dDurationto date, eOrganization text, eDesignation text, eLocation text, eDurationfrom date, eDurationto date, todaydate date)")
con.commit()
cur.close()
con.close()

@app.route('/')
def index():
    return render_template("loginpage.html")



@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        psw = request.form['psw']
        try:
            con = mysql.connect()
            cur = con.cursor()
            # print(f"Attempting to log in with username: {uname}, password: {psw}")
            cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (uname, psw))
            data = cur.fetchone()
            cur.close()
            con.close()
            # print(f"Query result: {data}")
            if data:
                return render_template("homepage.html")
            else:
                return "Login failed. Please check your username and password."
        except mysql.connector.Error as err:
            return f"MySQL Error: {err}"
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return render_template("loginpage.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")


    


        





@app.route('/homepage')
def homepage():
    return render_template("homepage.html")  

@app.route('/form')
def form():
    return render_template("form11.html")

@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
            choice1 = request.form['choice1']
            name1 = request.form['name1']
            dob = request.form['dob']
            fatherandhusband = request.form['fatherandhusband']
            choice3 = request.form['choice3']
            choice4 = request.form['choice4']
            mobile = request.form['mobile']
            email = request.form['email']
            choice5 = request.form['choice5']
            choice6 = request.form['choice6']
            choice7 = request.form['choice7']
            previousemployment = request.form['previousemployment']
            dateprevious = request.form['dateprevious']
            certificateforpreviousemployment = request.form['certificateforpreviousemployment']
            persionpayment = request.form['persionpayment']
            internationalworker = request.form['internationalworker']
            india = request.form['india']
            otherindia = request.form['otherindia']
            passportnumber = request.form['passportnumber']
            passportvalid = request.form['passportvalid']
            passportvalid1 = request.form['passportvalid1']
            educationalqualification = request.form.get('educationalqualification')
            maritalstatus = request.form.get('maritalstatus')
            specially = request.form.get('specially')
            abled =request.form.get('abled')  # Convert list to string
            bankkycnumber = request.form['bankkycnumber']
            banknumber = request.form['banknumber']
            bankremark = request.form['bankremark']
            nprkycnumber = request.form['nprkycnumber']
            nprnumber = request.form['nprnumber']
            nprremark = request.form['nprremark']
            permanentkycnumber = request.form['permanentkycnumber']
            permanentnumber = request.form['permanentnumber']
            permanentremark = request.form['permanentremark']
            passportkycnumber = request.form['passportkycnumber']
            passportnumber = request.form['passportnumber']
            passportremark = request.form['passportremark']
            drivinglicencekycnumber = request.form['drivinglicencekycnumber']
            drivinglicencenumber = request.form['drivinglicencenumber']
            drivinglicenceremark = request.form['drivinglicenceremark']
            electioncardkycnumber = request.form['electioncardkycnumber']
            electioncardnumber = request.form['electioncardnumber']
            electioncardremark = request.form['electioncardremark']
            rationcardkycnumber = request.form['rationcardkycnumber']
            rationcardnumber = request.form['rationcardnumber']
            rationcardremark = request.form['rationcardremark']
            esiccardkycnumber = request.form['esiccardkycnumber']
            esiccardnumber = request.form['esiccardnumber']
            esiccardremark = request.form['esiccardremark']

            # Insert data into the table
            con = mysql.connect()
            cur = con.cursor()
            cur.execute("""
    INSERT INTO providentfund (
        mr_ms_mrs, name, dateofbirth, fatherandhusband, relationinrespect, gender, 
        mobilenumber, email, emppovidentfunds, emppensionscheme, uaborprevious, account, 
        dateofexit, certificateissued, pensionpayment, internationworker, india, otherthanindia, 
        passport, passportfrom, passportto, educationalqualification, maritalstatus, specially, 
        category, bankkycnumber, banknumber, bankremark, nprkycnumber, nprnumber, nprremark, 
        permanentkycnumber, permanentnumber, permanentremark, passportkycnumber, passportnumber, 
        passportremark, drivinglicencekycnumber, drivinglicencenumber, drivinglicenceremark, 
        electioncardkycnumber, electioncardnumber, electioncardremark, rationcardkycnumber, 
        rationcardnumber, rationcardremark, esiccardkycnumber, esiccardnumber, esiccardremark
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s
    )
""", (
    choice1, name1, dob,fatherandhusband, choice3, choice4, mobile, email, choice5, choice6, choice7, 
    previousemployment,dateprevious, certificateforpreviousemployment, persionpayment, internationalworker, 
    india, otherindia, passportnumber, passportvalid, passportvalid1, educationalqualification, 
    maritalstatus, specially, abled, bankkycnumber, banknumber, bankremark, nprkycnumber, 
    nprnumber, nprremark, permanentkycnumber, permanentnumber, permanentremark, passportkycnumber, 
    passportnumber, passportremark, drivinglicencekycnumber, drivinglicencenumber, 
    drivinglicenceremark, electioncardkycnumber, electioncardnumber, electioncardremark, 
    rationcardkycnumber, rationcardnumber, rationcardremark, esiccardkycnumber, esiccardnumber, 
    esiccardremark
))

            con.commit()
            return 'User added successfully!'

    else: return 'fail'
    return redirect('/')

@app.route('/forms')
def forms():
    return render_template("form12.html")

@app.route('/informationform')
def informationform():
    return render_template("informationform.html")


# @app.route('/informationforminsert', methods=['POST'])
# def informationforminsert():
#     if request.method=='POST':
#        first_name=request.form["first_name"]
#        middle_name=request.form["middle_name"]
#        surname=request.form["surname"]
       
#         # try:
            
#             # con = mysql.connect()
#             # cur = con.cursor()
#             # cur.execute("insert")
            



@app.route('/newjoining')
def newjoining():
    return render_template("newjoining.html")

if __name__ == '__main__':
    app.run(debug=True)
