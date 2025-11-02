pkgname = "dns-root-data"
pkgver = "2025080400"
pkgrel = 0
pkgdesc = "DNS root hints and DNSSEC trust anchor"
license = "custom:none"
url = "https://data.iana.org/root-anchors"
# we could use a source package to generate the files the same as debian
# does, but then we create a depcycle as that needs programs that come
# with unbound as well as some others
source = f"$(DEBIAN_SITE)/main/d/dns-root-data/dns-root-data_{pkgver}_all.deb"
sha256 = "e18670a21334e5f9aa4931ebeafea23b32479ee61b796329ce55ec74c530a3ce"


def install(self):
    self.install_files("usr/share/dns", "usr/share")
