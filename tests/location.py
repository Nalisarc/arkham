import unittest


class Location(object):

    def __init__(self,
                 name=None,
                 connections=(),
    ):

        self.name = name
        self.connections = connections



class LocationTests(unittest.TestCase):

    def test_can_spawn_location(self):
        test_location = Location()
        try:
            test_location
        except:
            self.fail("Test location failed to be called")


    def test_can_set_location_attributes(self):
        """A test to set various attributes of locations"""
        test_location = Location(name="Test")

        self.assertEqual(test_location.name, "Test")

    def test_locations_have_connections(self):
        """Test to make sure that locations can be passes a tuple of connections"""
        test_location = Location(connections=("t1","t2"))

        self.assertEqual(test_location.connections, ("t1","t2"))
