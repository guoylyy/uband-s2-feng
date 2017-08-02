from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    print 'hello world'
    return render_template('test.html')

@app.route('/<string:student_number>/details')
def details(student_number):
    return render_template( str(student_number) + '.html')

if __name__ == '__main__':
    app.run(debug=True)