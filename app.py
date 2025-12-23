from flask import Flask, request, jsonify, render_template
from translator import translate_text

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    text = data.get("text", "")
    language = data.get("language", "")

    translated = translate_text(text, language)
    return jsonify({"translated_text": translated})

if __name__ == "__main__":
    app.run(debug=True)
