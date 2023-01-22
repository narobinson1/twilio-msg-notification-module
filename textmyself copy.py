#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string

import os
from twilio.rest import Client

account_sid = # enter account_sid
auth_token = # enter auth_token

myTwilioNumber = # enter twilio number
myMobileNumber = # enter phone number

def textmyself(message):
	client = Client(account_sid, auth_token)
	client.messages.create(body=message, from_=myTwilioNumber, to=myMobileNumber
)