from .config.config import *
import logging

logger = logging.getLogger(__name__)


class ResponseMapper:
    def __init__(self, mapping=None):
        self.mapping = mapping
        return

    def _is_relevant_result(self, res_item):
        '''
        called for every item in the response (res_item)
        returns True if the response matches the "filter" condition specified in the configuration
        '''
        for filter_field, filter_value in self.mapping.get(FILTER, {}).items():
            if res_item.get(filter_field) != filter_value:
                return False
            else:
                pass
        return True

    def _map_item_rules(self, res_item):
        # Rule based mapping
        mapped_schema = {}
        for to_key, rule_data in self.mapping.get(RULES, {}).items():
            logger.debug('Mapping rule: %s <- %s', to_key, rule_data)
            rule = rule_data.get(RULE)
            fields = rule_data.get(FIELDS, {})
            eval_params = {}
                    
            # obtain values from response to evauate the "mapping rule"
            for k, v in fields.items():
                eval_params[k] = res_item.get(v, '')
                logging.debug('%s: %s', k, rule.format(**eval_params))

            try:
                mapped_schema[to_key] = eval(rule.format(**eval_params))
                logging.debug('%s: %s', to_key, mapped_schema[to_key])
            except Exception as e:
                # Bad rule: keep calm and carry on
                mapped_schema[to_key] = ''
                logging.warning('Encountered bad rule (%s) for input "%s"',
                                rule_data, eval_params)
                logging.warning(e)
        return mapped_schema
    
    def _map_item_direct(self, res_item):
        # Direct field based mapping
        mapped_schema = {}
        for to_key, from_key in self.mapping.get(DIRECT, {}).items():
            mapped_schema[to_key] = res_item.get(from_key)
        return mapped_schema
    
    def _map_item(self, res_item):
        # filter and map response item
        if self._is_relevant_result(res_item):
            # append mapped schema to response
            direct_map = self._map_item_direct(res_item)
            rule_map = self._map_item_rules(res_item)            
            return {**direct_map, **rule_map}
        
        return {}
    
    def get_mapped_response(self, original_response):
        '''
        map original response to fields specified in config
        '''
        if not self.mapping:
            logging.error('No mapping found. Returning as-is.')
            return original_response
        
        if self.mapping.get(RESULT):
            original_response = original_response.get(self.mapping.get(RESULT))


        mapped_response = []
        for res_item in original_response:
            mapped_item = self._map_item(res_item)
            if len(mapped_item):
                mapped_response.append(mapped_item)
        
        return mapped_response
        

    
        
