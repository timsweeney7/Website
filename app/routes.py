#####################################################################
#
#  This file is for defining the routing of the website and what urls do
#
#####################################################################

from app import app, db
from flask import render_template, redirect, url_for, flash
from app.models import Post
from app.forms import PostForm, DeletePostForm
from wtforms import SubmitField


@app.route('/', methods=['GET', 'POST'])
def home_page():
    post_form = PostForm()
    delete_form = DeletePostForm()
    if post_form.validate_on_submit():
        new_post = Post(author=post_form.name.data, text=post_form.text.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home_page'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('home.html', home_feed=posts, form=post_form, delete_form=delete_form)


@app.route('/delete-post/<post_id>', methods=['GET'])
def delete_post(post_id):
    post_to_delete = Post.query.filter_by(id=post_id).first_or_404()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('home_page'))


@app.route('/scratch', methods=['GET'])
def scratch_page():
    # get template
    # render the template
    # return rendered template
    return render_template('scratch.html')
