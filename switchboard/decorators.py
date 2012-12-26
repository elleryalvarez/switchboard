"""
switchboard.decorators
~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 Kyle Adams.
:license: Apache License 2.0, see LICENSE for more details.
"""

from functools import wraps

from webob.exc import HTTPNotFound, HTTPFound

from switchboard import operator


def switch_is_active(key, request, redirect_to=None, operator=operator):
    def _switch_is_active(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            if not operator.is_active(key, request):
                if not redirect_to:
                    raise HTTPNotFound('Switch \'%s\' is not active' % key)
                else:
                    raise HTTPFound(location=redirect_to)
            return func(*args, **kwargs)
        return wrapped
    return _switch_is_active
