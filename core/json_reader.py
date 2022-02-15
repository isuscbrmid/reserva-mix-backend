import json
import os

__BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def json_settings():
    with open("{0}/{1}".format(__BASE_DIR, "core/settings.json")) as data_file:
        data = json.load(data_file)
    return data
