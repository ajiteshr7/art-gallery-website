from art_web import app
from flask import render_template, request, flash, redirect, url_for, session
from models import db, User, Feedback, Paintings, Artist, AdminUser
from forms import SignupForm, SigninForm , FeedbackForm, SubmitArt
from flask_admin import Admin
from flask_admin.base import MenuLink
from flask_admin.contrib.sqla import ModelView
# from flask_basicauth import BasicAuth


class MyModelView(ModelView):
    column_display_pk = True
    column_hide_backrefs = True


# Admin views
admin = Admin(app, name='Art Gallery', template_mode='bootstrap3')
# admin = Admin(app, name='art_gallery', base_template='base.html')
admin.add_view(MyModelView(AdminUser, db.session))
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Feedback, db.session))
admin.add_view(MyModelView(Paintings, db.session))
admin.add_view(MyModelView(Artist, db.session))
# Add home link by url
admin.add_link(MenuLink(name='Back', url='/'))


@app.route('/testdb')
def testdb():
    user = Paintings.query.with_entities(Paintings.name, Paintings.painting_photo).filter_by(artist_id=1)
    print dict(user.all())
    for u in user.all():
        print u
    # return render_template("login.html",title="login")
    return "done!"

@app.route('/', methods=['GET', 'POST'])
def index():
    title = 'Home'
    form = FeedbackForm()
    pnt = Paintings.query.with_entities(Paintings.name, Paintings.painting_photo).filter_by(artist_id=1)
    scp = Paintings.query.with_entities(Paintings.name, Paintings.painting_photo).filter_by(artist_id=2)
    paintings = dict(pnt.all())
    sculptures = dict(scp.all())
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('index.html',title = title, paintings = paintings, sculptures = sculptures, form = form)
        else:
             feedback = Feedback(form.name.data, form.email.data, form.subject.data, form.comment.data)
             db.session.add(feedback)
             db.session.commit()
             flash("Form submitted successfully!", "success")
             return redirect(url_for('index'))
    return render_template('index.html',title = title, paintings = paintings, sculptures = sculptures, form = form)

@app.route('/profile')
def profile():
    title = 'Profile'
    if 'email' not in session:
        return redirect(url_for('signin'))

    # Admin user
    if session['email'] == 'admin':
        return render_template('profile.html',title=title)

    # Normal user
    user = User.query.filter_by(email = session['email']).first()
    if user is None:
        return redirect(url_for('signin'))
    else:
        return render_template('profile.html',title=title)

@app.route('/signout')
def signout():
    if 'email' not in session:
        return redirect(url_for('signin'))

    session.pop('email', None)
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    title = 'Sign Up'
    form = SignupForm()
    # If user is signed in
    if 'email' in session:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html',title = title, form=form)
        else:
             newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
             db.session.add(newuser)
             db.session.commit()
             session['email'] = newuser.email
             return redirect(url_for('profile'))

    elif request.method == 'GET':
        return render_template('signup.html',title = title, form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    title = 'Login'
    form = SigninForm()
    # If user is signed in
    if 'email' in session:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        auser = AdminUser.query.filter_by(email = form.email.data.lower()).first()

        # Admin login
        if auser and auser.check_password(form.password.data):
            session['email'] = 'admin'
            return redirect('/admin')

        elif form.validate() == False:
            return render_template('signin.html',title = title, form=form)

        else:
            # return "hello!"
            session['email'] = form.email.data
            return redirect(url_for('profile'))

    elif request.method == 'GET':
        return render_template('signin.html',title = title, form=form)


@app.route('/art', methods=['GET','POST'])
def art():
    title = "Submit art"
    form = SubmitArt()
    if 'email' not in session:
        flash("Signin first!","error")
        return redirect(url_for(signin))
    elif request.method == 'POST':
        if form.validate() == False:
            flash("Enter correct values!","error")
            return render_template('submit_art.html',title = title, form=form)
        else:
             newart = Paintings(form.name.data, form.location.data, form.artist_id.data)
             db.session.add(newart)
             db.session.commit()
             flash("Form submitted successfully!", "success")
             return redirect(url_for('art'))

    return render_template("submit_art.html",title=title, form=form)
