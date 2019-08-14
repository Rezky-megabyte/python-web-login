from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def dasboard():
   return render_template('dasboard.html') 
@app.route('/index', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'rezky' or request.form['password'] != 'githublogin':
            error = 'Cannot Login,username or password is incoreect.'
        else:
            return redirect(url_for('index1'))
    return render_template('index.html', error=error)
@app.route('/index1')
def index1():
   return render_template('index1.html') 

if __name__ == '__main__':
   app.run(debug = True)