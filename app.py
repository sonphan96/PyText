from twilio.rest import Client

account_sid = "AC549262ec2d885cbb4e67fcad18fc58d9"
auth_token = "2e4bfaa837e893de2acb81e7e9ec5b89"

client = Client(account_sid, auth_token)

call = client.messages.create(
    to="..",
    from_="",
    body="This is our first message"
)
