class Version():
    def __init__(self, primary=1, secondary=0, additional=None, patch=0):
        self.primary = primary
        self.secondary = secondary
        self.additional = additional
        self.patch = patch
        self.paddings = {
            "primaryPad": 0,
            "secondaryPad": 0,
            "additionalPad": 0,
            "patchPad": 0,
        }
   
    def __repr__(self):
        _primary = str(self.primary).zfill(self.paddings["primaryPad"])
        _secondary = str(self.secondary).zfill(self.paddings["secondaryPad"])
        _patch = str(self.patch).zfill(self.paddings["patchPad"])
        
        if self.additional is None:
            return f"{_primary}.{_secondary}.{_patch}"
        else:
            _additional = str(self.additional).zfill(self.paddings["additionalPad"])
            return f"{_primary}.{_secondary}.{_additional}.{_patch}"
    
    def bump_primary(self)
        self.primary = self.primary + 1
        self.secondary = 0
        if not (self.additional is None):
            self.additional = 0
        self.patch = 0
        return self

    def bump_secondary(self)
        self.secondary = self.secondary + 1
        if not (self.additional is None):
            self.additional = 0
        self.patch = 0
        return self
    
    def bump_additional(self):
        if not (self.additional is None):
            self.additional = self.additional + 1
            self.patch = 0
        return self
    
    def bump_patch(self):
        self.patch = self.patch + 1
        return self
    
    def update_paddings(self, paddings):
        self.paddings = paddings
        return self
