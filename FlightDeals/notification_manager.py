from twilio.rest import Client

ACCOUNT_SID = "AC3d8cb9be7c43c9f4d68dc0269e59a8a1"
AUTH_TOKEN = "a4ddcf7dbf3f0da95900c38ea58ba637"
TWILO_VIRT_NUMBER = "+18886377899"
TWILO_VERIFIED_NUMBER = "+12523053832"


class NotificationManager:

    def send_message(self, text):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=text,
            from_=TWILO_VIRT_NUMBER,
            to=TWILO_VERIFIED_NUMBER
        )
        print(message.status)