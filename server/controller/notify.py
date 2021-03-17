from pyfcm import FCMNotification

from server.config import APIKEY, TOKEN

push_service = FCMNotification(APIKEY)


def sendMessage(body, title):

    message = {
        "body": body,
        "title": title
    }

    result = push_service.notify_multiple_devices(registration_ids=TOKEN, data_message=message)

    print(result)
