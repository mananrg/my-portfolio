from flask import Flask, redirect, render_template	,request
from sendmail import send_email
from projects import projects

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Replace with your Gmail address
app.config['MAIL_PASSWORD'] = 'your_password'  # Replace with your Gmail password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache'
    return response


@app.route('/')
def hello_world():
    project_titles = []
    project_descriptions = []
    project_tools=[]
    project_img=[]
    for project in projects:
        for key, value in project.items():
            project_titles.append(value['title'])
            project_descriptions.append(value['Description'])
            project_tools.append(value['Tools'])
            project_img.append(value['img'])
    return render_template('index.html',project_titles=project_titles,project_descriptions=project_descriptions,project_tools=project_tools,project_img=project_img)


@app.route('/contactus', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        send_email(name, email, message)
        return 'Thank you for your submission!'
    return render_template('contactus.html')
  


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

