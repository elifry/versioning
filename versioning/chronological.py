import datetime as dt
from base import Version

class ChronologicalVersion(Version):
    def __init__(self, year=None, month=None, day=None, patch=0):
        # Default is today's date
        if year is None:
            year = dt.datetime.now().year
        if month is None:
            month = dt.datetime.now().month
        if day is None:
            day = dt.datetime.now().month
        
        super(ChronologicalVersion, self).__init__(
            primary=year,
            secondary=month,
            additional=day,
            patch=patch
        )
    
    def get_year(self):
        return self.primary
    
    def get_month(self):
        return self.secondary
    
    def get_day(self):
        return self.additional
    
    def get_patch(self):
        return self.patch
    
    def set_year(self, year):
        self.primary = year
        return self
    
    def set_month(self, month):
        self.secondary = month
        return self
    
    def set_day(self, day):
        self.additional = day
        return self
    
    def set_patch(self, patch):
        self.patch = patch
        return self
    
    def bump_year(self):
        return super(ChronologicalVersion, self).bump_primary()
    
    def bump_month(self):
        return super(ChronologicalVersion, self).bump_secondary()
    
    def bump_day(self):
        return super(ChronologicalVersion, self).bump_additional()
    
    def __getattribute__(self, __name:str):
        # Hide base class names
        if __name in {'bump_primary','bump_secondary','bump_additional'}: raise AttributeError
        return super().__getattribute__(__name)
    
    def __repr__(self):
        _year = str(self.primary).zfill(self.paddings["primaryPad"])
        _month = str(self.secondary).zfill(self.paddings["secondaryPad"])
        _patch = str(self.patch).zfill(self.paddings["patchPad"])
        
        if self.additional is None:
            return f"{_year}.{_month}.{_patch}"
        else:
            _day = str(self.additional).zfill(self.paddings["additionalPad"])
            return f"{_year}.{_month}.{_day}.{_patch}"
