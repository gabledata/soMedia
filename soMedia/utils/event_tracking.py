from datetime import datetime
import uuid
from accounts.models import UserProfile


def send_analytics_payload(payload):
    """
    A stub function to send analytics payload.

    This function currently just prints the payload for demonstration purposes.

    :param payload: The analytics data payload to be sent.
    """

    print("Sending analytics payload:", payload)
    send_event_to_kafka(payload)


def get_session_property(request, property_name) -> str | None:
    """
    Get a property from the session.

    :param request: The request object.
    :param property_name: The name of the property to get.
    :return: The property value.
    """

    return request.session.get(property_name)

def get_client(request) -> str:
    """
    Get the client type - Android, iOS, or web.

    :param request: The request object.
    :return: "android", "iOS", or "web".
    """

    user_agent: str = request.META['HTTP_USER_AGENT'].lower() or ''
    if 'android' in user_agent:
        return "android"
    elif 'iphone' in user_agent:
        return "iOS"
    else:
        return "web"



def send_event_to_kafka(event):
    pass

def get_device_id(user) -> uuid.UUID:
    """
    Get the device id for the user.

    :param user: The user object.
    :return: The device id.
    """

    return uuid.uuid4()