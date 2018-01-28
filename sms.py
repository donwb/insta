from twilio.rest import Client

def send(sid, token, from_number, to_number, message):
    
    account_sid = sid
    auth_token  = token

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=to_number, 
        from_=from_number,
        body=message)

    print("Message sent {}!".format(message.sid))

def send_multiple(sid, token, from_number, to_numbers, message):
    for num in to_numbers:
        send(sid, token, from_number, num, message)
        