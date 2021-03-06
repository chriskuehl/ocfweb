from textwrap import dedent

import pytest
import requests
from django.core.urlresolvers import NoReverseMatch
from django.core.urlresolvers import reverse

from ocfweb.urls import urlpatterns


def assert_does_not_error(running_server, path):
    path = running_server + path
    resp = requests.get(path)
    if resp.status_code != 200:
        raise AssertionError(
            dedent('''\
            Should have received status code 200, but instead received {resp.status_code}.

            Full path: {path}

            The response body was:
            {resp.content}''').format(path=path, resp=resp)
        )


def _get_reversed_urlpatterns():
    """Yields a list of all URLs that we can reverse with default args."""
    for urlpattern in urlpatterns:
        try:
            path = reverse(urlpattern.name, *urlpattern.default_args)
        except NoReverseMatch:
            pass
        else:
            yield path


@pytest.mark.parametrize('path', _get_reversed_urlpatterns())
def test_view_does_not_error_with_default_args(running_server, path):
    assert_does_not_error(running_server, path)
