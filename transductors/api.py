import requests


def create_transductor(transductor, subordinate_server):
    protocol = "http://"
    endpoint = "/energy-transductors/"
    address = protocol\
        + subordinate_server.ip_address\
        + ":"\
        + subordinate_server.port\
        + endpoint

    return requests.post(address, json=__get_transductor_data(transductor,
                                                              subordinate_server))


def update_transductor(transductor, subordinate_server):
    protocol = "http://"
    endpoint = "/energy-transductors/"
    address = protocol\
        + subordinate_server.ip_address\
        + ":"\
        + subordinate_server.port\
        + endpoint\
        + transductor.serial_number\
        + "/"

    return requests.put(address, json=__get_transductor_data(transductor,
                                                             subordinate_server))


def delete_transductor(transductor, subordinate_server):
    protocol = "http://"
    endpoint = "/energy-transductors/"
    address = protocol\
        + subordinate_server.ip_address\
        + ":"\
        + subordinate_server.port\
        + endpoint\
        + transductor.serial_number\
        + "/"

    return requests.delete(address)


def __get_transductor_data(transductor, subordinate_server):
    latitude = (
        transductor.geolocation_latitude
        if transductor.geolocation_latitude is not None else 0.0
    )
    longitude = (
        transductor.geolocation_longitude
        if transductor.geolocation_longitude is not None else 0.0
    )

    return {
        "model": transductor.model,
        "serial_number": transductor.serial_number,
        "ip_address": transductor.ip_address,
        "geolocation_latitude": latitude,
        "geolocation_longitude": longitude,
        "measurement_minutelymeasurement": [],
        "measurement_quarterlymeasurement": [],
        "measurement_monthlymeasurement": [],
        "firmware_version": transductor.firmware_version
    }
