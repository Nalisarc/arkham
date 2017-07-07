import unittest


class Location(object):

    def __init__(self):
        pass



class LocationTests(unittest.TestCase):

    def test_can_spawn_location(self):
        test_location = Location()
        try:
            test_location
        except:
            self.fail("Test location failed to be called")
