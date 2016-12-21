from flask import Flask, render_template, flash, url_for
import markdown
import os
from werkzeug import cached_property
from flask_flatpages import FlatPages
import yaml
from blog import *

class Blog(object):
	"""docstring for Blog"""
	def __init__(self, app, root_dir, file_ext=POSTS_FILE_EXTENSION):
		self._app = app
		self.root_dir = root_dir
		self.file_ext = file_ext
		self._cache = {}
		self._initialize_cache()

		@property
		def posts(self):
			return self._cache.values()

		def get_post_or_404(self, path):
			"""Return a path or return 404"""
			try:
				return self._cache[path]
			except KeyError:
				abort(404)

		def _initialize_cache():
			"""loop through root_dir and creats a cache of posts"""
			for (root, dirpaths, filepaths) in os.walk(self.root_dir):
				for filepath in filepaths:
					filename, ext = os.path.splitext(filepath)
					if ext == self.file_ext:
						path = os.path.join(root, filepath).replace(self.root_dir, '')
						post = Post(path, root_dir=self.root_dir)
						self.cache[post.urlpath] = post


		


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
			content = fin.read().split('\r\n\r\n', 1)[1].strip() #for linux \n\n
			print content
		return markdown.markdown(content)

	#handling of urls for clicking	
	@property
	def url(self):
		print self.urlpath
		return url_for('post', path=self.urlpath)
	
	#handle the metadata aspect
	def _initialize_metadata(self):
			content = ''
			with open(self.filepath, 'r') as fin:
				for line in fin:
					if not line.strip():
						break
					content += line
			self.__dict__.update(yaml.load(content))