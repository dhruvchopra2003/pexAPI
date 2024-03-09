# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# try:
#     openai.api_key = os.getenv("OPENAI_API_KEY")
# except:
#     pass

# initial_prompt = "You are a real estate investment expert specializing in commercial real estate in delhi ncr region. Start by taking the name and phone number of the user. Assist users in understanding the right investment for them and assisting them with the best option for that nature of investment. Finalizing upto 3 projects and schedule a visit. only access primary market commercial projects."

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_input = request.json.get("user_input", "")

#     if user_input.strip() != "":
#         messages = [{"role": "system", "content": initial_prompt}]
#         messages.append({"role": "user", "content": user_input})

#         response = openai.ChatCompletion.create(
#             model="gpt-4-vision-preview",
#             messages=messages,
#             max_tokens=600,
#             temperature=1,
#         )

#         bot_reply = response.choices[0].message.content.strip()
#         return jsonify({"bot_reply": bot_reply})
#     else:
#         return jsonify({"error": "Empty user input"}), 400


# if __name__ == "__main__":
#     app.run()

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# try:
#     openai.api_key = os.getenv("OPENAI_API_KEY")
# except Exception as e:
#     print("Error setting OpenAI API key:", e)

# initial_prompt = "You are a real estate investment expert specializing in commercial real estate in Delhi NCR region. Start by taking the name and phone number of the user. Assist users in understanding the right investment for them and assisting them with the best option for that nature of investment. Finalizing up to 3 projects and schedule a visit. Only access primary market commercial projects."

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes


# @app.route("/chat", methods=["POST"])
# def chat():
#     try:
#         messages = [request.json]
#         if not messages:
#             messages = [{"role": "system", "content": initial_prompt}]
#         else:
#             messages.insert(0, {"role": "system", "content": initial_prompt})

#         response = openai.ChatCompletion.create(
#             model="text-davinci-003",
#             messages=messages,
#             max_tokens=150,
#             temperature=0.7,
#         )

#         bot_reply = response.choices[0].message["content"].strip()
#         return jsonify({"bot_reply": bot_reply})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()

try:
    openai.api_key = os.getenv("OPENAI_API_KEY")
except Exception as e:
    print("Error setting OpenAI API key:", e)

initial_prompt = "You are a real estate investment expert specializing in commercial real estate in Delhi NCR region. Start by taking the name and phone number of the user. Assist users in understanding the right investment for them and assisting them with the best option for that nature of investment. Finalizing up to 3 projects and schedule a visit. Only access primary market commercial projects."

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/chat", methods=["POST"])
def chat():
    try:
        chat_history = request.json["chat_history"]
        messages = [chat for chat in chat_history]
        print(chat_history)
        print(messages)

        response = openai.ChatCompletion.create(
            model="gpt-4-vision-preview",
            messages=messages,
            max_tokens=600,
            temperature=1,
        )

        bot_reply = response.choices[0].message["content"].strip()
        return jsonify({"bot_reply": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
