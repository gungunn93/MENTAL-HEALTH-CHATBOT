from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
from chatbot import get_response
from safety import is_crisis, CRISIS_RESPONSE
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

@app.route("/")
def home():
    session["history"] = []   # reset on fresh load
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    
    if not user_message:
        return jsonify({"reply": "Please type something. I'm here to listen. 💙"})
    
    # Safety check first
    if is_crisis(user_message):
        return jsonify({"reply": CRISIS_RESPONSE, "crisis": True})
    
    # Load history from session
    history = session.get("history", [])
    
    # Get AI response
    reply = get_response(user_message, history)
    
    # Update history
    history.append({"role": "user", "content": user_message})
    history.append({"role": "assistant", "content": reply})
    session["history"] = history
    
    return jsonify({"reply": reply, "crisis": False})

@app.route("/reset", methods=["POST"])
def reset():
    session["history"] = []
    return jsonify({"status": "reset"})

if __name__ == "__main__":
    app.run(debug=True)