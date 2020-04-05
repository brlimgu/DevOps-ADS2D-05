import pytest
from principal import soma


def test_soma():
    assert soma(2, 3) == 5
