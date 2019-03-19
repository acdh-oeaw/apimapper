'''
Query different APIs with different payloads and obtain response in a common schema if preferred
'''
from apimapper.apimapper import APIMapper
from pprint import pprint
from apimapper.config.config import *

GND_PERSON_MAP = {DIRECT: {'uri': 'id'},
                  RULES: {'source': {RULE: '"GND"'},
                          'label': {RULE: '"{p1}".split("|")[0].strip()',
                                    FIELDS: {'p1': 'label'}}}}
           
VIAF_PERSON_MAP = {RESULT: 'result',
                   FILTER: {'nametype': 'personal'},
                   DIRECT: {'label': 'displayForm'},
                   RULES: {'source': {RULE: '"VIAF"'},
                           'uri': {RULE: '"http://www.viaf.org/viaf/{p1}"',
                                   FIELDS: {'p1': 'viafid'}}}}

GND_PERSON_SOURCE = {URL: 'https://lobid.org/gnd/search',
                     QUERY_FIELD: 'q',
                     PAYLOAD: {'format':'json:suggest',
                               'filter': 'type:Person',
                               'q': None}}
    
VIAF_PERSON_SOURCE =  {URL: 'http://www.viaf.org/viaf/AutoSuggest',
                       QUERY_FIELD: 'query',
                       # only resources having the nametype "personal" will be returned                           
                       PAYLOAD: {'query': None}}
           

def main():
    query = 'Enya'
    gnd = APIMapper(GND_PERSON_SOURCE, GND_PERSON_MAP)
    viaf = APIMapper(VIAF_PERSON_SOURCE, VIAF_PERSON_MAP)
    apis = [gnd, viaf]
    results = []
    for api in apis:            
        api.fetch_results('Pratchett')
        results.extend(api.fetch_results(''))

    pprint(results)


if __name__ == '__main__':
    main()

    
                
        
            
        
