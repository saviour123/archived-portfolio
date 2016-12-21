
from flask import Flask, render_template, flash, url_for, abort
import markdown
import os
from werkzeug import cached_property
from flask_flatpages import FlatPages
import yaml
from myclass import Blog, Post


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
#app.config.from_object(__name__)
app = Flask(__name__)
app.secret_key = 'saviour123'
POSTS_FILE_EXTENSION = '.md'
blog = Blog(app, root_dir='posts')


#the data formating function
@app.template_filter('date')
def format_date(value, format='%B %d, %Y'):
	return value.strftime(format)

#home route for listing
@app.route('/')
def index():
	posts = [Post('hello.md', root_dir='posts')]
	return render_template('index.html', posts=posts)

#blog rendering
@app.route('/blog/<path:path>/')
def post(path):
	path = os.path.join('posts', path)
	post = Post(path + POSTS_FILE_EXTENSION)
	return render_template('post.html', post=post)

if __name__=='__main__':
	app.run()