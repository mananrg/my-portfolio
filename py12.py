
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, render_template	
projects=[
    {'1':{'title':"ChatGPT Mobile Application",'Description':"Designed a mobile application in ChatGPT","Tools":"Flutter, Dart, Firebase, OpenAI",'img':"../static/images/chatbot.png"}
     },
         {'2':{'title':"Solar Educational Application",'Description':"Android application made using Flutter","Tools":"Flutter, Dart",'img':"../static/images/solarpanel.png"}
     },
         {'3':{'title':"Raspberrypi WebServer",'Description':"Designed a webserver with custom Mods and Firebase","Tools":"Flask, Python, HTML, CSS",'img':"../static/images/piserver.png"}
     },
]
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
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
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
