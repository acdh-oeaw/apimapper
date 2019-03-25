import requests
from pprint import pprint

from apimapper import ResponseMapper
from apimapper import config
import json

def main():    

    DBPEDIA_URL = 'http://lookup.dbpedia.org/api/search/PrefixSearch'
    DBPEDIA_RESPONSE_MAP = {config.RESULT: 'results',
                            config.DIRECT: {'label': 'label',
                                            'uri': 'uri'}}
    response_mapper = ResponseMapper(DBPEDIA_RESPONSE_MAP)
    
    original_response = requests.get(DBPEDIA_URL, params={'QueryString': 'Rosalind Franklin'},
                                     headers = {'accept': 'application/json'}).content
    
    
    pprint('ORIGINAL RESPONSE\n{}'.format( original_response))
    mapped_response = response_mapper.get_mapped_response(json.loads(original_response))
    pprint('MAPPED RESPONSE\n{}'.format(mapped_response))

    return


if __name__ == '__main__':
    main()
