import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC7743e256a6fbb6b764362ed407330233']
auth_token = os.environ['327ab5811e22c9440d09761ae980347c']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+919927065553',
                     to='+919084801974'
                 )

print(message.sid)
# Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client
# # Set environment variables for your credentials
# # Read more at http://twil.io/secure
# account_sid = "AC7743e256a6fbb6b764362ed407330233"
# auth_token = os.environ["327ab5811e22c9440d09761ae980347c"]
# client = Client(account_sid, auth_token)
# message = client.messages \
#     .create(
#          messaging_service_sid='MG9752274e9e519418a7406176694466fa',
#          body='body',
#          to='+919084801974'
#      )
#
# print(message.sid)
# print("helo")