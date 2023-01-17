#  Python_23.2.12_Jinja_Exercise
# """Madlibs game, this file is the baseline python file to run all the routes through"""
#
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from templates.stories import story
#
# Change below after settled in
# from stories import X, y, z

app = Flask(__name__)

app.config['SECRET_KEY'] = "madlib314"
debug = DebugToolbarExtension(app)


@app.route("/madlibs/story")
def main_page():
    """set-up main page"""
    text = story.generate(story, request.args)
    return render_template('madlib.html', text=text)


@app.route('/madlibs/test')
def story_test():
    # place1 = request.args["placea"]
    # noun1 = request.args["noun"]
    # verb1 = request.args["verb"]
    # adjective1 = request.args["adjective"]
    # plural_noun= request.args["plural_noun"]

    prompts = story.prompts
    # return storytime
    # answers={}
    # for idx, val in enumerate(storytime):
    # answers[val] = storytime[idx]

    # testing = story.generate(story, {"place": "winamac", "noun": "cat", "verb": "running", "adjective": "soft", "plural_noun": "strawberries"})
    # testing = story.generate(story, answers)
    return render_template('form1.html', prompts=prompts)
    # , place=place1, verb=verb1, testing=testing)


# @app.route('/madlibs/story2')
# def story_test2():
    # testing2 = story2.generate(story2, {"place": "winamac", "noun": "cat",
    #    "verb": "running", "adjective": "soft", "plural_noun": "strawberries"})
    # return render_template('madlib.html', testing=testing2)


# @app.route('/madlibs/form1')
# def entry():
    # return render_template('form1.html')
#

# from flask import Flask, request, render_template
# from random import randint,  choice, sample
# from flask_debugtoolbar import DebugToolbarExtension
#
# app = Flask(__name__)
#
# app.config['SECRET_KEY'] = "chickenzarecool21837"
# debug = DebugToolbarExtension(app)
#
#
# @app.route('/')
# def home_page():
    # """Shows home page"""
    # return render_template('base.html')
