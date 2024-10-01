url = "https://github.com/project-spiel/libspeechprovider/tags"
pattern = r"SPEECHPROVIDER_([\d_]+)"


def fetch_versions(self, src):
    return map(lambda v: v.replace("_", "."), self.fetch_versions(src))
