from lib.hello_world import HelloWorld
from hamcrest import assert_that, equal_to


class TestHelloWorld:
    def test_greet_default_name(self):
        result = HelloWorld.greet()
        assert_that(result, equal_to('Hello stranger!'))
