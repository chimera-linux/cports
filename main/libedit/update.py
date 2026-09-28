# we have a forked version but this still usefully pings when this one might
# have a useful change or upstream source changes meaningfully
url = "https://www.thrysoee.dk/editline"
pattern = r"([\d]+\-[\d]+\-[\d]+) "
# different versioning scheme
ignore = ["20240808"]


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", ""), self.fetch_versions(src))
