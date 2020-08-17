#####################################################################
#
#  This file is for defining the routing of the website and what urls do
#
#####################################################################

from app import app
from flask import render_template
from app.models import test_posts, Post
from app.forms import PostForm


@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = PostForm()
    home_feed = test_posts
    if form.validate_on_submit():
        new_post = Post(form.name.data, form.text.data)
        home_feed.insert(0, new_post)
    return render_template('home.html', home_feed=home_feed, form=form)


@app.route('/scratch', methods=['GET'])
def scratch_page():
    # get template
    # render the template
    # return rendered template
    return render_template('scratch.html')
