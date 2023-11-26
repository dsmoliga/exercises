from twilio.rest import Client

TWILIO_SID = "ACc9f3cd54b3e55b82b819f7ab20231088"
TWILIO_AUTH_TOKEN = "80ab4b890768450a8998d794166e09cd"
TWILIO_VIRTUAL_NUMBER = "+12674606849"
TWILIO_VERIFIED_NUMBER = "#"


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)
