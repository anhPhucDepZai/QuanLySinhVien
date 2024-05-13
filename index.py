from flask import Flask, render_template, request
import dao
app=Flask(__name__)

@app.route("/home")
def home():
    cates = dao.load_menu()
    return render_template('index.html', categories = cates)

@app.route("/student")
def register_student():
    return render_template("student.html")

@app.route("/class")
def register_class():
    return render_template("class.html")
if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)