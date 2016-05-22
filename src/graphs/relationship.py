class Relationship(object):

    NAME = None
    registry = None
    inverse_type = None


    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "%s %s %s (%s)" % (
            self.a,
            self.NAME,
            self.b,
            self.registry.name
        )

    def __repr__(self):
        return "<%s.%s %s>" % (self.__class__.__module__, self.__class__.__name__, self)

    @property
    def inverse(self):
        return self.inverse_type(self.b, self.a)

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            if self.registry == other.registry:
                if self.a == other.a:
                    if self.b == other.b:
                        return True
        return False


