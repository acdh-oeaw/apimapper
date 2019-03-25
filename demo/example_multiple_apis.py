'''
Query different APIs with different payloads and obtain response in a common schema if preferred
'''
from apimapper import APIMapper
from apimapper import config
from pprint import pprint

GND_PERSON_MAP = {config.DIRECT: {'uri': 'id',
	       	 		  'label': 'label'}}
           
VIAF_PERSON_MAP = {config.RESULT: 'result',
                   config.FILTER: {'nametype': 'personal'},
                   config.DIRECT: {'label': 'displayForm'},
                   config.RULES: {'uri': {config.RULE: '"http://www.viaf.org/viaf/{p1}"',
                                          config.FIELDS: {'p1': 'viafid'}}}}

GND_PERSON_SOURCE = {config.URL: 'https://lobid.org/gnd/search',
                     config.QUERY_FIELD: 'q',
                     config.PAYLOAD: {'format':'json:suggest',
                                      'filter': 'type:Person'}}
    
VIAF_PERSON_SOURCE =  {config.URL: 'http://www.viaf.org/viaf/AutoSuggest',
                       config.QUERY_FIELD: 'query'}
           

def main():
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

    
                
        
            
        
