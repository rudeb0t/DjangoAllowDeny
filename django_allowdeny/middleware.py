import sys

from django.conf import settings
from django.http import HttpResponseForbidden
from django.template import loader

ALLOW_DENY_DEFAULTS = dict(
    ORDER = list(('allow', 'deny')),
    ALLOW = list(),
    DENY = list()
)

ALLOW_DENY_SETTINGS = ALLOW_DENY_DEFAULTS.copy()

ALLOW_DENY_SETTINGS.update(getattr(settings, 'ALLOW_DENY_SETTINGS', dict()))


class AllowDenyMiddleware(object):
    def allow(self, ip_address):
        if 'all' in ALLOW_DENY_SETTINGS['ALLOW']:
            return True
        return ip_address in ALLOW_DENY_SETTINGS['ALLOW']

    def deny(self, ip_address):
        if 'all' in ALLOW_DENY_SETTINGS['DENY']:
            return True
        return ip_address in ALLOW_DENY_SETTINGS['DENY']

    def process_request(self, request):
        print ALLOW_DENY_SETTINGS
        ip_address = request.META.get('REMOTE_ADDR', None)
        if ip_address:
            for task in ALLOW_DENY_SETTINGS['ORDER']:
                if task.lower() == 'allow' and self.allow(ip_address):
                    return None
                elif task.lower() == 'deny' and self.deny(ip_address):
                    return HttpResponseForbidden(loader.render_to_string('allowdeny/forbidden.html'))
        return None
