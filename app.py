from os import path, walk

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route("/index")
@app.route("/boo")
def index():
    return render_template("base.html")


if __name__ == '__main__':

    extra_dirs = ['templates','static' ]
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in walk(extra_dir):
            for filename in files:
                filename = path.join(dirname, filename)
                if path.isfile(filename):
                    extra_files.append(filename)
    app.run(debug=True, extra_files=extra_files)
