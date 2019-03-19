from apimapper.apimapper import APIMapper
from apimapper.config.config import *
import logging
from pprint import pprint


def main():
    GND_PERSON_SOURCE = {URL: 'https://lobid.org/gnd/search',
                         QUERY_FIELD: 'q',
                         PAYLOAD: {'format':'json:suggest',
                                   'filter': 'type:Person',
                                   'q': None}}

    GND_PERSON_MAP = {DIRECT: {'label': 'label',
                           'uri': 'id'},
                      RULES: {'source': {RULE: '"GND"'},
                              'label_name': {RULE: '"{p1}".split("|")[0].strip()',
                                             FIELDS: {'p1': 'label'}},
                              'label_year': {RULE: '"{p1}".split("|")[1].strip() if "{p1}".split("|")[1].strip()[0].isnumeric() else ""',
                                             FIELDS: {'p1': 'label'}},
                              'label_profession': {RULE: '"{p1}".split("|")[2].strip() if "{p1}".split("|")[1].strip()[0].isnumeric() else "{p1}".split("|")[1].strip()',
                                                   FIELDS: {'p1': 'label'}}}}
    
    api = APIMapper(GND_PERSON_SOURCE, GND_PERSON_MAP)
    res = api.fetch_results('Doctor')
    pprint(res)
    
    return


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    main()
