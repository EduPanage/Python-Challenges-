import os
from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
database_uri = "sqlite:///" + os.path.join(basedir, "todo.sqlite")

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), unique=True, nullable=False)
    
    profile = db.relationship("UserProfile", backref="user", uselist=False)
    tasks = db.relationship("Task", backref="author", lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

class UserProfile(db.Model):
    __tablename__ = "user_profiles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True)

class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    data_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"Task: {self.name}\nDescription: {self.description}\nCreated on: {self.data_created}"

task_categories = db.Table(
    "task_categories",
    db.Column("task_id", db.Integer, db.ForeignKey("tasks.id"), primary_key=True),
    db.Column("category_id", db.Integer, db.ForeignKey("categories.id"), primary_key=True),
)

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    tasks = db.relationship(
        "Task", secondary=task_categories, backref="categories", lazy="dynamic"
    )

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_name = request.form.get('name', 'Tarefa Sem Nome')
        task_desc = request.form.get('description', '')
        task = Task(name=task_name, description=task_desc, user_id=1)
        try:
            db.session.add(task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"Error: Wasn't able to insert the task! {e}"
    else:
        tasks = Task.query.order_by(Task.data_created).all()
        return render_template("index.html", usuario="eduardo", tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return "Error: Wasn't able to remove the task!"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.description = request.form['description']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Error: Wasn't able to update the task!"
    else:
        return render_template('update.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)
