from flask import Flask, render_template, request
import google.generativeai as genai
import os


API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyB_63vrEJQOwrYWqFCMCSn-AF3rXw2cMuM")

app = Flask(__name__)

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        if prompt:
            try:
                response = model.generate_content(prompt)
                output = response.text
            except Exception as e:
                output = f"Erreur: {str(e)}"
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
