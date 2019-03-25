'''
Query different APIs with different payloads and obtain response in a common schema if preferred
'''
from apimapper import APIMapper
from pprint import pprint
from apimapper import config

GND_PERSON_MAP = {config.DIRECT: {'uri': 'id'},
                  config.RULES: {'source': {config.RULE: '"GND"'},
                                 'label': {config.RULE: '"{p1}".split("|")[0].strip()',
                                           config.FIELDS: {'p1': 'label'}}}}
           
VIAF_PERSON_MAP = {config.RESULT: 'result',
                   config.FILTER: {'nametype': 'personal'},
                   config.DIRECT: {'label': 'displayForm'},
                   config.RULES: {'source': {config.RULE: '"VIAF"'},
                                  'uri': {config.RULE: '"http://www.viaf.org/viaf/{p1}"',
                                          config.FIELDS: {'p1': 'viafid'}}}}

GND_PERSON_SOURCE = {config.URL: 'https://lobid.org/gnd/search',
                     config.QUERY_FIELD: 'q',
                     config.PAYLOAD: {'format':'json:suggest',
                                      'filter': 'type:Person',a
                                      'q': None}}
    
VIAF_PERSON_SOURCE =  {config.URL: 'http://www.viaf.org/viaf/AutoSuggest',
                       config.QUERY_FIELD: 'query',
                       # only resources having the nametype "personal" will be returned                           
                       config.PAYLOAD: {'query': None}}
           

def main():
    query = 'Enya'
    gnd = APIMapper(GND_PERSON_SOURCE, GND_PERSON_MAP)
    viaf = APIMapper(VIAF_PERSON_SOURCE, VIAF_PERSON_MAP)
    apis = [gnd, viaf]
    results = []
    for api in apis:            
        res = api.fetch_results('Pratchett')
        results.extend(res)

    pprint(results)


if __name__ == '__main__':
    main()

    
                
        
            
        
