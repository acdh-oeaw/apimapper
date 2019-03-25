# API Wrapper

## Install package
* from PyPi: 
    pip install apimapper
* from source: 
    pip install -e .

## Unit Testing
   tests> python -m pytest

## Usage
* Multiple APIs (GND and VIAF) mapped to a common JSON schema

VIAF only returns VIAF ID - which is contructed into a url using a "rule"
```
from apimapper import APIMapper
from apimapper import config

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
           

gnd = APIMapper(GND_PERSON_SOURCE, GND_PERSON_MAP)
viaf = APIMapper(VIAF_PERSON_SOURCE, VIAF_PERSON_MAP)
apis = [gnd, viaf]
results = []
for api in apis:            
    res = api.fetch_results('Pratchett')
    results.extend(res)

print(results)
```

* Using mapping rules

Splitting the GND label field into meaningful subparts
```
from apimapper import APIMapper
from apimapper import config

GND_PERSON_SOURCE = {config.URL: 'https://lobid.org/gnd/search',
                     config.QUERY_FIELD: 'q',
                     config.PAYLOAD: {'format':'json:suggest',
                                      'filter': 'type:Person'}}

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
res = api.fetch_results('Rosalind Franklin')
```

* More example usage in apimapper/demo
