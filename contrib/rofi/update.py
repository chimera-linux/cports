pattern = r"([\d.]+\+wayland\d+)"


def fetch_versions(self, src):
    return map(lambda v: v.replace("+wayland", "_p"), self.fetch_versions(src))
