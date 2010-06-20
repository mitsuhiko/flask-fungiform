# -*- coding: utf-8 -*-
"""
    flaskext.fungiform
    ~~~~~~~~~~~~~~~~~~

    Implements fungiform support for Flask.

    :copyright: (c) 2010 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import absolute_import

from flask import _request_ctx_stack, redirect, url_for

import fungiform
from fungiform import widgets
from fungiform.exceptions import ValidationError
from fungiform.forms import *
__all__ = list(x for x in fungiform.forms.__all__ if x != 'FormBase')
__all__ += ['Form', 'ValidationError', 'widgets', 'validators']

try:
    from flaskext import babel
except ImportError:
    babel = None


class Form(FormBase):

    def _get_translations(self):
        ctx = _request_ctx_stack.top
        if ctx is not None and hasattr(ctx, 'babel_instance'):
            return babel.get_translations()
        return FormBase._get_translations(self)

    def _lookup_request_info(self):
        ctx = _request_ctx_stack.top
        if ctx is not None:
            return ctx.request

    def _get_wsgi_environ(self):
        if self.request_info is not None:
            return self.request_info.environ

    def _autodiscover_data(self):
        if self.request_info.method in ('PUT', 'POST'):
            return self.request_info.form
        return self.request_info.args

    def _redirect_to_url(self, url):
        return redirect(url)

    def _resolve_url(self, args, kwargs):
        return url_for(*args, **kwargs)

    def _get_session(self):
        ctx = _request_ctx_stack.top
        if ctx is not None:
            return ctx.session
