import json as js
import jwt as JWT
from django.conf import LazySettings
import requests

settings = LazySettings()

def create_transductor_model(transductor_model, slave_server):
    protocol = "http://"
    endpoint = "/transductor_models/"
    address = protocol\
        + slave_server.ip_address\
        + ":"\
        + slave_server.port\
        + endpoint

    jwt = JWT.JWT()
    key = JWT.jwk.OctetJWK(
        key=settings.SECRET_KEY.encode('ascii'), kid=1
    )

    content = __get_data(transductor_model)
    print(repr(content))

    new_content = dict(
        {'msg': str(jwt.encode(content, key))}
    )

    print(repr(new_content))

    new_content = js.dumps(new_content)

    return requests.post(address, json=new_content)


def update_transductor_model(transductor_model, slave_server):
    protocol = "http://"
    endpoint = "/transductor_models/"
    address = protocol\
        + slave_server.ip_address\
        + ":"\
        + slave_server.port\
        + endpoint\
        + transductor_model.model_code\
        + "/"

    return requests.put(address, json=__get_data(transductor_model))


def delete_transductor_model(transductor_model, slave_server):
    protocol = "http://"
    endpoint = "/transductor_models/"
    address = protocol\
        + slave_server.ip_address\
        + ":"\
        + slave_server.port\
        + endpoint\
        + transductor_model.model_code\
        + "/"

    return requests.delete(address)


def __get_data(transductor_model):
    return {
        "name": transductor_model.name,
        "model_code": transductor_model.model_code,
        "serial_protocol": transductor_model.serial_protocol,
        "transport_protocol": (transductor_model.transport_protocol),
        "minutely_register_addresses":
            transductor_model.minutely_register_addresses,
        "quarterly_register_addresses":
            transductor_model.quarterly_register_addresses,
        "monthly_register_addresses":
            transductor_model.monthly_register_addresses
    }
