class Deduplicator:

    def transform(self, data):
        return data[["Imię"]].drop_duplicates()