from flask import Flask, request, jsonify, session
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()

try:
    openai.api_key = os.getenv("OPENAI_API_KEY")
except:
    pass

initial_prompt = "You are a real estate investment expert specializing in both commercial and resident real estate in Delhi NCR region. Start by taking the name and phone number of the user. Assist users in understanding the right investment for them and assisting them with the best option for that nature of investment (For residential preferences, also consider number of family members). Finalizing upto 3 projects and schedule a visit. Only access primary market projects. Don't ask all questions in one go."

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Set your secret key for session management
CORS(app)  # Enable CORS for all routes

# Initialize an empty dictionary to store chat histories for each user's session
session_chat_histories = {}


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("user_input", "")

    if user_input.strip() != "":
        if "chat_history" not in session:
            # If chat history is not in session, initialize it with the initial prompt
            session["chat_history"] = [{"role": "system", "content": initial_prompt}]
            session_chat_histories[session["sid"]] = session["chat_history"]

        chat_history = session["chat_history"]

        # Append user input to chat history stored in session
        chat_history.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-4-vision-preview",
            messages=chat_history,
            max_tokens=600,
            temperature=1,
        )

        bot_reply = response.choices[0].message.content.strip()
        # Append bot's reply to chat history stored in session
        chat_history.append({"role": "assistant", "content": bot_reply})

        return jsonify({"bot_reply": bot_reply})
    else:
        return jsonify({"error": "Empty user input"}), 400


if __name__ == "__main__":
    app.run()
