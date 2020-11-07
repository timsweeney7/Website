#####################################################################
#
#  This file is for defining the routing of the website and what urls do
#
#####################################################################

from app import app, db
from flask import render_template, redirect, url_for, flash
from app.models import Comment
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

    if upload_file_form.validate_on_submit():
        f = upload_file_form.file.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(DefaultConfig.UPLOAD_FOLDER, filename))
        return redirect(url_for('home_page'))

    if comment_form.validate_on_submit():
        new_post = Comment(author=comment_form.name.data, text=comment_form.text.data)
        db.session.add(new_post)
        db.session.commit()
        flash('here')
        return redirect(url_for('scratch_page'))


    return render_template('home.html', home_feed=posts, form=comment_form, delete_form=delete_comment_form,
                           upload_file_form=upload_file_form)


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
