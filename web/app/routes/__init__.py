from flask import request ,make_response,redirect,render_template ,url_for,flash,session,escape
from app import app,db
from werkzeug.security import generate_password_hash,check_password_hash
from app.schemas.models import Users

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