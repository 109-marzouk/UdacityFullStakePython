# -*- coding: utf-8 -*-
# By Mohamed Marzouk
# facebook.com/MohamedMarzouk23
from twilio.rest import Client
account_sid = "my account_sid"
auth_token = "my auth_token"
client = Client(account_sid, auth_token)
client.api.account.messages.create(
    to="mobile Phone number To send",
    from_="my mobile Phone number",
    body="Hello World!")