from flask import render_template,url_for ,flash ,redirect
from app import app , db , bcrypt
from app.models import User , Post
from app.forms import RegistrationForm , LoginForm
from flask_login import login_user ,current_user , logout_user,login_required


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')




@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()


        flash(f'Account created Successfully, Now You Can login!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registration',form=form)




@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password,form.password.data):
                print("login")
                login_user(user,remember=True) 
                flash('Login successful. {form.email.data}','success')
                return redirect('home')
            else:
                flash('Login unsuccessful. Please check email and Password ','danger')
    return render_template('login.html', title='Login',form=form)



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))





@app.route("/profile")
def profile():
    return render_template('profile.html', title='Profile')





@app.route("/photos")
def photos():
    return render_template('photos.html', title='Photos')






@app.route("/members")
def members():
    return render_template('members.html', title='Members')






@app.route("/groups")
def groups():
    return render_template('groups.html', title='Groups')





@app.route("/contact")
def contact():
    return render_template('groups.html', title='Contact')