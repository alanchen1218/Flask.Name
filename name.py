from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/process', methods= ['GET','POST'])
def next():
    name = request.form['name']
    name1 = request.form['email']
    print(name, name1)
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)