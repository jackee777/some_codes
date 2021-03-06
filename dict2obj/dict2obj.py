class dict2obj(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.items():
            if isinstance(value, dict):
                setattr(self, key, dict2obj(value))
            elif isinstance(value, list) and \
                len(value) != 0 and isinstance(value[0], dict):
                setattr(self, key, 
                        [dict2obj(val) for val in value])
            else:
                setattr(self, key, value)