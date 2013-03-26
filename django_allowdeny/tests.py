from mock import Mock
from django.http import HttpResponseForbidden
from django.test import TestCase

import middleware


class AllowDenyMiddlewareTest(TestCase):
    def setUp(self):
        middleware.ALLOW_DENY_SETTINGS = middleware.ALLOW_DENY_DEFAULTS.copy()
        self.m = middleware.AllowDenyMiddleware()
        self.request = Mock()
        self.request.META = {}

    def test_00100(self):
        '''
        Testing default settings
        '''

        self.request.META['REMOTE_ADDR'] = '192.168.1.1'
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

    def test_00200(self):
        '''
        Testing ORDER: (allow, deny) ALLOW ('192.168.1.1')
        '''

        self.request.META['REMOTE_ADDR'] = '192.168.1.1'
        middleware.ALLOW_DENY_SETTINGS['ALLOW'] = list(('192.168.1.1',))
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

        self.request.META['REMOTE_ADDR'] = '192.168.1.2'
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

    def test_00201(self):
        '''
        Testing ORDER: (allow, deny) DENY ('192.168.1.1')
        '''

        self.request.META['REMOTE_ADDR'] = '192.168.1.1'
        middleware.ALLOW_DENY_SETTINGS['DENY'] = list(('192.168.1.1',))
        response = self.m.process_request(self.request)
        self.assertTrue(isinstance(response, HttpResponseForbidden))

        self.request.META['REMOTE_ADDR'] = '192.168.1.2'
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

    def test_00202(self):
        '''
        Testing ORDER: (allow, deny) ALLOW ('192.168.1.1') DENY ('192.168.1.1')
        '''

        self.request.META['REMOTE_ADDR'] = '192.168.1.1'
        middleware.ALLOW_DENY_SETTINGS['ALLOW'] = list(('192.168.1.1',))
        middleware.ALLOW_DENY_SETTINGS['DENY'] = list(('192.168.1.1',))
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

        self.request.META['REMOTE_ADDR'] = '192.168.1.2'
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

    def test_00203(self):
        '''
        Testing ORDER: (allow, deny) ALLOW ('all')
        '''

        self.request.META['REMOTE_ADDR'] = '192.168.1.1'
        middleware.ALLOW_DENY_SETTINGS['ALLOW'] = list(('all',))
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

        self.request.META['REMOTE_ADDR'] = '192.168.1.2'
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

    def test_00204(self):
        '''
        Testing ORDER: (allow, deny) DENY ('all')
        '''

        self.request.META['REMOTE_ADDR'] = '192.168.1.1'
        middleware.ALLOW_DENY_SETTINGS['DENY'] = list(('all',))
        response = self.m.process_request(self.request)
        self.assertTrue(isinstance(response, HttpResponseForbidden))

        self.request.META['REMOTE_ADDR'] = '192.168.1.2'
        response = self.m.process_request(self.request)
        self.assertTrue(isinstance(response, HttpResponseForbidden))

    def test_00205(self):
        '''
        Testing ORDER: (allow, deny) ALLOW ('all') DENY ('all')
        '''

        self.request.META['REMOTE_ADDR'] = '192.168.1.1'
        middleware.ALLOW_DENY_SETTINGS['ALLOW'] = list(('all',))
        middleware.ALLOW_DENY_SETTINGS['DENY'] = list(('all',))
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

        self.request.META['REMOTE_ADDR'] = '192.168.1.2'
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

    def test_00300(self):
        '''
        Testing ORDER: (deny, allow) ALLOW ('192.168.1.1')
        '''

        self.request.META['REMOTE_ADDR'] = '192.168.1.1'
        middleware.ALLOW_DENY_SETTINGS['ORDER'] = list(('deny', 'allow'))
        middleware.ALLOW_DENY_SETTINGS['ALLOW'] = list(('192.168.1.1',))
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

        self.request.META['REMOTE_ADDR'] = '192.168.1.2'
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

    def test_00301(self):
        '''
        Testing ORDER: (deny, allow) DENY ('192.168.1.1')
        '''

        self.request.META['REMOTE_ADDR'] = '192.168.1.1'
        middleware.ALLOW_DENY_SETTINGS['ORDER'] = list(('deny', 'allow'))
        middleware.ALLOW_DENY_SETTINGS['DENY'] = list(('192.168.1.1',))
        response = self.m.process_request(self.request)
        self.assertTrue(isinstance(response, HttpResponseForbidden))

        self.request.META['REMOTE_ADDR'] = '192.168.1.2'
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

    def test_00302(self):
        '''
        Testing ORDER: (deny, allow) ALLOW ('192.168.1.1') DENY ('192.168.1.1')
        '''

        self.request.META['REMOTE_ADDR'] = '192.168.1.1'
        middleware.ALLOW_DENY_SETTINGS['ORDER'] = list(('deny', 'allow'))
        middleware.ALLOW_DENY_SETTINGS['ALLOW'] = list(('192.168.1.1',))
        middleware.ALLOW_DENY_SETTINGS['DENY'] = list(('192.168.1.1',))
        response = self.m.process_request(self.request)
        self.assertTrue(isinstance(response, HttpResponseForbidden))

        self.request.META['REMOTE_ADDR'] = '192.168.1.2'
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

    def test_00303(self):
        '''
        Testing ORDER: (deny, allow) ALLOW ('all')
        '''

        self.request.META['REMOTE_ADDR'] = '192.168.1.1'
        middleware.ALLOW_DENY_SETTINGS['ORDER'] = list(('deny', 'allow'))
        middleware.ALLOW_DENY_SETTINGS['ALLOW'] = list(('all',))
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

        self.request.META['REMOTE_ADDR'] = '192.168.1.2'
        response = self.m.process_request(self.request)
        self.assertEqual(response, None)

    def test_00304(self):
        '''
        Testing ORDER: (deny, allow) DENY ('all')
        '''

        self.request.META['REMOTE_ADDR'] = '192.168.1.1'
        middleware.ALLOW_DENY_SETTINGS['ORDER'] = list(('deny', 'allow'))
        middleware.ALLOW_DENY_SETTINGS['DENY'] = list(('all',))
        response = self.m.process_request(self.request)
        self.assertTrue(isinstance(response, HttpResponseForbidden))

        self.request.META['REMOTE_ADDR'] = '192.168.1.2'
        response = self.m.process_request(self.request)
        self.assertTrue(isinstance(response, HttpResponseForbidden))

    def test_00305(self):
        '''
        Testing ORDER: (deny, allow) ALLOW ('all') DENY ('all')
        '''

        self.request.META['REMOTE_ADDR'] = '192.168.1.1'
        middleware.ALLOW_DENY_SETTINGS['ORDER'] = list(('deny', 'allow'))
        middleware.ALLOW_DENY_SETTINGS['ALLOW'] = list(('all',))
        middleware.ALLOW_DENY_SETTINGS['DENY'] = list(('all',))
        response = self.m.process_request(self.request)
        self.assertTrue(isinstance(response, HttpResponseForbidden))

        self.request.META['REMOTE_ADDR'] = '192.168.1.2'
        response = self.m.process_request(self.request)
        self.assertTrue(isinstance(response, HttpResponseForbidden))
