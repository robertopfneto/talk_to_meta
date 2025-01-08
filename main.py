import openai
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

import tokens


#Substitute the Tokens and Keys Variables with your tokens and put between the quotes
openai.api_key = "" #Put your OpenAI API Key here
twilio_sid = "" #Put your Twilio SID here
twilio_auth_token = "" #Put your Twilio Auth Token here
twilio_phone_number = "" #Put your Twilio Phone Number here

client = Client(twilio_sid, twilio_auth_token)

app = Flask(__name__)


def chat_com_gpt(prompt):
    response = openai.chat.Completion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()

@app.route("/webhook", methods=["POST"])
def iniciar_conversa():

    message = request.values.get("Body", "").strip()
    #sender = request.values.get("From", "")
    response = MessagingResponse()
    msg = response.message()

    if message.lower() == "comece":
        msg.body("Olá @Meta AI, tudo bem?")
        resposta_gpt = chat_com_gpt("Inicie uma conversa com outro bot chamado @Meta AI, obrigatoriamente antes de toda mensagem voce deve escrever @Meta AI antes da mensagem")
        msg.body(resposta_gpt)

    else:
        resposta_gpt = chat_com_gpt(message)
        msg.body(resposta_gpt)

    return str(response)


if __name__ == "__main__":
    app.run(debug=True)