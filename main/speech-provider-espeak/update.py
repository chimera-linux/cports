url = "https://github.com/project-spiel/speech-provider-espeak/tags"
pattern = r"SPEECH_PROVIDER_ESPEAK_([\d_]+)"


def fetch_versions(self, src):
    return map(lambda v: v.replace("_", "."), self.fetch_versions(src))
