import unittest


class Location(object):

    def __init__(self):
        pass



class LocationTests(unittest.TestCase):

    def test_can_spawn_location(self):
        test = Location()
        try:
            test
        except:
            self.fail("Test location failed to be called")
