
##Notes:
'''
{{}} expression to print output in html

{%...%} conditon for loops

{# ..# } for comments 
'''

from flask import Flask, render_template, request,redirect,url_for

# It creates an instance of the Flask class,

# which will be your WSGI (Web Server Gateway Interface) application.

###WSGI Application

app=Flask(__name__)

@app.route("/")

def welcome():

    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index", methods=['GET'])

def index():

    return render_template('index.html')

@app.route('/about')

def about():

    return render_template('about.html')



# @app.route('/submit', methods=['GET', 'POST'])
# # def submit():
# #     if request.method=='POST':
# #         name=request.form['name']

# #         return f'Hello {name}!!!!!'

# #     return render_template('form.html')

# #variable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="pass"
    else:
        res='Fail'
    return render_template('result.html',results=res)    

 

#variable rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="pass"
    else:
        res='Fail'
    exp={'score':score,'res':res}
    return render_template('result1.html',results=exp)    


#if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result3.html',results=score)    


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)

@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
        return redirect(url_for('successres',score=int(total_score)))
    return render_template('getresult.html')

if __name__=="__main__":
    print('running server')
    app.run(debug=True)