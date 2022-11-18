from flask import Flask, render_template, redirect, session, request, flash

app = Flask(__name__)
app.secret_key='this is secret'

@app.route('/')
def index():
    return render_template("form.html")


@app.route('/process', methods=['POST'])
def process():
    session['name']= request.form['name']
    session['location']= request.form['location']
    session['language']= request.form['language']
    session['comment']= request.form['comment']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/goBack')
def goBack():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)