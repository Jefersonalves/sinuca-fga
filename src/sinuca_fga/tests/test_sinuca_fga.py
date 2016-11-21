import pytest
import sinuca_fga


def test_project_defines_author_and_version():
    assert hasattr(sinuca_fga, '__author__')
    assert hasattr(sinuca_fga, '__version__')
