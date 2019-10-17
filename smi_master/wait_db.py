import importlib
import os
import time

import logging

SERVICES_STARTED = False

def start_services():
    global SERVICES_STARTED

    if SERVICES_STARTED:
        return

    start_postgres()

    SERVICES_STARTED = True


log = logging.getLogger()


def start_postgres():
    settings_path = os.environ['DJANGO_SETTINGS_MODULE']
    settings = importlib.import_module(settings_path)

    db = settings.DATABASES['default']
    dbname = db['NAME']
    user = db['USER']
    password = db['PASSWORD']
    host = db['HOST']

    for _ in range(100):
        if can_connect(dbname, user, password, host):
            log.info("======= POSTGRES IS UP, CONNECTING")
            return
        log.warning('======= POSTGRES IS UNAVAILABLE, WAITING 0.5 Seconds')
        time.sleep(0.5)

    log.critical('Maximum number of attempts connecting to postgres database')
    raise RuntimeError('could not connect to database')


def can_connect(dbname, user, password, host):
    import psycopg2

    try:
        psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )
    except psycopg2.OperationalError:
        return False
    return True
