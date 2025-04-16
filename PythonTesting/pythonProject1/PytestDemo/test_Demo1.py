#Any pytest file should start with test_
#pytest method name should always start with test
#any code must be wrapped in method only
#method naming should be done carefully with meaning.
#-k stands for method names execution(meaningful name for all the cases you want to choose Ex: "greet" in line 18
# -s logs of the output
#-v more info metadata
#you can run specific test case by using py.test<filename>
#you can select particular test cases together and run them by marking them using pytest.mark.(tagname) and -m in cmd prmpt
#skip test using @pytest.mark.skip
#@pytest.mark.xfail

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    print("Hello")


def test_greet():
    print("GM")


def test_assert():
    msg = "hi"
    assert msg=="hai"

