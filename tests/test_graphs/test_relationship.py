import unittest

from graphs.relationship_registry import RelationshipRegistry


class TestRelationship(unittest.TestCase):

    def test_registry(self):
        rr = RelationshipRegistry()
        Above, Below = rr.new_relationship(name="Above", inverse="Below")
        self.assertEqual(rr.get_by_name("Above"), Above)
        self.assertEqual(rr.get_by_name("Below"), Below)


    def test_relationship_inversion(self):
        rr = RelationshipRegistry()
        Above, Below = rr.new_relationship(name="Above", inverse="Below")
        self.assertEqual(Above.inverse_type, Below)
        self.assertEqual(Below.inverse_type, Above)

    def test_relationship_link(self):
        rr = RelationshipRegistry()
        Above, Below = rr.new_relationship(name="Above", inverse="Below")
        self.assertEqual(Above.registry, rr)
        self.assertEqual(Below.registry, rr)

    def test_relationship_instance(self):
        rr = RelationshipRegistry("XX")
        Before, After = rr.new_relationship(name="Before", inverse="After")
        a = Before("A", "B")
        b = a.inverse
        self.assertEqual(b, After("B", "A"))

    def test_relationship_instance_double_invert(self):
        rr = RelationshipRegistry("XX")
        Before, After = rr.new_relationship(name="Before", inverse="After")
        a = Before("A", "B")
        self.assertEqual(a.inverse.inverse, a)

    def test_str(self):
        rr = RelationshipRegistry(name="Foo")
        Before, After = rr.new_relationship(name="Before", inverse="After")
        a = Before("A", "B")
        self.assertEqual("A Before B (Foo)", str(a))

    def test_hashable(self):
        rr = RelationshipRegistry(name="Foo")
        Before, After = rr.new_relationship(name="Before", inverse="After")
        a = Before("A", "B")
        self.assertEqual(hash(a), hash(a.inverse.inverse))

    def test_identical(self):
        rr = RelationshipRegistry(name="Foo")

        Before1, After1 = rr.new_relationship(name="Before", inverse="After")
        Before2, After2 = rr.new_relationship(name="Before", inverse="After")

        self.assertIs(Before1, Before2)
        self.assertIs(After1, After2)


    # def test_identical_objects_in_other_registries_have_different_hashes(self):
    #     rr1 = RelationshipRegistry(name="Foo")
    #     Before1, _ = rr1.new_relationship(name="Before", inverse="After")
    #
    #     rr2 = RelationshipRegistry(name="Bar")
    #     Before1, _ = rr2.new_relationship(name="Before", inverse="After")
    #
    #     a1 = Before1("A", "B")
    #     a2 = Before1("A", "B")
    #
    #     self.assertNotEqual(hash(a1), hash(a2))
