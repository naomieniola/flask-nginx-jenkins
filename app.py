from flask import *
import google.generativeai as genai

app = Flask ("gemini-api")

@app.route("/")
def Index():
    return render_template('index.html')
#passing data from route url to html page

    app.run(debug=True)
