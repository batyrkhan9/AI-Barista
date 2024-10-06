from openai import OpenAI
import os
from dotenv import load_dotenv

#load environment variables from the .env file
load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

#API call 
def get_response(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a barista chatbot."},
        {"role": "user", "content": prompt},
    ])
    return response.choices[0].message.content

#function to generate barista chatbot responses
def generate_barista_response(customer_input):
    prompt = f"As a barista chatbot, respond to this: {customer_input}"
    response = get_response(prompt)
    return response

#example usage of the chatbot
if __name__ == "__main__":
    customer_query = "What coffee do you recommend today?"
    response = generate_barista_response(customer_query)
    print(response)