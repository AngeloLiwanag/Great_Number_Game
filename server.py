from flask import Flask, render_template, request, redirect, session
import random

app = Flask (__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():
    if not 'random' in session:
        session['random'] = random.randint(0,100) 
    if not 'guess' in session:
        session['guess'] = 0
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True)