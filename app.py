from flask import Flask, render_template, request
from  flask_mysqldb import MySQL
from datetime import datetime


app = Flask(__name__)

app.config['MySQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mohamed2003'
app.config['MYSQL_DB'] = 'Salaries'
mysql = MySQL(app)

@app.route('/')
def Homepage():
    return render_template('index.html')

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        job_title = request.form.get('jobTitle')
        years_of_experience = request.form.get('yearsOfExperience')
        salary = request.form.get('salary')
        payment_date = request.form.get('paymentDate')
        work_location = request.form.get('workLocation')
        work_type = request.form.get('workType')
        work_hour = request.form.get('workHour')
        city_of_company_site = request.form.get('cityOfCompanySite')
        current_time_str = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
        current_time_obj = datetime.strptime(current_time_str, '%Y-%m-%d %I:%M:%S %p')


        # Convert values to a tuple
        data = (job_title, years_of_experience, salary, payment_date, work_location, work_type, work_hour, city_of_company_site,current_time_obj)

        # Insert data into the 'Salaries_In_Egypt_at_2024' table
        insert_query = """INSERT INTO Salaries_In_Egypt_at_2024 (Job_Title,
                                                                Years_of_Experiences,
                                                                Salary, 
                                                                Date_of_Salary,
                                                                work_location,
                                                                Work_Type,
                                                                Work_Hour,
                                                                City_of_Company_site,
                                                                Process_time) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cur = mysql.connection.cursor()
        cur.execute(insert_query, data)
        mysql.connection.commit()
        cur.close()

        return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)