url = "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xml"
pattern = r"<updated>([-\d]+)</updated>"


def fetch_versions(self, src):
    # keep only global last updated date
    return map(
        lambda v: self.pkgver[:-8] + v.replace("-", ""),
        self.fetch_versions(src)[:1],
    )
