from django.conf import settings


def get_db_config():
    _host = None
    _port = None
    _database = None

    if settings.TESTING_MODE:
        _host = settings.USERS_DB.TEST.HOST
        _port = settings.USERS_DB.TEST.PORT
        _database = settings.USERS_DB.TEST.DATABASE
    else:
        _host = settings.USERS_DB.DEV.HOST
        _port = settings.USERS_DB.DEV.PORT
        _database = settings.USERS_DB.DEV.DATABASE

    class config:
        host = _host
        port = _port
        database = _database

    return config
