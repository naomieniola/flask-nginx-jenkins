from flask import Flask, render_template, session
import google.generativeai as genai

app = Flask("flaskwithGemini")
app.secret_key = "abc"

genai.configure(api_key="YOUR_GEMINI_API_KEY")

prompt = """Write Recommendations to be followed by SRE when the production 
respond with 3 suggestions and order by priority and less than 100 lines.
Respond in html, ignore header and body tags"""

@app.route('/')
def Home():
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    session["text"] = response.text.strip("\n").strip("").lstrip("html")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
