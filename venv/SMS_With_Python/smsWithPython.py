# +17652955060

from twilio.rest import Client

account_sid = 'ACc4c3d35f07f59cd05f8567c6525ac552'
auth_token = '78654e92a9e1d7beaf38d40f0b0054b0'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGea4847f307acbebb181cb81711c05785',
    body='KYA baat kch to sikh rhe tum',
    to='+918923108116'
)

print(message.sid)