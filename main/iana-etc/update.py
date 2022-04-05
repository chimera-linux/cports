url = "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xml"
_pver = self.template.pkgver
pkgver = f"{_pver[0:4]}-{_pver[4:6]}-{_pver[6:]}"
pattern = "<updated>([-\d]+)(?=</updated>)"

def fetch_versions(self, src):
    return map(lambda v: v.replace("-", ""), self.fetch_versions(src))
