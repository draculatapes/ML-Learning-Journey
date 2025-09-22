from flask import Flask 
'''
it create an instance of the Flask calss, 
whifch will be the WSGI(Web Server Gateway Interface) application

'''
##WSGI Application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html> <H1>Hello This is Amarjeet's Website</H1> </html>"
@app.route("/index")
def indexWelcome():
    return 'welcome to this Flask course. we are in index page'


if __name__=="__main__": ## entry point of any .py file 
    app.run(debug=True)