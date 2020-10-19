import json
import os

from ckan.common import config
from ckan.plugins.toolkit import abort, get_action


def load_secure_vocabularies_config():
    """
    Load some config info from a json file
    """
    try:
        # @TODO: Get the filepath from the CKAN .ini file
        # path = config.get('ckan.workflow.json_config', '/usr/lib/ckan/default/src/ckanext-workflow/ckanext/workflow/example.settings.json')
        with open('/app/src/ckanext-vocabulary-services/ckanext/vocabulary_services/secure/secure_vocabularies.json') as json_data:
            d = json.load(json_data)
            return d
    except Exception as e:
        abort(403, "Secure vocabularies configuration file not found.")


def load_secure_vocabulary_config(vocabulary_name):
    secure_vocabulary_config = [
        x for x in load_secure_vocabularies_config() if x.get('name', None) == vocabulary_name
    ]

    return secure_vocabulary_config[0] if secure_vocabulary_config[0] else {}


def get_secure_filepath(filename):
    return os.path.join(
        config.get('ckan.storage_path'),
        # Because we are using the standard CKAN uploader class - "storage/uploads" is the path
        'storage',
        'uploads',
        config.get('ckan.vocabulary_services.secure_dir', 'secure_csv'),
        filename
    )


def get_secure_vocabulary_record(vocabulary_name, query):
    return get_action('get_secure_vocabulary_record')({}, {'vocabulary_name': vocabulary_name, 'query': query})