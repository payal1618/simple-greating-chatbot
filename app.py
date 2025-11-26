from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.form['msg'].lower()

    # Time-based greeting function
    def smart_greeting():
        current_time = datetime.now()
        hour = current_time.hour
        
        if hour < 12:
            greeting = "Good Morning! 🌅"
        elif hour < 18:
            greeting = "Good Afternoon! ☀️"
        else:
            greeting = "Good Evening! 🌙"
        
        return greeting

    # FIRST TIME “HI / HELLO” MESSAGE → TIME GREETING
    if "hi" in user_msg or "hello" in user_msg or "hii" in user_msg:
        return smart_greeting() + " How can I help you? 😊"

    # Other conversation replies
    elif "how are you" in user_msg:
        return "I’m doing great! 😊 What about you?"
    elif "bye" in user_msg:
        return "Goodbye! 👋 Take care!"
    elif "thanks" in user_msg or "thank you" in user_msg:
        return "You're welcome! 😊"

    # Default answer → greeting again
    return smart_greeting() + " How can I assist you?"
    

if __name__ == "__main__":
    app.run()
