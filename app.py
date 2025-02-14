from flask import *

app = Flask("my-api")

@app.route("/")
def home():
    return render_template('index.html')

app.run(host="0.0.0.0", port=5000, debug=True)
