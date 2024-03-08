from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

try:
    openai.api_key = os.getenv("OPENAI_API_KEY")
except:
    pass

initial_prompt = "You are a real estate investment expert specializing in commercial real estate in delhi ncr region. Start by taking the name and phone number of the user. Assist users in understanding the right investment for them and assisting them with the best option for that nature of investment. Finalizing upto 3 projects and schedule a visit. only access primary market commercial projects."

app = Flask(__name__)

@app.route("/"):
def hello_world():
    return "Testing"
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("user_input", "")

    if user_input.strip() != "":
        messages = [{"role": "system", "content": initial_prompt}]
        messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-4-vision-preview",
            messages=messages,
            max_tokens=600,
            temperature=1,
        )

        bot_reply = response.choices[0].message.content.strip()
        return jsonify({"bot_reply": bot_reply})
    else:
        return jsonify({"error": "Empty user input"}), 400


if __name__ == "__main__":
    app.run()
