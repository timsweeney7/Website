#####################################################################
#
#  This file is for defining the routing of the website and what urls do
#
#####################################################################

from app import app, db, login_manager
from flask import render_template, redirect, url_for, flash, request, Response
from flask_login import current_user, login_user, logout_user
from app.models import Comment, Img, User
from app.forms import CommentForm, DeleteCommentForm, UploadFileForm, LoginForm, LogoutForm
from werkzeug.utils import secure_filename
from config import DefaultConfig
import os


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def home_page():
    comment_form = CommentForm()
    delete_comment_form = DeleteCommentForm()
    upload_file_form = UploadFileForm()

    posts = Comment.query.order_by(Comment.timestamp.desc()).all()
    images = Img.query.order_by(Img.timestamp.desc()).all()

    if comment_form.validate_on_submit():
        new_post = Comment(author=comment_form.name.data, text=comment_form.text.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home_page'))

    return render_template('home.html', home_feed=posts, form=comment_form, delete_form=delete_comment_form,
                           upload_file_form=upload_file_form, images=images)


#TODO: Fix delete comment form so that it uses post and not get. This will make it secure.
@app.route('/delete-comment/<comment_id>', methods=['GET'])
def delete_comment(comment_id):
    comment_to_delete = Comment.query.filter_by(id=comment_id).first_or_404()
    db.session.delete(comment_to_delete)
    db.session.commit()
    return redirect(url_for('home_page'))


@app.route('/scratch', methods=['GET'])
def scratch_page():
    # get template
    # render the template
    # return rendered template
    return render_template('scratch.html')


@app.route('/upload', methods=['POST'])
def upload():
    pic = request.files['pic']

    if not pic:
        flash('No pic uploaded')
        return redirect(url_for('home_page'))

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    image_file = open(os.path.join(DefaultConfig.UPLOAD_FOLDER, filename), 'wb')
    image_file.write(pic.read())
    image_file.close()
    img = Img(mimetype=mimetype, file_name=filename)
    db.session.add(img)
    db.session.commit()

    return redirect(url_for('home_page'))


@app.route('/delete-img', methods=['POST'])
def delete_img():
    img_id = request.form['img_id']
    img_to_delete = Img.query.filter_by(id=img_id).first_or_404()
    img_file_name = img_to_delete.file_name
    print(img_file_name)
    if os.path.exists(os.path.join(DefaultConfig.UPLOAD_FOLDER, img_file_name)):
        os.remove(os.path.join(DefaultConfig.UPLOAD_FOLDER, img_file_name))
    else:
        print("The file does not exist")
    db.session.delete(img_to_delete)
    db.session.commit()

    return redirect(url_for('home_page'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    login_form = LoginForm()
    logout_form = LogoutForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Incorrect')
            return redirect(url_for('login'))
        else:
            login_user(user)
            flash('Welcome back..')
            return redirect(url_for('home_page'))

    if logout_form.validate_on_submit():
        logout_user()
        return redirect(url_for('home_page'))

    return render_template('login.html', login_form=login_form, logout_form=logout_form)


