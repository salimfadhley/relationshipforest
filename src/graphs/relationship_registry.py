from graphs.relationship import Relationship


class RelationshipRegistry(object):

    def __init__(self, name=None):
        self.name = name
        self.relationships = {}

    def new_relationship(self, name, inverse):
        if name in self.relationships:
            r = self.relationships[name]
        else:
            r = type(name, (Relationship,), {"NAME":name, 'registry':self})
            r.inverse_type = type(name, (Relationship,), {"NAME":inverse, 'registry':self})
            r.inverse_type.inverse_type = r
            self.relationships[name] = r
            self.relationships[inverse] = r.inverse_type

        yield r
        yield r.inverse_type

    def get_by_name(self, name):
        return self.relationships[name]
