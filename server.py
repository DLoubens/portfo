from flask import Flask, render_template, url_for, request, redirect
import smtplib
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')
#@app.route('/thanks.html')
#def my_thanks():
  #  return render_template('thanks.html')


#@app.route('/about.html')
#def about():
 #   return render_template('about.html')

#@app.route("/blog")
#def blog():
 # return "It's my first blog!"


def write_to_csv(data):
   with open('database.csv', mode='a') as database2:
      name = data["name"]
      email=data["email"]
      subject=data["subject"]
      message=data["message"]
      csv_writer = csv.writer(database2,delimiter=',', quotechar='|', quoting= csv.QUOTE_MINIMAL)
      csv_writer.writerow([name,email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
   if request.method == 'POST':
      data= request.form.to_dict()
      write_to_csv(data)
      return 'Form Submitted Successfully!'
      #return redirect('/thanks.html')
   else:
      return 'Form Submitted Failure! Please try again'



if __name__ == "__main__":
  app.run(debug=True)
  

