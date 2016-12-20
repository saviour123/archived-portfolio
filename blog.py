
from flask import Flask, render_template, flash
import markdown
import os
from werkzeug import cached_property
from flask_flatpages import FlatPages
import yaml


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
#app.config.from_object(__name__)

app = Flask(__name__)
app.secret_key = 'saviour123'
#pages = FlatPages(app)
POSTS_FILE_EXTENSION = '.md'

#markdown rendering class
class Post(object):
	def __init__(self, path, root_dir=''):
		self.urlpath = os.path.splitext(path.strip('/'))[0]
		self.filepath = os.path.join(root_dir, path.strip('/'))
		self._initialize_metadata()

	#handles the markdown conversion
	@cached_property
	def html(self):
		with open(self.filepath, 'r') as fin:
			content = fin.read().split('\n', 1)[1].strip()
		return markdown.markdown(content)

	@property
	def url(self):
		return url_for('post', path=self.urlpath)
	
	def _initialize_metadata(self):
			content = ''
			with open(self.path, 'r') as fin:
				for line in fin:
					if not line.strip():
						break
					content += line
			self.__dict__.update(yaml.load(content))

@app.template_filter('date')
def format_date(value, format='%B %d, %Y'):
	return value.strftime(format)

#app.jinja_env.filters['date'] = format_date

# @app.context_processor
# def inject_format_date():
# 	return {'format_date': format_date}

@app.route('/')
def index():
	#dir_path = os.path.dirname(os.path.realpath(__file__))
	#print dir_path
	posts = [Post('hello.md', root_dir='posts')]
	return render_template('index.html', posts=posts)

@app.route('/blog/<path:path>/')
def post(path):
	path = os.path.join('posts', path + POSTS_FILE_EXTENSION)
	post = Post(path + POSTS_FILE_EXTENSION, root_dir='posts')
	return render_template('post.html', post=post)

if __name__=='__main__':
	app.run(debug=True)