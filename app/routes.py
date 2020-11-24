#####################################################################
#
#  This file is for defining the routing of the website and what urls do
#
#####################################################################

from app import app, db
from flask import render_template, redirect, url_for, flash, request, Response
from app.models import Comment, Img
from app.forms import CommentForm, DeleteCommentForm, UploadFileForm
from werkzeug.utils import secure_filename
from config import DefaultConfig
import os


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


@app.route('/image/<db_image_id>')
def imageRoute(db_image_id):
    image_data = Img.query.filter_by(id=db_image_id).first_or_404()
    print(image_data.mimetype)
    return Response(image_data.img, mimetype=image_data.mimetype)
