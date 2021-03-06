# Test for one implementation of the interface
from lexicon.providers.easyname import Provider
from integration_tests import IntegrationTests
from unittest import TestCase
from bs4 import BeautifulSoup

class EasynameProviderTests(TestCase, IntegrationTests):

    Provider = Provider
    provider_name = 'easyname'
    domain = 'lexicontest.astzweig.de'

    def _filter_post_data_parameters(self):
        return ['username', 'password']

    def _filter_headers(self):
        return ['Cookie']

    def _test_fallback_fn(self):
        return lambda x: 'placeholder_' + x if x != 'priority' else ''
