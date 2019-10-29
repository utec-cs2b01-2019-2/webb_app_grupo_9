from flask import Flask ,request ,make_response,redirect,render_template ,url_for,flash,session,escape
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
import os


dbdir="sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
db=SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"]=dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

class Users(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),unique=True,nullable=False)
    email=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(80),nullable=False)
    tarea_1=db.Column(db.String(80),nullable=True)
    tarea_2=db.Column(db.String(80),nullable=True)
    tarea_3=db.Column(db.String(80),nullable=True)
    tarea_4=db.Column(db.String(80),nullable=True)
    tarea_5=db.Column(db.String(80),nullable=True)
    tarea_6=db.Column(db.String(80),nullable=True)
    tarea_7=db.Column(db.String(80),nullable=True)
    tarea_8=db.Column(db.String(80),nullable=True)
    tarea_9=db.Column(db.String(80),nullable=True)
    tarea_10=db.Column(db.String(80),nullable=True)



@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
    session.pop("username",None)
    if request.method == "POST":
            if request.form["username"]=="" or request.form["email"]=="" or request.form["password"]=="":
                flash('Los campos no deben estar vacios para que te registres')
            else:
                hashed_pw = generate_password_hash(request.form["password"],method="sha256")#sha256 es un metodo de cifrado 
                new_user=Users(username=request.form["username"],email=request.form["email"],password=hashed_pw)
                db.session.add(new_user)
                db.session.commit()   
                flash('REGISTRADO CORRECTAMENTE')

    return render_template('registrarse.html')

@app.route('/')
def index():
    session.pop("username",None)
    return render_template('home.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('error_404.html',error=error)

@app.route('/logout')
def logout():
    session.pop("username",None)
    return redirect(url_for('login'))

    
@app.route('/tareas_app')
def tareas_app():
    if "username" in session:
        user=Users.query.filter_by(username=session["username"]).first()
        flash('Bienvenido '+ session["username"] )
        context_tareas={}
        if user.tarea_1!="":
            context_tareas['tarea']=user.tarea_1
        if user.tarea_2!="":
            context_tareas['tarea']=user.tarea_1
        if user.tarea_3!="":
            context_tareas['tarea']=user.tarea_1
        if user.tarea_4!="":
            context_tareas['tarea']=user.tarea_1
        if user.tarea_5!="":
            context_tareas['tarea']=user.tarea_1
        if user.tarea_6!="":
            context_tareas['tarea']=user.tarea_1
        if user.tarea_7!="":
            context_tareas['tarea']=user.tarea_1
        if user.tarea_8!="":
            context_tareas['tarea']=user.tarea_1
        if user.tarea_9!="":
            context_tareas['tarea']=user.tarea_1
        if user.tarea_10!="":
            context_tareas['tarea']=user.tarea_1
        return render_template('blog_1.html',**context_tareas)
    flash('Debes loggearte primero')
    return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
    session.pop("username",None)
    if request.method=="POST":
        user=Users.query.filter_by(username=request.form["username"]).first()
        if user and check_password_hash(user.password,request.form["password"]):
            session['username']=user.username
            return redirect(url_for('tareas_app'))
        flash('CREDENCIALES INVALIDAS')

    return render_template('login.html')


@app.route('/tareas_app/Editar_tarea',methods=['GET','POST'])
def Editar_tarea():
    if "username" in session:
        return render_template('blog_1.html')
    flash('Debes loggearte primero')
    return render_template('login.html')


@app.route('/tareas_app/Crear_nueva_tarea',methods=['GET','POST'])
def Crear_nueva_tarea():
    if "username" in session:
        user=Users.query.filter_by(username=session["username"]).first()
        nueva_tarea=True
        if request.method=='POST':
            if user.tarea_1=="":
                new_user=Users(username=user.username,email=user.email,password=user.password,tarea_1=request.form["description"],
                tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=user.tarea_4,tarea_5=user.tarea_5,tarea_6=user.tarea_6,
                tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=user.tarea_9,tarea_10=user.tarea_10)
                db.session.delete(user)
                db.session.add(new_user)
                db.session.commit() 

                return redirect(url_for('tareas_app'))
            elif user.tarea_2=="":
                new_user=Users(username=user.username,email=user.email,password=user.password,tarea_1=user.tarea_1,
                tarea_2=request.form["description"],tarea_3=user.tarea_3,tarea_4=user.tarea_4,tarea_5=user.tarea_5,tarea_6=user.tarea_6,
                tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=user.tarea_9,tarea_10=user.tarea_10)
                db.session.delete(user)
                db.session.add(new_user)
                db.session.commit() 

                return redirect(url_for('tareas_app'))
            elif user.tarea_3=="":
                new_user=Users(username=user.username,email=user.email,password=user.password,tarea_1=user.tarea_1,
                tarea_2=user.tarea_2,tarea_3=request.form["description"],tarea_4=user.tarea_4,tarea_5=user.tarea_5,tarea_6=user.tarea_6,
                tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=user.tarea_9,tarea_10=user.tarea_10)
                db.session.delete(user)
                db.session.add(new_user)
                db.session.commit()
                
                return redirect(url_for('tareas_app'))

            elif user.tarea_4=="":
                new_user=Users(username=user.username,email=user.email,password=user.password,tarea_1=user.tarea_1,
                tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=request.form["description"],tarea_5=user.tarea_5,tarea_6=user.tarea_6,
                tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=user.tarea_9,tarea_10=user.tarea_10)
                db.session.delete(user)
                db.session.add(new_user)
                db.session.commit() 

                return redirect(url_for('tareas_app'))
            elif user.tarea_5=="":
                new_user=Users(username=user.username,email=user.email,password=user.password,tarea_1=user.tarea_1,
                tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=user.tarea_4,tarea_5=request.form["description"],tarea_6=user.tarea_6,
                tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=user.tarea_9,tarea_10=user.tarea_10)
                db.session.delete(user)
                db.session.add(new_user)
                db.session.commit() 

                return redirect(url_for('tareas_app'))
            elif user.tarea_6=="":
                new_user=Users(username=user.username,email=user.email,password=user.password,tarea_1=user.tarea_1,
                tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=user.tarea_4,tarea_5=user.tarea_5,tarea_6=request.form["description"],
                tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=user.tarea_9,tarea_10=user.tarea_10)
                db.session.delete(user)
                db.session.add(new_user)
                db.session.commit() 
                return redirect(url_for('tareas_app'))
            elif user.tarea_7=="":
                new_user=Users(username=user.username,email=user.email,password=user.password,tarea_1=user.tarea_1,
                tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=user.tarea_4,tarea_5=user.tarea_5,tarea_6=user.tarea_6,
                tarea_7=request.form["description"],tarea_8=user.tarea_8,tarea_9=user.tarea_9,tarea_10=user.tarea_10)
                db.session.delete(user)
                db.session.add(new_user)
                db.session.commit()                 
                return redirect(url_for('tareas_app'))
            elif user.tarea_8=="":
                new_user=Users(username=user.username,email=user.email,password=user.password,tarea_1=user.tarea_1,
                tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=user.tarea_4,tarea_5=user.tarea_5,tarea_6=user.tarea_6,
                tarea_7=user.tarea_7,tarea_8=request.form["description"],tarea_9=user.tarea_9,tarea_10=user.tarea_10)       
                db.session.delete(user)
                db.session.add(new_user)
                db.session.commit() 
                return redirect(url_for('tareas_app'))
            elif user.tarea_9=="":
                new_user=Users(username=user.username,email=user.email,password=user.password,tarea_1=user.tarea_1,
                tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=user.tarea_4,tarea_5=user.tarea_5,tarea_6=user.tarea_6,
                tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=request.form["description"],tarea_10=user.tarea_10)
                db.session.delete(user)
                db.session.add(new_user)
                db.session.commit() 

                return redirect(url_for('tareas_app'))
            elif user.tarea_10=="":
                new_user=Users(username=user.username,email=user.email,password=user.password,tarea_1=user.tarea_1,
                tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=user.tarea_4,tarea_5=user.tarea_5,tarea_6=user.tarea_6,
                tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=user.tarea_9,tarea_10=request.form["description"])
                db.session.delete(user)
                db.session.add(new_user)
                db.session.commit() 

                return redirect(url_for('tareas_app'))
            
        return render_template('nueva_tarea.html',nueva_tarea=nueva_tarea)
    flash('Debes loggearte primero')
    return render_template('login.html')

@app.route('/tareas_app/Eliminar_tarea',methods=['GET','POST'])
def Eliminar_tarea():
    if "username" in session:
        return render_template('blog_1.html')
    flash('Debes loggearte primero')
    return render_template('login.html')

app.secret_key='..'

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True,port=8000)