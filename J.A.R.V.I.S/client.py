# from openai import OpenAI
# # client = OpenAI()

# client=OpenAI(
#     api_key="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"
# )
# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a Virtual assistant named jarvis skilled in genral task like Alexa and Google Cloud"},
#         {
#             "role": "user",
#             "content": "What is coding"
#         }
#     ]
# )

# print(completion.choices[0].message)

# ------------------------------------------------------------------------------------------------------------------------


# import openai
# import os

# # Store your API key securely in an environment variable
# os.environ["OPENAI_API_KEY"] = "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"  # Replace with your new API key

# # Initialize OpenAI client securely
# client = openai.OpenAI()

# # Make a request
# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a Virtual Assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant."},
#         {"role": "user", "content": "What is coding?"}
#     ]
# )

# # Print the assistant's response
# print(completion.choices[0].message.content)
# -------------------------------------------------------------------------------------------------------------------
# from google import genai
# from google.genai import types
# api="AIzaSyALq0PF4TB6hDWIZOTc9TFptic4XVEGhFk"

import google.generativeai as genai
import os

# Store API key securely using environment variables
os.environ["GOOGLE_API_KEY"] = "AIzaSyALq0PF4TB6hDWIZOTc9TFptic4XVEGhFk"

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def aiProcess(command):
    """Send a command to the Gemini AI model and return the response."""
    model = genai.GenerativeModel("gemini-pro")  # Choose the appropriate model
    response = model.generate_content(command)
    return response.text

# Example usage
user_command = "What is the capital of France?"
print(aiProcess(user_command))

