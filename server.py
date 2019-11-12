from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
import re	# the regex module
app = Flask(__name__)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
@app.route("/")
def index():
    return render_template("index.html")
            
#@app.route('/process', methods=['POST'])
#def submit():
#    if not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern
#        flash("Invalid email address!")
#        return redirect("/")
#    else:
#        return redirect("/success")

@app.route('/success', methods=['POST'])
def success():
    email_for_form = request.form['email']
    mysql = connectToMySQL('email')
    query = "INSERT INTO email (email) VALUES (%(e)s);"
    data = {
    
        "e": request.form['email']
        
    }
    email = mysql.query_db('SELECT * FROM email;')
    print(email)
    return render_template("success.html", all_email=email, email_on_template=email_for_form)

if __name__ == "__main__":
    app.run(debug=True)
