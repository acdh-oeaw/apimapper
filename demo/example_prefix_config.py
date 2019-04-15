from apimapper import APIMapper
from apimapper import config
import logging
from pprint import pprint


def main():
    FISH_MONUMENT_TYPES_SOURCE = {config.URL: 'https://www.heritagedata.org/live/services/getConceptLabelMatch?',
                                  config.QUERY_FIELD: 'contains',
                                  config.PAYLOAD: {'contains': None,
                                                   'schemeURI': 'http://purl.org/heritagedata/schemes/eh_tmt2'}}

    FISH_MAP = {config.DIRECT: {'label': 'label',
                                'uri': 'uri'}}
    api = APIMapper(FISH_MONUMENT_TYPES_SOURCE, FISH_MAP)
    res = api.fetch_results('nia')
    pprint(res)
    
    return


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    main()

    
