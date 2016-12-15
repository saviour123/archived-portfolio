
from flask import Flask, render_template, flash
import markdown
import os
from werkzeug import cached_property
from flask_flatpages import FlatPages


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
#app.config.from_object(__name__)


app = Flask(__name__)
app.secret_key = 'saviour123'
#pages = FlatPages(app)
POSTS_FILE_EXTENSION = '.md'

class Post(object):
	def __init__(self, path):
		self.path = path

	@cached_property
	def html(self):
		with open(self.path, 'r') as fin:
			content = fin.read().strip()
		return markdown.markdown(content)  
		




@app.route('/')
def index():
	dir_path = os.path.dirname(os.path.realpath(__file__))
	#print dir_path
	return 'hello world'

@app.route('/blog/<path:path>/')
def post(path):	
	import ipdb; ipdb.set_trace()
	path = os.path.join('posts', path + POSTS_FILE_EXTENSION)
	print path
	post = Post(path)
	return render_template('post.html', post=post)

if __name__=='__main__':
	app.run(debug=True)