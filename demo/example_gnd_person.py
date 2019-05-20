from apimapper import APIMapper
from apimapper import config
import logging
from pprint import pprint


def main():
    GND_PERSON_SOURCE = {config.URL: 'https://lobid.org/gnd/search',
                         config.QUERY_FIELD: 'q',
                         config.PAYLOAD: {'format':'json:suggest',
                                         'filter': 'type:Person',
                                         'q': None}}

    GND_PERSON_MAP = {config.DIRECT: {'label': 'label',
                                      'uri': 'id'},
                      config.RULES: {'source': {config.RULE: '"GND"'},
                                     'label_name': {config.RULE: '"{p1}".split("|")[0].strip()',
                                                    config.FIELDS: {'p1': 'label'}},
                                     'label_year': {config.RULE: '"{p1}".split("|")[1].strip() if "{p1}".split("|")[1].strip()[0].isnumeric() else ""',
                                                    config.FIELDS: {'p1': 'label'}},
                                     'label_profession': {config.RULE: '"{p1}".split("|")[2].strip() if "{p1}".split("|")[1].strip()[0].isnumeric() else "{p1}".split("|")[1].strip()',
                                                          config.FIELDS: {'p1': 'label'}}}}
    
    api = APIMapper(GND_PERSON_SOURCE, GND_PERSON_MAP)
    res = api.fetch_results('Doctor Who')
    pprint(res)
    
    return


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    main()
