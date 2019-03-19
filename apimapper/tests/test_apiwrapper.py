import pytest
from apimapper import APIMapper


def test_bad_config():
    config = {'notURL': 'definitely not a URL'}
    with pytest.raises(ValueError, match=r'.*Bad source, no URL*'):
        api = APIMapper(config)

    with pytest.raises(ValueError, match=r'.*Bad source, no URL*'):
        config = {'url': 'http://someurl'}
        api = APIMapper(config)

    return

def test_good_config():    
    config = {'URL': 'http://someurl'}
    api = APIMapper(config)
    return


def test_bad_responsecode():
    config = {'URL': 'http://google.com/madeup'}
    api = APIMapper(config)
    assert not len(api.fetch_results())
    return

def test_good_bad_responsecode():
    config = {'URL': 'http://google.com'}
    api = APIMapper(config)
    api.fetch_results()
    return
