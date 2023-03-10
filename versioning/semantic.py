from base import Version

class SemanticVersion(Version):
    def __init__(self, major=1, minor=0, additional=None, patch=0):
        super(SemanticVersion, self).__init__(
            primary=major,
            secondary=minor,
            additional=additional,
            patch=patch
        )
    
    def bump_major(self):
        return super(SemanticVersion, self).bump_primary()
    
    def bump_minor(self):
        return super(SemanticVersion, self).bump_secondary()
    
    def __getattribute__(self, __name: str):
        # Hide base class names
        if __name in {'bump_primary','bump_secondary'}: raise AttributeError
        return super().__getattribute__(__name)
