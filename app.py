from flask import Flask, render_template, request, session, escape,redirect, url_for, flash, g, send_from_directory, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

import os
import hashlib

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpge", "gif", "pdf"])

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy(app)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS #

def get_profile_picture(email):
    size = 512
    utec = "https://2.bp.blogspot.com/-FFVPfgAwfW4/Wp3BRQ2NiSI/AAAAAAAAK80/1NpK6c_nAawu5cjCzi6dn_ETT0eIGrYiQCLcBGAs/s1600/UTEC.png" + hashlib.md5(email.encode("utf-8").lower()).hexdigest() + "?"

    return utec


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())

class Users(Base):
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    about_me = db.Column(db.String(280), default="")
    images = db.relationship("Image", backref="owner", lazy="dynamic")

class Image(Base):
    filename = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    owner_username = db.Column(db.String(50), nullable=False)

@app.before_request
def before_request():
    if "username" in session:
        g.user = session["username"]
    else:
        g.user = None

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/search")
def search():
    username = request.args.get("username")

    return redirect(url_for("profile", username=username))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if not g.user:
        if request.method == "POST":
            username = Users.query.filter_by(username=request.form["username"].lower()).first()
            email = Users.query.filter_by(email=request.form["email"].lower()).first()

            if username or email:
                flash("Ese nombre o email ya esta en uso", "alert-warning")

                return redirect(request.url)
            hashed_pw = generate_password_hash(request.form["password"], method="sha256")
            new_user = Users(username=request.form["username"].lower(),email=request.form["email"].lower(), password=hashed_pw)
            db.session.add(new_user)
            db.session.commit()

            flash("Te has registrado exitosamente", "alert-success")

            return redirect(url_for("login"))

        return render_template("signup.html")
    flash("Ya estas registrado", "alert-primary")

    return redirect(url_for("home"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if not g.user:
        if request.method == "POST":
            user = Users.query.filter_by(username=request.form["username"].lower()).first()
            if user and check_password_hash(user.password, request.form["password"]):
                session["username"] = user.username
                flash("Ya se ha autentificado", "alert-success")
                return redirect("home")
            flash("Tus credenciales son invalidas", "alert-warning")

        return render_template("login.html")
    flash("Necesitas loggearte.", "alert-primary")

    return redirect(url_for("home"))

@app.route("/profile/<username>")
def profile(username):
    user = Users.query.filter_by(username=username).first()

    if user:
        files = user.images.order_by(Image.date_modified).limit(10).all()
        picture = get_profile_picture(user.email)

        return render_template("profile.html", user=user, files=files, picture=picture)
    
    abort(404)

@app.route("/profile/edit", methods=["GET", "POST"])
def edit_profile():
    user = Users.query.filter_by(username=g.user).first()

    if request.method == "POST":
        user.about_me = request.form["about"]
        db.session.commit()

        flash("Los cambios han sido guardados exitosamente", "alert-success")
        return redirect(url_for("profile", username=g.user))

    return render_template("edit_profile.html", user=user)

@app.route("/home", methods=["GET", "POST"])
def home():
    if g.user:
        if request.method == "POST":
            if "file" not in request.files:
                flash("ninguna parte del archivo", "alert-danger")
                return redirect(request.url)
            file = request.files["file"]
            if file.filename == "":
                flash("No hay archivo", "alert-warning")
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                user = Users.query.filter_by(username=g.user).first()
                file_to_db = Image(filename=filename, owner=user, \
                                owner_username=user.username)
                db.session.add(file_to_db)
                db.session.commit()
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                return redirect(url_for("get_files"))
        return render_template("home.html")
    flash("Debes registrarte", "alert-warning")

    return redirect(url_for("login"))

@app.route("/files")
def get_all_files():
    files = Image.query.order_by(Image.date_modified).limit(200).all()

    return render_template("files.html", files=files)


@app.route("/myfiles")
def get_files():
    if g.user:
        user = Users.query.filter_by(username=g.user).first()

        if user.images.all():
            files = user.images.order_by(Image.date_modified).all()
            return render_template("my_files.html", files=files)
        
        files = []
        return render_template("my_files.html", files=files)

    flash("Debes registrarte", "alert-warning")

    return redirect(url_for("login"))

@app.route('/uploads/<filename>')
def uploaded_file(filename):

    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Ya no estas loggeado", "alert-secondary")

    return redirect(url_for("index"))

@app.route("/about")
def about():

    return render_template("about.html")
    
@app.errorhandler(404)
def page_not_found(error):

    return render_template("404_page_not_found.html"), 404

if __name__ == "__main__":
    db.create_all()
    app.run()
