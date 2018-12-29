import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from datetime import datetime

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'


app = Flask(__name__, static_folder='static_dir')
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)


@app.route("/")
def index():
    latest = get_pages(pages)
    return render_template('index.html', pages=latest)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/projects")
def projects():
    return render_template('projects.html')


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@app.route("/tag/<string:tag>/")
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)


# helpers
def get_pages(articles, offset=None, limit=None, section=None, year=None):
    """ Retrieves pages matching passec criterias.
    """
    # filter unpublished article
    if not app.debug:
        # articles = (p for p in pages if 'date' in p.meta) validadate the presence of date
        articles = (p for p in articles if p.meta.get('published') is True)
        return sorted(articles, reverse=True, key=lambda p: str(p.meta['date']))
    else:
        return sorted(articles, reverse=True, key=lambda p: str(p.meta['date']))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=4000)
