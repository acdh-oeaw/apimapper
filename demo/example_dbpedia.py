from apimapper import APIMapper
from apimapper import config
import logging
from pprint import pprint


def main():
    DBPEDIA_SOURCE = {config.URL: 'http://lookup.dbpedia.org/api/search/PrefixSearch?',
                      config.QUERY_FIELD: 'QueryString',
                      config.PAYLOAD: {'QueryString': None}}

    DBPEDIA_MAP = {config.RESULT: 'results',
                   config.DIRECT: {'label': 'label',
                                   'uri': 'uri'}}

    api = APIMapper(DBPEDIA_SOURCE, DBPEDIA_MAP)
    res = api.fetch_results('Shania')
    pprint(res)
    
    return


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    main()
