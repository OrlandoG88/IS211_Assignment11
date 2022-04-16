from flask import render_template, Flask, request, redirect
import re


app = Flask(__name__)
to_do =[]

class Task():
    def __init__(self, task, email, priority):
        self.task = task
        self.email = email
        self.priority = priority

@app.route('/')
def display_list():

    return render_template('index.html', to_do=to_do)

@app.route('/submit', methods=['POST'])
def submit():
    global message
    global to_do
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    if task == '':
        message = 'Unable to Add Task - Task Field is Blank'
        return redirect("/")

    email_reg = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

    if email == '':
        message = 'Unable to Add Task - Email Field is Blank'
        return redirect("/")

    elif not re.search(email_reg, email):
        message = 'Unable to Add Task - Email Format is Not Valid'
        return redirect("/")

    if priority == 'Blank':
        message = 'Unable to Add Task - Priority Was Not Set'
        return redirect("/")

    new_task = Task(task, email, priority)

    to_do.append(new_task)
    message = ''

    return redirect("/")


@app.route('/clear', methods=['POST'])
def clear():
    global to_do
    global message

    to_do = []
    message = ''

    return redirect("/")



if __name__ == '__main__':
    app.run()