from flask import request ,make_response,redirect,render_template ,url_for,flash,session,escape
from app import app,db
from werkzeug.security import generate_password_hash,check_password_hash
from app.schemas.models import Users
from app.schemas.models import Tareas

@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
    session.pop("username",None)
    if request.method == "POST":
            if request.form["username"]=="" or request.form["email"]=="" or request.form["password"]=="":
                flash('Los campos no deben estar vacios para que te registres')
            else:
                hashed_pw = generate_password_hash(request.form["password"],method="sha256")#sha256 es un metodo de cifrado 
                new_user=Users(username=request.form["username"],email=request.form["email"],password=hashed_pw)
                new_user_tar=Tareas(username=request.form["username"],tarea_1=None,tarea_2=None,tarea_3=None,tarea_4=None,tarea_5=None,
                tarea_6=None,tarea_7=None,tarea_8=None,tarea_9=None,tarea_10=None)
                db.session.add(new_user)
                db.session.add(new_user_tar)
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
        user_tar=Tareas.query.filter_by(username=session["username"]).first()
        flash('Bienvenido '+ session["username"] )
        context_tareas={}
        if user_tar.tarea_1 != "":
            context_tareas['tarea']=user_tar.tarea_1
        

        return render_template('blog_1.html',tarea=user_tar.tarea_1)
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
        nueva_tarea=True
        user=Tareas.query.filter_by(username=session["username"]).first()
        if request.method=='POST':
            if(user.tarea_1==""):
                new_user=Tareas(username=session["username"],tarea_1=request.form["description"],tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=user.tarea_4,
                tarea_5=user.tarea_5,tarea_6=user.tarea_6,tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=user.tarea_1,tarea_10=user.tarea_1)
                db.session.add(new_user)
                db.session.delete(user)
                db.session.commit()
            elif(user.tarea_2==""):
                new_user=Tareas(username=session["username"],tarea_1=user.tarea_1,tarea_2=request.form["description"],tarea_3=user.tarea_3,tarea_4=user.tarea_4,
                tarea_5=user.tarea_1,tarea_6=user.tarea_1,tarea_7=user.tarea_1,tarea_8=user.tarea_1,tarea_9=user.tarea_1,tarea_10=user.tarea_1)
                db.session.add(new_user)
                db.session.delete(user)
                db.session.commit()
            elif(user.tarea_3==""):
                new_user=Tareas(username=session["username"],tarea_1=user.tarea_1,tarea_2=user.tarea_2,tarea_3=request.form["description"],tarea_4=user.tarea_4,
                tarea_5=user.tarea_5,tarea_6=user.tarea_6,tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=user.tarea_9,tarea_10=user.tarea_10)            
                db.session.add(new_user)
                db.session.delete(user)
                db.session.commit()            
            elif(user.tarea_4==""):
                new_user=Tareas(username=session["username"],tarea_1=user.tarea_1,tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=request.form["description"],
                tarea_5=user.tarea_4,tarea_6=user.tarea_6,tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=user.tarea_9,tarea_10=user.tarea_10)
            elif(user.tarea_5==""):
                new_user=Tareas(username=session["username"],tarea_1=user.tarea_1,tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=user.tarea_4,
                tarea_5=request.form["description"],tarea_6=user.tarea_6,tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=user.tarea_9,tarea_10=user.tarea_10)
                db.session.add(new_user)
                db.session.delete(user)
                db.session.commit()            
            elif(user.tarea_6==""):
                new_user=Tareas(username=session["username"],tarea_1=user.tarea_1,tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=user.tarea_4,
                tarea_5=user.tarea_5,tarea_6=request.form["description"],tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=user.tarea_9,tarea_10=user.tarea_10)
                db.session.add(new_user)
                db.session.delete(user)
                db.session.commit()            
            elif(user.tarea_7==""):
                new_user=Tareas(username=session["username"],tarea_1=user.tarea_1,tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=user.tarea_4,
                tarea_5=user.tarea_5,tarea_6=user.tarea_6,tarea_7=request.form["description"],tarea_8=user.tarea_8,tarea_9=user.tarea_9,tarea_10=user.tarea_10)
                db.session.add(new_user)
                db.session.delete(user)
                db.session.commit()

            elif(user.tarea_8==""):
                new_user=Tareas(username=session["username"],tarea_1=user.tarea_1,tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=user.tarea_4,
                tarea_5=user.tarea_5,tarea_6=user.tarea_6,tarea_7=user.tarea_7,tarea_8=request.form["description"],tarea_9=user.tarea_9,tarea_10=user.tarea_10)
            
                db.session.add(new_user)
                db.session.delete(user)
                db.session.commit()            
            elif(user.tarea_9==""):
                new_user=Tareas(username=session["username"],tarea_1=user.tarea_1,tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=user.tarea_4,
                tarea_5=user.tarea_5,tarea_6=user.tarea_6,tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=request.form["description"],tarea_10=user.tarea_10)
                db.session.add(new_user)
                db.session.delete(user)
                db.session.commit()
            elif(user.tarea_10==""):
                new_user=Tareas(username=session["username"],tarea_1=request.form["description"],tarea_2=user.tarea_2,tarea_3=user.tarea_3,tarea_4=user.tarea_4,
                tarea_5=user.tarea_5,tarea_6=user.tarea_6,tarea_7=user.tarea_7,tarea_8=user.tarea_8,tarea_9=user.tarea_9,tarea_10=request.form["description"])
                db.session.add(new_user)
                db.session.delete(user)
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