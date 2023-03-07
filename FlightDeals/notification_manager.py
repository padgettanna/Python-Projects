from twilio.rest import Client

ACCOUNT_SID = "Your account SID"
AUTH_TOKEN = "Your auth token"
TWILO_VIRT_NUMBER = "Your Twilo number"
TWILO_VERIFIED_NUMBER = "Verified number"


class NotificationManager:

    def send_message(self, text):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=text,
            from_=TWILO_VIRT_NUMBER,
            to=TWILO_VERIFIED_NUMBER
        )
        print(message.status)
