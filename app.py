from flask import Flask , render_template,url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html', title='Registration')



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