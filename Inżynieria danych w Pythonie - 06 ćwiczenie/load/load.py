class JsonLoader:

    def __init__(self, orient = 'records', index = False, lines = True):
        self.orient = orient
        self.index = index 
        self.lines = lines
    
    def load(self, df, path):
        return df.to_json(path, orient = self.orient, index = self.index, lines = self.lines)