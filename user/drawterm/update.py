url = "https://git.9front.org/plan9front/drawterm/HEAD/log.html"
pattern = r"(\d\d\d\d/\d\d/\d\d)"  # YYYY/mm/dd


def fetch_versions(self, src):
    return map(lambda v: "0_git" + v.replace("/", ""), self.fetch_versions(src))
