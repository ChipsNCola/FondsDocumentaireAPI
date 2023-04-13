from flask import Flask, render_template, request
import config
import aicontent
import openai
import os
def page_not_found(e):
    return render_template('404.html'), 404

app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/demander', methods=["GET", "POST"])
def coldEmails():

    if request.method == 'POST':

        submission = request.form['query']
        query = "Posez moi votre question: {}".format(submission)
        openAIAnswer = aicontent.ask(query)
        prompt = 'Réponse'.format(submission)

    return render_template('index.html', **locals())

if __name__ == "__main__":
    app.run()