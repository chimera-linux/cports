url = "https://github.com/floriankirsch/OpenCSG/tags"
pattern = r"opencsg-(\d+-\d+-\d+)-release"


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", "."), self.fetch_versions(src))
