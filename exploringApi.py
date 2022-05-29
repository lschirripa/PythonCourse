from twilio.rest import Client
import credentials

client = Client(credentials.SID,credentials.token)

for msg in client.messages.list():
    print(f"Deleting {msg.body}")
    msg.delete()

# msg = client.messages.create(
#     from_= credentials.hidden_from,
#     to = credentials.hidden_to,
#     body= 'Hi there, sent from python!'
# )

#print(f"Created a new message: {msg.sid}")
