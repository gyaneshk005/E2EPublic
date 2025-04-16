import pytest


@pytest.mark.smoke
@pytest.mark.xfail

def test_greet():
    print("GM")