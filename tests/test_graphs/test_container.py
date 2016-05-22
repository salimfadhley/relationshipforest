import unittest

from graphs.container import Container
from graphs.relationship_registry import RelationshipRegistry


class TestContainer(unittest.TestCase):

    def test_instance(self):
        c = Container()


    def test_stuff_in_contiainer(self):
        c = Container().add("X")
        self.assertTrue("X" in c)

    def test_relationship_add(self):
        rr = RelationshipRegistry()
        c = Container(relationship_registry=rr).add_related("X", "Y", "Above")
        Above, Below = rr.new_relationship(name="Above", inverse="Below")


        self.assertTrue("X" in c)
        self.assertTrue("Y" in c)
        self.assertTrue(Above("X", "Y") in c)
        self.assertTrue(Below("Y", "X") in c)





