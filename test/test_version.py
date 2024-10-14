import sys
import pytest


@pytest.mark.xfail(sys.version_info < (3, 8), reason="requires Python 3.8")
def test_version() -> None:
    assert True
