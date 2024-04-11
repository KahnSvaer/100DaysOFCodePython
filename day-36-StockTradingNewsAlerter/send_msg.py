from twilio.rest import Client
import os
import time

ACCOUNT_SID = os.environ.get("T_AUTH_ID")
auth_token = os.environ.get("T_KEY")
client = Client(ACCOUNT_SID, auth_token)

PHONE_NUMER = os.environ.get("T_PHONE")
PSNL_PHONE_NUMBER = os.environ.get("PSNL_PHONE")


def send_message(list_dict: list, symbol: str, percentage: float, is_up_arrow):
    arrow = "🔺" if is_up_arrow else "🔻"

    for iter_dict in list_dict:
        message_body = (f"\n{symbol}: {arrow}{abs(percentage):.2f}%\n"
                        f"Headline: {iter_dict.get('title')}")
        message = client.messages.create(
            body=message_body,
            from_=PHONE_NUMER,
            to=PSNL_PHONE_NUMBER
        )
        print(message.status)
        time.sleep(5)