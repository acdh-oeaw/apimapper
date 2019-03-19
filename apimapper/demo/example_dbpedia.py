from apimapper.apimapper import APIMapper
from apimapper.config.config import *
import logging
from pprint import pprint


def main():
    DBPEDIA_SOURCE = {URL: 'http://lookup.dbpedia.org/api/search/PrefixSearch?',
                      QUERY_FIELD: 'QueryString',
                      PAYLOAD: {'QueryString': None}}

    DBPEDIA_MAP = {RESULT: 'results',
                   DIRECT: {'label': 'label',
                           'uri': 'uri'}}

    api = APIMapper(DBPEDIA_SOURCE, DBPEDIA_MAP)
    res = api.fetch_results('Shania')
    pprint(res)
    
    return


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    main()
