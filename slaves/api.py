import requests
from datetime import datetime, timedelta


def request_measurements(measurement_type, subordinate, transductor=None, 
                         start_date=None, end_date=None):
    protocol = "http://"
    endpoint = "/" + measurement_type + "/"
    address = protocol\
        + subordinate.ip_address\
        + ":"\
        + subordinate.port\
        + endpoint

    params = {}
    if transductor is not None:
        params["serial_number"] = transductor.serial_number

    if start_date is not None:
        start_date = start_date.strftime("%Y-%m-%d %H:%M:%S")
        params["start_date"] = start_date        

    if end_date is not None:
        end_date = end_date.strftime("%Y-%m-%d %H:%M:%S")
        params["end_date"] = end_date        

    return requests.get(address, params=params)


def request_all_events(subordinate):
    """
    Gets all subordinate related events.
    Returns an array of tuples containing tuple(Classname, response) pairs
    """
    responses = [
        (
            "FailedConnectionTransductorEvent",
            request_measurements('failed-connection-events', subordinate)
        ),
        (
            "VoltageRelatedEvent",
            request_measurements('voltage-events', subordinate)
        )
    ]

    return responses
