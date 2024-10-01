url = "https://github.com/project-spiel/libspiel/tags"
pattern = r"SPIEL_([\d_]+)"


def fetch_versions(self, src):
    return map(lambda v: v.replace("_", "."), self.fetch_versions(src))
