url = "https://github.com/acpica/acpica/tags"
pattern = r"R([\d\_]+).tar.gz"


# be warned, this will break in 2100
def _mapv(ver):
    a, b, c = ver.split(".")
    return f"20{c}{a}{b}"


def fetch_versions(self, src):
    return map(_mapv, self.fetch_versions(src))
