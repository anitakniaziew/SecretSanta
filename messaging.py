# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from secrets import account_sid, auth_token, sender

client = Client(account_sid, auth_token)


def send(phone, message):
    client.messages \
        .create(
            body=message,
            from_=sender,
            to=phone
        )
