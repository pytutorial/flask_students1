from flask import Flask, request, render_template

students = [
    {'studentNo': '10001', 'studentName': 'Student 1'},
    {'studentNo': '10002', 'studentName': 'Student 2'},    
]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', students=students)
    
app.run(debug=True)
