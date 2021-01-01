# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
#account_sid = os.environ['ACe874e32931b4d9e0d1e2656d2144328b']
account_sid = 'ACe874e32931b4d9e0d1e2656d2144328b'
#auth_token = os.environ['aca349608dd61fb46609b5031fd68398']
auth_token = 'aca349608dd61fb46609b5031fd68398'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+17655302551',
                     to='+14082189586'
                 )

print(message.sid)