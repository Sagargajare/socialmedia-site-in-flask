from flask import Flask , render_template,url_for ,flash ,redirect
from forms import RegistrationForm , LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '124fv22f58f5f6f9ff4dwda6d'



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registration',form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'sagar@gmail.com' and form.password.data =='password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please Check username and Password ','danger')
    return render_template('login.html', title='Login',form=form)



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








if __name__ == "__main__":
    app.run(debug=True)