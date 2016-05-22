from pyrsistent import s

class Container(object):

    def __init__(self, contents=None, relationships=None, relationship_registry=None):
        self.contents = contents or s()
        self.relationships = relationships or s()
        self.relationship_registry = relationship_registry

    def add(self, item) -> 'Container':
        return self.__class__(
            contents=self.contents.add(item),
            relationships=self.relationships,
            relationship_registry=self.relationship_registry
        )

    def add_related(self, a, b, rel:str):
        return self.add(a).add(b).relate(a,b,rel)

    def relate(self,a,b, rel_name:str):
        relationship_type = self.relationship_registry.get_by_name(rel_name)
        relationship = relationship_type(a,b)


        return self.__class__(
            contents=self.contents,
            relationships=self.relationships.add(relationship),
            relationship_registry=self.relationship_registry
        )

    def __iter__(self):
        yield from self.contents.__iter__()


Container_ = Container


