from graphs.relationship import Relationship


class RelationshipRegistry(object):

    def __init__(self, name=None):
        self.name = name
        self.relationships = {}

    def _new_relationship(self, name, inverse):
        r = type(name, (Relationship,), {"NAME":name, 'registry':self})
        r.inverse_type = type(name, (Relationship,), {"NAME":inverse, 'registry':self})

        r.inverse_type.inverse_type = r

        yield r
        yield r.inverse_type

    def new_relationship(self, name, inverse):
        for r in self._new_relationship(name, inverse):
            self.relationships[r.NAME] = r
            yield r

    def get_by_name(self, name):
        return self.relationships[name]