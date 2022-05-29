from twilio.rest import Client
import credentials

client = Client(credentials.SID,credentials.token)

for msg in client.messages.list():
    print(msg.body)